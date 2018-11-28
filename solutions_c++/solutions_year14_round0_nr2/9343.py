//
//  main.cpp
//  Cookie_Clicker_Alpha
//
//  Created by kuaijianghua on 4/11/14.
//  Copyright (c) 2014 rampageworks. All rights reserved.
//

#include <iostream>
#include <unordered_map>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <iterator>
#include <iomanip>

using namespace std;

//C: Cost of farm
//F: extra per farm
//X: goal score
double calculateTimeWithFarmNumber(double C, double F ,double X, int farmNumber){
    double resultTime = 0;
    
    //Caculate buy farm time
    for (int i = 0; i < farmNumber; i++) {
        resultTime += C / (2 + F*i);
    }
    
    //Calculate wait time
    resultTime += X / (2 + F*farmNumber);
    
    return resultTime;
}


double calculateBestTime(double C, double F ,double X){
    
    int numberOfFarm = 0;
    double currentBestTime = calculateTimeWithFarmNumber(C, F, X, numberOfFarm);
    
    while (true) {
        double nextTime = calculateTimeWithFarmNumber(C, F, X, numberOfFarm+1);
        
        if (currentBestTime < nextTime) {
            return currentBestTime;
        }else{
            currentBestTime = nextTime;
            numberOfFarm++;
        }
    }
    
    return 0;
}

int main(int argc, const char * argv[])
{
    ifstream infile("inputFile");
    ofstream oufile("outputFile");
    
    //Get test case number
    string lineString;
    getline(infile, lineString);
    int testCaseNumber = atoi(lineString.c_str());
    
    for (int i = 0; i < testCaseNumber; i++) {
        getline(infile, lineString);
        
        istringstream iss(lineString);
        vector<string> conditions;
        copy(istream_iterator<string>(iss),
             istream_iterator<string>(),
             back_inserter<vector<string> >(conditions));
        
        double C = atof(conditions[0].c_str());
        double F = atof(conditions[1].c_str());
        double X = atof(conditions[2].c_str());
        
        double bestTime = calculateBestTime(C, F, X);
        
        oufile << "Case #" << i+1 << ": " << fixed <<setprecision(7) << bestTime << "\n";
    }
    
    infile.close();
    oufile.close();
    
    return 0;
}

