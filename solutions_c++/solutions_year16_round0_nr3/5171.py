#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <stdlib.h>
#include <math.h>

int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
size_t lastPrimeInd = sizeof(primes) / sizeof(primes[0]);

long long generateNumber(size_t len, long long num, int base, std::string &s)
{
    s = "1";
    for (size_t i = 1; i <= len - 2; ++i)
        if (((num >> (len - 2 - i)) % 2) == 0)
            s += "0";
        else
            s += "1";
    s += "1";

    return strtoll(s.c_str(), NULL, base);
}

bool jamcoinFound(size_t len, long long num)
{
    std::vector<long long> foundDivs;
    std::string str;

    for (size_t base = 2; base <= 10; ++base)
    {
        long long number = generateNumber(len, num, base, str);
        long long maxDiv = ceill(sqrtl(number)) + 1;

        bool found = false;
        for (size_t i = 0; i < lastPrimeInd; ++i)
        {
            if (number == primes[i])
                return false;

            if (number % primes[i] == 0)
            {
                foundDivs.push_back(primes[i]);
                found = true;
                break;
            }
        }

        if (found)
            continue;

        long long divs[] = {31, 37, 41, 43, 47, 49, 53, 59};
        size_t lastDivInd = (sizeof(divs) / sizeof(divs[0]));
        while(divs[lastDivInd - 1] < maxDiv)
        {
            for (size_t i = 0; i < lastDivInd; ++i)
                if (number % divs[i] == 0)
                {
                    foundDivs.push_back(divs[i]);
                    found = true;
                    break;
                }

            if (found)
                break;

            for (size_t i = 0; i < lastDivInd; ++i)
                divs[i] += 30;
        }
    }

    if (foundDivs.size() >= 9)
    {
        std::cout << str;
        for (size_t i = 0; i < foundDivs.size(); ++i)
            std::cout << " " << foundDivs[i];
        std::cout << std::endl;

        return true;
    }

    return false;
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <input data>" << std::endl;
        return 1;
    }

    std::ifstream f(argv[1]);
    if (!f)
    {
        std::cerr << "Error: can't open " << argv[1] << std::endl;
        return 2;
    }

    size_t caseCount = 0;
    f >> caseCount;
    for (size_t i = 0; i < caseCount; ++i)
    {
        std::cout << "Case #" << i + 1 << ":" << std::endl;
        size_t len = 0;
        size_t variantsCount = 0;

        f >> len >> variantsCount;

        long long maxVariantsCout = 1 << (len  - 2);

        for (long long j = 0; j < maxVariantsCout; ++j)
        {
            if (jamcoinFound(len, j))
                --variantsCount;

            if (variantsCount == 0)
                break;
        }
    }


    f.close();
    return 0;
}
