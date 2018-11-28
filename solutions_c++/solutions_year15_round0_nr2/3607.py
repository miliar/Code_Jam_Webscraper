#ifndef INFINITEPANCAKES_H
#define INFINITEPANCAKES_H

#include <fstream>
#include <stdlib.h>
#include <iostream>
#include <list>
#include <math.h>

void infinitepancakes(std::string file)
{
    std::ifstream input;
    input.open(file.c_str(), std::ios_base::in);
    if (input.is_open())
    {
        std::string line = "";
        std::getline(input, line);
        int caseNum = 1;
        while (!input.eof())
        {
            std::getline(input, line);
            if (input.eof())
            {
                return;
            }
            int diners = atoi(line.c_str());
            std::getline(input, line);
            std::list<int> stacks;
            for (int i = 0; i < diners; i++)
            {
                int pancakes = atoi(line.substr(0, line.find_first_of(' ')).c_str());
                line = line.substr(line.find_first_of(' ') + 1);
                stacks.push_back(pancakes);
            }

            int best = 1000;
            for (int i = 1; i < 1000; i++)  //i represents chunk size
            {
                std::list<int> tempStacks = stacks;
                int steps = 0;
                for (std::list<int>::iterator it = tempStacks.begin(); it != tempStacks.end(); it++)
                {
                    while (*it > i)
                    {
                        *it = *it - i;
                        tempStacks.push_back(i);
                        steps++;
                    }
                }
                steps += i;
                if (steps < best)
                {
                    best = steps;
                }
            }

            std::cout << "Case #" << caseNum << ": " << best << std::endl;
            caseNum++;
        }
    }
}

#endif // INFINITEPANCAKES_H
