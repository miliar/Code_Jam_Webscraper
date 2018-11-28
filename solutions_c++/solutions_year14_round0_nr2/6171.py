/* 
 * File:   main.cpp
 * Author: Charles
 *
 * Created on 12 April 2014, 12:28
 */

#include <cstdlib>
#include <fstream>
#include <string>
#include <iomanip>
#include <limits>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv)
{
    const float cookieBaseRate = 2.0;
    
    const std::string answerPreamble("Case #");
    
    std::ofstream answers("Answers.txt");
    std::ifstream input("input.txt");
    
    int cases = 0;
    
    input >> cases;
    
    for(int i_cases = 0;i_cases < cases;i_cases++)
    {
        double cookieFarmRate = 0;
        double cookieFarmCost = 0;
        double cookieGoalQuantity = 0;    
        double timeToWin = 0;
        double timePreviousToWin = 0;
        
        input >> std::fixed >> std::setprecision(7) >> cookieFarmCost >> cookieFarmRate >> cookieGoalQuantity;
        for(int farmQuantity = 0;timeToWin <= timePreviousToWin;farmQuantity++)
        {
            double cookieProductionRate = cookieBaseRate;
            timePreviousToWin = timeToWin;
            timeToWin = 0;
            
            for(int i_farms = 0;i_farms < farmQuantity;i_farms++)
            {
                timeToWin += (cookieFarmCost / cookieProductionRate);
                cookieProductionRate += cookieFarmRate;
            }    
            
            timeToWin += cookieGoalQuantity / cookieProductionRate;           
            if(timePreviousToWin == 0) timePreviousToWin = timeToWin;
        }
        
        answers << answerPreamble;
        answers << (i_cases + 1);
        answers << ": ";
        answers << std::fixed << std::setprecision(7) << timePreviousToWin;
        answers << std::endl;
    }
    
    return 0;
}

