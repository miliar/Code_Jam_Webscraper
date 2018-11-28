//
//  main.cpp
//  GCJ 2014 Q 1
//
//  Created by Saad Khoudmi on 12/04/14.
//  Copyright (c) 2014 Saad Khoudmi. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

void readData();
void processData();
void printResult();
void deleteData();


typedef struct TestData {
    int firstAnswer;
    int secondAnswer;
    int firstGrid[16];
    int secondGrid[16];
    int cardNumber = -1;
}TestData;


int numberOfTests = 0;
TestData * testDatas;

void magicTrick()
{
    
    readData();
    
    processData();
    
    printResult();
    
    deleteData();
}


void readData()
{
    ifstream input ("A-small-attempt2.in");
    
    input >> numberOfTests;
    
    testDatas = new TestData[numberOfTests];
    
    for (int i=0; i<numberOfTests; i++)
    {
        input >> testDatas[i].firstAnswer;
        
        for (int index = 0; index < 16; index++) {
            input >> testDatas[i].firstGrid[index];
        }
        
        input >> testDatas[i].secondAnswer;
        
        for (int index = 0; index < 16; index++) {
            input >> testDatas[i].secondGrid[index];
        }
    }
    
}

void processData()
{
    for (int testIndex=0; testIndex<numberOfTests; testIndex++)
    {
        for (int possibleAnswerIndex = 0;  possibleAnswerIndex < 4; possibleAnswerIndex++)
        {
            int possibleAnswer = testDatas[testIndex].firstGrid[(testDatas[testIndex].firstAnswer - 1)*4 + possibleAnswerIndex];
            
            for (int matchAnswerIndex = 0;  matchAnswerIndex < 4; matchAnswerIndex++)
            {
                int matchupAnswer = testDatas[testIndex].secondGrid[(testDatas[testIndex].secondAnswer - 1)*4 + matchAnswerIndex];
                if(possibleAnswer == matchupAnswer)
                {
                    if(testDatas[testIndex].cardNumber >= 0)
                        testDatas[testIndex].cardNumber = -2;
                    else
                        testDatas[testIndex].cardNumber = possibleAnswer;
                    break;
                }
            }
            if( testDatas[testIndex].cardNumber == -2)
                break;
            
        }
    }
}

void printResult()
{
    ofstream output ("output");
    for (int i=0; i<numberOfTests; i++)
    {
        output << "Case #" << i+1 << ": ";
        if(testDatas[i].cardNumber >= 0)
            output << testDatas[i].cardNumber << endl;
        else if (testDatas[i].cardNumber == -1)
        {
            output << "Volunteer cheated!" << endl;
        }
        else
        {
            output << "Bad magician!" << endl;
        }
    }
}

void deleteData()
{
    delete [] testDatas;
}
