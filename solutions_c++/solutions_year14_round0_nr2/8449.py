//
//  main.cpp
//  GCJ 2014 Q 1
//
//  Created by Saad Khoudmi on 12/04/14.
//  Copyright (c) 2014 Saad Khoudmi. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

void readData();
void processData();
void printResult();
void deleteData();


typedef struct TestData {
    double farmCost;
    double extraCookieRate;
    double cookieTarget;
    double estimatedTime;
    int numberOfFarmToBuild = 0;
}TestData;


int numberOfTests = 0;
TestData * testDatas;

void cookieFarm()
{
    
    readData();
    
    processData();
    
    printResult();
    
    deleteData();
}


void readData()
{
    ifstream input ("cookieFarm/B-large.in");
    
    input >> numberOfTests;
    
    testDatas = new TestData[numberOfTests];
    
    for (int i=0; i<numberOfTests; i++)
    {
        input >> testDatas[i].farmCost;
        input >> testDatas[i].extraCookieRate;
        input >> testDatas[i].cookieTarget;
    }
    
}

void processData()
{
    for (int testIndex=0; testIndex<numberOfTests; testIndex++)
    {
        bool shouldBuildAnotherFarm = true;
        double elapsedTime = 0.0;
        double currentBestEstimation = testDatas[testIndex].cookieTarget / 2.0;
        
        while (shouldBuildAnotherFarm) {
            double cookiesPerSecond = 2 + testDatas[testIndex].numberOfFarmToBuild * testDatas[testIndex].extraCookieRate;
            double remainingEstimatedTime = (testDatas[testIndex].cookieTarget) / cookiesPerSecond;
            
            if(remainingEstimatedTime + elapsedTime <= currentBestEstimation)
                currentBestEstimation = remainingEstimatedTime + elapsedTime;
            else
            {
                testDatas[testIndex].numberOfFarmToBuild--;
                shouldBuildAnotherFarm = false;
                continue;
            }
            
            double remainingEstimatedTimeForFarm = testDatas[testIndex].farmCost / cookiesPerSecond;
            
            if(remainingEstimatedTimeForFarm >= remainingEstimatedTime)
            {
                shouldBuildAnotherFarm = false;
            }
            else
            {
                elapsedTime += remainingEstimatedTimeForFarm;
                testDatas[testIndex].numberOfFarmToBuild++;
                
            }
        }
        testDatas[testIndex].estimatedTime = currentBestEstimation;
    }
}

void printResult()
{
    ofstream output ("cookieFarm/output");
    for (int i=0; i<numberOfTests; i++)
    {
        output << "Case #" << i+1 << ": " << fixed << setprecision(7) << testDatas[i].estimatedTime << endl;
    }
}

void deleteData()
{
    delete [] testDatas;
}
