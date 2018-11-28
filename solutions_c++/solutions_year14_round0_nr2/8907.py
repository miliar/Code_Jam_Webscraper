//
//  main.cpp
//  GCJ_2014
//
//  Created by Adrien on 12/04/14.
//  Copyright (c) 2014 Adrien. All rights reserved.
//

#include <iostream>
#include <iomanip>

#include <fstream>
#include <cmath>


double constructionTime(int aFarmCount, double C, double I, double F)
{
    double time = 0.;
    for (int id = 0;
         id != aFarmCount;
         ++id)
     {
         time += (C / (I + id*F));
     }
    
    return time;
}

double timeToProduce(double X, double F, double I, int q)
{
    return X / (I + q*F);
}

int totalFarms(double X, double I, double F, double C)
{
    int q=0;
    while(true)
    {
        if ( timeToProduce(X, F, I, q) <= (timeToProduce(C, F, I, q) + timeToProduce(X, F, I, q+1)) )
        {
            return q;
        }
        
        ++q;
    }
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
        double C, F, X, I=2;
        inputFile >> C >> F >> X;
        
        std::cout << "Test #" << currentTestId << ": "
        << "C: " << C << " F: " << F << " X: " << X << std::endl;
        
        double result = 0.;

        if (C > 0)
        {
            int totalFarmsBuilt = totalFarms(X, I, F, C);
            std::cout << "Farms built:" << totalFarmsBuilt << std::endl;
            
            double cTime = constructionTime(totalFarmsBuilt, C, I, F);
            result = cTime + timeToProduce(X, F, I, totalFarmsBuilt);
        }
        
        outputFile << "Case #" << currentTestId << ": "
        << std::fixed << std::setprecision(7) << result << std::endl;
    }
    
    return 0;
}