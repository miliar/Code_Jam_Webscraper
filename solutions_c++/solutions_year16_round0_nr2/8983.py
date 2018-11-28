//
//  main.cpp
//  B
//
//  Created by Adrien David on 09/04/2016.
//  Copyright (c) 2016 Adrien David. All rights reserved.
//

#include <iostream>
#include <fstream>

#include <array>
#include <string>
#include <vector>

char revert(char aIn)
{
    if (aIn == '+') return '-';
    else return '+';
}

std::string flip(const std::string & aStack, std::string::const_iterator aFirstUntouched, int &aMoveCount)
{
    long aLastFlippedIndex = (aFirstUntouched-aStack.cbegin())-1;
    if (aLastFlippedIndex >= aStack.size())
    {
        throw std::invalid_argument("Last flipped out of range.");
    }

    std::string replacement;
    for (int flipIndex=0; flipIndex<=aLastFlippedIndex; ++flipIndex)
    {
        replacement += revert(aStack[aLastFlippedIndex-flipIndex]);
    }

    ++aMoveCount;
    return replacement + aStack.substr(aLastFlippedIndex+1);
}

int main(int argc, const char * argv[])
{
    if (argc != 2)
    {
        throw std::runtime_error("Must specify input file.");
    }

    std::ifstream input(argv[1]);
    std::ofstream output(argv[1]+std::string(".out"));

    int testCount;
    input >> testCount;

    for (int testId = 0; testId != testCount; ++testId)
    {
        std::cout << "\t# case: " << testId+1 << std::endl;

        std::string panstack;
        input >> panstack;

        //for (std::string::size_type charId = panstack.size()-1; charId
        auto updateLastPlus = [](const std::string &aStack) -> std::string::const_iterator
        {
            std::string::const_reverse_iterator lastMinus = find(aStack.rbegin(), aStack.rend(), '-');
            return lastMinus.base();
        };
        std::string::const_iterator lastPlus = updateLastPlus(panstack);

        int moveCount=0;
        while (lastPlus != panstack.begin())
        {
            std::cout << "0) Last plus index: " << lastPlus - panstack.begin() << std::endl;
            auto firstMinus = std::find(panstack.begin(), panstack.end(), '-');
            if (firstMinus != panstack.begin())
            {
                panstack = flip(panstack, firstMinus, moveCount);
            }

            std::cout << "1) Maximized - chain: " << panstack << std::endl;

            lastPlus = updateLastPlus(panstack);
            panstack = flip(panstack, lastPlus, moveCount);
            std::cout << "2) Set to back: " << panstack << std::endl;

            lastPlus = updateLastPlus(panstack);

        }
        output << "Case #" << testId+1 << ": " << moveCount << std::endl;
    }
}
