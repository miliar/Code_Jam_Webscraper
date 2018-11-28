//
//  main.cpp
//  A
//
//  Created by Adrien on 13/04/14.
//  Copyright (c) 2014 Adrien. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <fstream>

std::set<int> getChosenLine(std::ifstream & inputFile, int answer)
{
    int currentNumber;
    std::set<int> answerSet;
    
    for (int rowId = 1;
         rowId < 5;
         ++rowId)
    {
        for (int numberId = 1;
             numberId < 5;
             ++numberId)
        {
            inputFile >> currentNumber;
            
            if (rowId == answer)
            {
                answerSet.insert(currentNumber);
            }
        }
        
    }
    
    return answerSet;
}
int main(int argc, const char * argv[])
{
    std::ifstream inputFile(argv[1]);
    std::ofstream outputFile(argv[1]+std::string(".out"));
    
    int numberTests;
    inputFile >> numberTests;
    
    
    for (int currentTestId = 1;
         currentTestId <= numberTests;
         ++currentTestId)
    {
        int firstAnswer, secondAnswer;
        
        inputFile >> firstAnswer;
        std::set<int> firstSet = getChosenLine(inputFile, firstAnswer);
        
        inputFile >> secondAnswer;
        std::set<int> secondSet = getChosenLine(inputFile, secondAnswer);
        
        std::vector<int> intersection;
        
        std::set_intersection(firstSet.begin(), firstSet.end(),
                              secondSet.begin(), secondSet.end(),
                              std::back_inserter(intersection));
        
        
        outputFile << "Case #" << currentTestId << ": ";
        if (intersection.size() == 0)
        {
            outputFile << "Volunteer cheated!";
        }
        else if (intersection.size() > 1)
        {
            outputFile <<  "Bad magician!";
        }
        else
        {
            outputFile << intersection.at(0);
        }
        outputFile << std::endl;
    }
    
    return 0;
}

