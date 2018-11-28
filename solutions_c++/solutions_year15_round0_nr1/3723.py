#ifndef STANDINGOVATION_H
#define STANDINGOVATION_H

#include <fstream>
#include <stdlib.h>
#include <iostream>

void standingovation(std::string file)
{
    std::ifstream input;
    input.open(file.c_str(), std::ios_base::in);
    if (input.is_open())
    {
        std::string line = "";
        std::getline(input, line);
        int testCases = atoi(line.c_str());
        for (int i = 0; i < testCases; i++)
        {
            std::getline(input, line);
            if (input.eof())
            {
                return;
            }

            int maxShyness = atoi(line.substr(0, line.find_first_of(' ')).c_str());
            std::string frequencies = line.substr(line.find_first_of(' ') + 1).c_str();

            int friendsRequired = 0;
            unsigned int prev = 0;
            for (unsigned int j = 0; j < frequencies.length(); j++)
            {
                if (frequencies[j] == '0')
                {
                    friendsRequired++;
                }
                else
                {
                    prev = j;
                    break;
                }
            }
            int audienceUsed = 0;
            for (unsigned int j = prev; j < frequencies.length(); j++)
            {
                audienceUsed += frequencies[j] - '0' - 1;
                if (frequencies[j] == '0')
                {
                    if (audienceUsed == -1)
                    {
                        audienceUsed = 0;
                        friendsRequired++;
                    }
                }
            }

            std::cout << "Case #" << i + 1 << ": " << friendsRequired << std::endl;
        }
    }
}

#endif // STANDINGOVATION_H
