#include <iostream>
#include <string>
#include <sstream>
#include <set>
#include <cmath>

typedef long long NumberType;
inline bool getDivisor(const NumberType nro, NumberType& divisor)
{
    if (nro % 2 == 0)
    {
        divisor = 2;
        return true;
    }
    const auto MaxDivisor = std::sqrt(nro);
    for (NumberType c = 3; c <= MaxDivisor; c += 2)
    {
        if (nro%c == 0)
        {
            divisor = c;
            return true;
        }
    }
    return false;
}

NumberType getNumberFromBase(NumberType* const number, const NumberType size, const NumberType base)
{
    NumberType result = 0;
    NumberType aBase = 1;
    for (auto i = 0; i < size; ++i)
    {
        result += number[i] * aBase;
        aBase *= base;
    }
    return result;
}

bool incrementNumber(NumberType* const number, const NumberType size)
{
    bool success(false);
    for (NumberType i = 1; i < size - 2; ++i)
    {
        if (number[i] == 1)
        {
            number[i] = 0;
        }
        else
        {
            number[i] = 1;
            success = true;
            break;
        }

    }
    return success;
}
inline void printNumber(NumberType* const number, const NumberType size)
{
    for (auto i = size - 1; i >= 0; --i)
    {
        std::cout << number[i];
    }
}

void calculateJamcoin(NumberType* const number, const NumberType size)
{
    NumberType divisors[9] = {0};
    bool isJamcoin;
    do
    {
        isJamcoin = true;
        for (NumberType i = 0; i < 9; ++i)
        {
            const NumberType base = i + 2;
            const auto numberWithBase = getNumberFromBase(number, size, base);
            if (!getDivisor(numberWithBase, divisors[i]))
            {
                isJamcoin = false;
                break;
            }
        }
    } while (!isJamcoin && incrementNumber(number, size));
    if (isJamcoin)
    {
        printNumber(number, size);

        for (auto divisor : divisors)
        {
            std::cout << " " << divisor;
        }
        std::cout << std::endl;

    }
    else
    {
        std::cout << "SOMETHING WAS WRONG" << std::endl;
    }

}

void calculateJamcoins(const NumberType length, const NumberType amountOfJamcoins)
{
    NumberType number[32] = {0};
    number[0] = 1;
    number[length - 1] = 1;
    for (NumberType i = 0; i < amountOfJamcoins; ++i)
    {
        calculateJamcoin(number, length);
        incrementNumber(number, length);
    }

}


int main()
{
    int T;

    std::cin >> T;
    for (auto i = 0; i < T; i++)
    {
        NumberType length;
        NumberType amountOfJamcoins;
        std::cin >> length;
        std::cin >> amountOfJamcoins;

        std::cout << "Case #" << i + 1 << ": " << std::endl;

        calculateJamcoins(length, amountOfJamcoins);
    }

    return 0;
}