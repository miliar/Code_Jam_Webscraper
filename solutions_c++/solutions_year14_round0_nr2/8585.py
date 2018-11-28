//
//  main.cpp
//  Cookies
//
//  Created by Eddie Kaiger on 4/12/14.
//  Copyright (c) 2014 Eddie Kaiger. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main(int argc, const char * argv[])
{
    
    int numberOfCases;
    double C, F, X, currentRate, time = 0;
    cin >> numberOfCases;
    
    double results[numberOfCases];
    
    
    for (int i = 0; i < numberOfCases; i++) {
        cin >> C >> F >> X;
        currentRate = 2;
		time = 0;        

        while ( (X/currentRate) > (C/currentRate) + (X/(currentRate + F))) {
            time += C / currentRate;
            currentRate += F;
        }
        
        results[i] = (X / currentRate) + time;
        
    }
    
    for (int i = 0; i < numberOfCases; i++) {
        cout << "Case #" << i + 1<< ": " << setprecision(7) << fixed << results[i] << endl;
    }

    
    return 0;
}

