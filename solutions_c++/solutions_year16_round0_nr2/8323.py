//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Alexandre Duong on 09/04/2016.
//  Copyright © 2016 Alexandre Duong. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <list>
#include <cmath>

int findIndex(const std::string& iString)
{
    int aIndex = -1;
    uint32_t aMax = 0;
    uint32_t aCount = 0;
    if(iString.size() == 1 && iString == "-")
    {
        aIndex = 0;
    }
    else if(iString.size() > 1)
    {
        for(size_t i=0; i<iString.size(); ++i)
        {
            if(iString[i] == '-')
            {
                ++aCount;
            }
            else if(aCount >= aMax && aCount != 0)
            {
                aMax = aCount;
                aCount = 0;
                aIndex = i-1;
            }
            else
            {
                aCount = 0;
            }
            
            if(i == iString.size() - 1)
            {
                if(aCount >= aMax && aCount != 0)
                {
                    aIndex = i;
                }
            }
        }
    }
    return aIndex;
}

void flip(std::string& ioString, size_t iIndex)
{
    for(size_t i=0; i<=iIndex; ++i)
    {
        if(ioString[i] == '-')
        {
            ioString[i] = '+';
        }
        else
        {
            ioString[i] = '-';
        }
    }
}

void print(std::ofstream& ioOutput, uint32_t i, uint32_t iCount)
{
    ioOutput << "Case #" << i << ": " << iCount << std::endl;
}

int main(int argc, const char * argv[]) {
    std::ifstream aStream(argv[1]);
    std::ofstream aOutput(argv[2]);
    if(aStream.is_open() && aOutput.is_open())
    {
        uint32_t T;
        aStream >> T;
        for(uint32_t i = 1; i <= T; ++i)
        {
            std::string aPancakeStack;
            aStream >> aPancakeStack;
            uint32_t aCount = 0;
            size_t aIndex = findIndex(aPancakeStack);
            while(aIndex != -1)
            {
                flip(aPancakeStack, aIndex);
                ++aCount;
                aIndex = findIndex(aPancakeStack);
            }
            print(aOutput, i, aCount);
        }
    }
}

