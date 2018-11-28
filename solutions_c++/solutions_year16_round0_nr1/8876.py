//
//  main.cpp
//  A
//
//  Created by Adrien David on 09/04/2016.
//  Copyright (c) 2016 Adrien David. All rights reserved.
//

#include <iostream>
#include <fstream>

#include <array>
#include <vector>

//void getDigitsIn(long long aInput)
std::vector<size_t> getDigitsIn(long long aInput)
{
    //rank = 1;
    long long remainder = aInput;
    std::vector<size_t> result;
    while (remainder)
    {
        //result.push_back(aInput % std::pow(10, rank));
        result.push_back(remainder % 10);
        remainder -= result.back();
        remainder /= 10;
        //++rank;
    }

    return result;
}

int main(int argc, const char * argv[]) {

    if (argc != 2)
    {
        throw std::runtime_error("Must specify input file.");
    }

    std::ifstream input(argv[1]);
    std::ofstream output(argv[1]+std::string(".out"));

    int testCount;
    input >> testCount;

    std::string result;
    for (int testId = 0; testId != testCount; ++testId)
    {
        std::array<bool, 10> seenDigits;
        for (size_t i=0; i!=10; ++i)
        {
            seenDigits[i] = false;
        }

        long long startValue;
        input >> startValue;

        if (startValue==0)
        {
            result = "INSOMNIA";
        }
        else
        {
            auto seenAll = [&]()
            {
                for (size_t i=0; i!=10; ++i)
                {
                    if (!seenDigits[i]) return false;
                }
                return true;
            };

            int currentFactor = 0;
            int limit = 10000;
            while (!seenAll() & (currentFactor!=limit))
            {
                auto digits = getDigitsIn((++currentFactor) * startValue);

                //std::string dbg;
                //for (auto dig : digits)
                //{
                //    dbg += " " + std::to_string(dig);
                //}
                //result = dbg;

                for (size_t dig : digits)
                {
                    seenDigits[dig] = true;
                }
            }
            if (currentFactor == limit)
            {
                throw std::logic_error("Exceeded the recursion for " + std::to_string(startValue));
            }

            result = std::to_string(currentFactor * startValue);
        }
        output << "Case #" << testId+1 << ": " << result << std::endl;
    }

    return 0;
}
