//
//  main.cpp
//  Cookie_Clicker_Alpha
//
//  Created by Xiaochen Dai on 4/11/14.
//  Copyright (c) 2014 Xiaochen Dai. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>


using namespace std;

const char* small_data = "/Users/Rosalio/Desktop/Code Jam/Cookie_Clicker_Alpha/Cookie_Clicker_Alpha/B-small-attempt0.in";
const char* outputFile = "/Users/Rosalio/Desktop/Code Jam/Cookie_Clicker_Alpha/Cookie_Clicker_Alpha/B-small-attempt0.out";


double cookie(double C, double F, double rate, double balance)
{
    double waitTime = balance / rate;   // simply wait, no adding new farm
    double upgradeTime = C / rate;      // time for gaining enough cookies for a new farm
    double newRate = rate + F;
    double remainTime = balance / newRate;
    
    if(waitTime < upgradeTime + remainTime)
    {
        return waitTime;
    }
    else
    {
        return upgradeTime + cookie(C, F, newRate, balance);
    }
}


int main(int argc, const char * argv[])
{
    ifstream input;
    ofstream output;
    
    input.open(small_data);
    if(!input.is_open())
    {
        cout << "Error opening the input file!" << endl;
        return 1;
    }
    
    output.open(outputFile);
    if(!output.is_open())
    {
        cout << "Error opening the output file!" << endl;
        return 1;
    }
   
    // Main code starts from here;
    int numOfCases = 0;
    input >> numOfCases;
    
    for(int i = 1; i <= numOfCases; ++i)
    {
        double c = 0, f = 0, x = 0;
        input >> c;
        input >> f;
        input >> x;
        double t = cookie(c, f, 2.0, x);
        output.precision(7);
        output  << "Case #" << i << ": " << t << endl;
    }

    
    
    input.close();
    output.close();
    
    return 0;
}