//
//  main.cpp
//  magicTrick
//
//  Created by Si Te Feng on 2014-04-11.
//  Copyright (c) 2014 Si Te Feng. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void inputArray(int rowValues[], ifstream& infile);

int main(int argc, const char * argv[])
{
    
    string Tstring;
    long T;
    
    int firstChoice[4];
    int secondChoice[4];
    
    int matchStatus = 0;
    int result=0;
   
    ifstream infile;
    
    infile.open("A-small-attempt0.in", ios::in);
    
    if(infile.is_open())
    {
        infile >> Tstring;
        T = stol(Tstring, NULL, 10);
        
        for(int i=0; i<T ; i++)
        {
            cout << "Case #" << (i+1) << ": ";
            
            inputArray(firstChoice, infile);
            inputArray(secondChoice, infile);
            
            for(int j=0; j<4; j++)
            {
                for(int k=0; k<4; k++)
                {
                    if(firstChoice[j]==secondChoice[k])
                    {
                        if(matchStatus == 0)
                        {
                            matchStatus = 1;
                            result = firstChoice[j];
                        }
                        else
                        {
                            matchStatus = 2;
                            break;
                        }
                    }
                }
                
            }
            
            if(matchStatus == 0)
            {
                cout<< "Volunteer cheated!" << endl;
            }
            else if(matchStatus ==2)
            {
                cout << "Bad magician!" <<endl;
            }
            else
            {
                cout << result <<endl;
            }

            matchStatus = 0;
            result=0;
        }
        
    }
    
    return 0;
}


void inputArray(int rowValues[], ifstream& infile)
{
    string i1;
    string temp;
    int num;
    int first;
    
    infile >> i1;

    first = (int)stol(i1, NULL, 10);
    
    first--;
    
    int numToSkip = first*4;

    for(int j=0; j<numToSkip; j++)
    {
        infile >> temp;
    }
    for(int k=0; k<4; k++)
    {
        infile >> temp;
        num = (int)stol(temp, NULL, 10);
        rowValues[k] = num;
    }
    for(int l=0; l<(12-numToSkip); l++)
    {
        infile >> temp;
    }
    
}



