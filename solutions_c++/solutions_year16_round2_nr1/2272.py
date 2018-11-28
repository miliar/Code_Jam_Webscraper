#include <iostream>
#include <string>
#include <cassert>
#include <algorithm>

void getNumber(std::string & input, std::string & phonenumber, std::string letters, std::string digit)
{
    while (true)
    {
        for (int i = 0; i < letters.size(); ++i)
        {
            if (std::count(input.begin(), input.end(), letters[i]) < std::count(letters.begin(), letters.end(), letters[i]))
                return;
        }
        for (int i = 0; i < letters.size(); ++i)
        {
            assert(input.find(letters[i]) != std::string::npos);
            input = input.erase(input.find(letters[i]), 1);
        }
        phonenumber += digit;
    }
}

int main()
{
    int T;
    std::cin >> T;
    for (int t = 0; t < T; ++t)
    {
        std::string input;
        std::cin >> input;
        std::string phonenumber;

        getNumber(input, phonenumber, "EIGHT", "8");
        getNumber(input, phonenumber, "ZERO", "0");
        getNumber(input, phonenumber, "SIX", "6");
        getNumber(input, phonenumber, "TWO", "2");
        getNumber(input, phonenumber, "SEVEN", "7");
        getNumber(input, phonenumber, "THREE", "3");
        getNumber(input, phonenumber, "FOUR", "4");
        getNumber(input, phonenumber, "FIVE", "5");
        getNumber(input, phonenumber, "NINE", "9");
        getNumber(input, phonenumber, "ONE", "1");

        std::sort(phonenumber.begin(), phonenumber.end());
        std::cout << "Case #" << (t+1) << ": " << phonenumber << std::endl;
    }
    return 0;
}
