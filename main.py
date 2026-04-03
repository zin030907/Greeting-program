print("Welcome to my greeting program!")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello", name, "!")

if age < 13:
    print("You're quite young and full of energy!")
elif age < 18:
    print("You're a teenager—perfect time to learn new skills!")
elif age < 25:
    print("You're in a great phase to build your future!")
else:
    print("Keep growing and learning every day!")

hobby = input("What is your favorite hobby? ")

print("That's awesome,", name, "!")
print("Spending time on", hobby, "can make you really good at it!")
