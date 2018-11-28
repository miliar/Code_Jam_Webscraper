//
//  main.cpp
//  Counting Sheep
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

template<class T>
void print(std::ofstream& ioStream, uint32_t i, T iSolution)
{
    ioStream << "Case #" << i << ": " << iSolution << std::endl;
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
            uint32_t N;
            aStream >> N;
            std::vector<bool> aTestVector;
            for(uint32_t j=0; j<10; ++j)
            {
                aTestVector.push_back(false);
            }
            
            if(N == 0)
                print(aOutput, i, "INSOMNIA");
            else
            {
                bool aTest = false;
                int aCounter = 1;
                while(aTest == false || aCounter > 1000)
                {
                    std::string NString = std::to_string(N * aCounter);
                    for(size_t j=0; j < NString.size(); ++j)
                    {
                        aTestVector[NString[j]-48] = true;
                    }
                    aTest = true;
                    for(size_t j=0; j<aTestVector.size(); ++j)
                    {
                        if(aTestVector[j] == false)
                        {
                            aTest = false;
                            ++ aCounter;
                            break;
                        }
                    }
                }
                if(aTest)
                    print(aOutput, i, N * aCounter);
                else
                    print(aOutput, i, "INSOMNIA");
            }
        }
    }
}