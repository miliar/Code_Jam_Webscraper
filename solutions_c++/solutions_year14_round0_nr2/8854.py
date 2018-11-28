//
//  main.cpp
//  CookieClickerAlpha
//
//  Created by Dmitry Fantastik on 4/13/14.
//  Copyright (c) 2014 funlife. All rights reserved.
//

#include <iostream>
#include <limits>

using namespace std;

double const kCoockiePerSecond = 2;

double calculateBestProfit(double dFarmCost, double dFarmProfit, double dGloal)
{
    double richGoal = dGloal / kCoockiePerSecond;
    double newReach = 0;
    double addition = kCoockiePerSecond;
    
    do {
        newReach += (dFarmCost / addition);
        addition += dFarmProfit;
    } while (richGoal > (newReach + (dGloal / addition)) && (richGoal = (newReach + (dGloal / addition))));
    
    return richGoal;
}

int main(int argc, const char * argv[])
{
    double ptrdResult[100];
    short sCount;
    double dFarmCost, dFarmProfit, dGoal;
    
    cin >> sCount;
    for (int i = 0; i < sCount; i++) {
        cin >> dFarmCost >> dFarmProfit >> dGoal;
        ptrdResult[i] = calculateBestProfit(dFarmCost, dFarmProfit, dGoal);
    }
    
    for (int i = 0; i < sCount; i++) {
        cout.precision(10);
        cout << "Case #" << i + 1 << ": " << ptrdResult[i] << endl;
    }
    
    return 0;
}

