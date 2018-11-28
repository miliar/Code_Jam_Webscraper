//
//  main.cpp
//  Cookie Clicker Alpha
//
//  Created by Ryan on 4/12/14.
//  Copyright (c) 2014 Ryan. All rights reserved.
//

#include <iostream>
#include <iomanip>

using namespace std;


bool shouldBuyFarm(double, double, double, double);


int main(int argc, const char * argv[])
{
    
    int numCases;
    cin >> numCases;
    
    double rate = 2.0;
    double goal;
    double extraCookieRate;
    double farmCost;
    double totalTime = 0;
    bool isDone = false;
    
    
    int counter = 1;
    while (cin >> farmCost >> extraCookieRate >> goal) {
        while (!isDone) {
            if ( shouldBuyFarm(goal, rate, farmCost, extraCookieRate) ) {
                totalTime += farmCost/rate;
                rate += extraCookieRate;
            }
            else {
                isDone = true;
                totalTime += goal/rate;
            }
        }
        cout << "Case #" << counter << ": " << fixed << setprecision(7) << totalTime << "\n";
        counter++;
        totalTime = 0;
        rate = 2.0;
        isDone = false;
    }
    
    return 0;
}

bool shouldBuyFarm(double goal, double rate, double farmCost, double extraCookieRate) {
    double timeTillEndWithoutFarm = goal/rate;
    double timeTillEndWithFarm = (farmCost/rate) + ( goal/(rate+extraCookieRate) );
    
    if (timeTillEndWithoutFarm > timeTillEndWithFarm) {
        return true;
    }
    else {
        return false;
    }
}

