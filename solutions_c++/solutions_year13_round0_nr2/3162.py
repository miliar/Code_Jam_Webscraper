//
//  main.cpp
//  CodeJam2
//
//  Created by Wade Norris on 4/12/13.
//  Copyright (c) 2013 norris. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int yardWidth;
int yardHeight;

bool columnPossible(int grassHeight, int input[100][100], int col)
{
    for(int i = 0; i<yardHeight; i++)
    {
        if(input[i][col] > grassHeight)
            return false;
    }
    
    return true;
}

bool rowPossible(int grassHeight, int input[100][100], int row)
{
    for(int i = 0; i<yardWidth; i++)
    {
        if(input[row][i] > grassHeight)
            return false;
    }
    
    return true;
}

bool yardPossible(int input[100][100])
{
    for(int j=0; j<yardHeight; j++)
    {
        for(int k=0; k<yardWidth; k++)
        {
            if(!columnPossible(input[j][k], input, k) && !rowPossible(input[j][k], input, j))
            {
                return false;
            }
        }
    }
    
    return true;
}

int main (int argc, char* argv[]) {
    string line;
    ifstream myfile (argv[1]);
    
    if (!myfile.is_open())
    {
        cout << "Error opening file!" << endl;
        return 0;
    }
    
    getline (myfile,line);
    
    int numTestCases = atoi(line.c_str());
    
    for(int i=0; i<numTestCases; i++)
    {
        myfile >> yardHeight;
        myfile >> yardWidth;
        
        myfile.ignore(10000, '\n');

        int input[100][100];
        
        for(int j=0; j<yardHeight; j++)
        {
            for(int k=0; k<yardWidth; k++)
            {
                myfile >> input[j][k];
            }
            myfile.ignore(10000, '\n');
        }
        
        if(yardPossible(input))
        {
            cout << "Case #" << i+1 << ": YES" << endl;
        }
        else
        {
            cout << "Case #" << i+1 << ": NO" << endl;
        }
        
    }
    
    myfile.close();
    
    return 0;
}


