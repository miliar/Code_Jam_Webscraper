//
//  main.cpp
//  CodeJam
//
//  Created by Sam Boles on 12/04/2014.
//  Copyright (c) 2014 Sam Boles. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream infile ("test.in");
    ofstream outfile("test.out");
    int testCases;
    int junk;
    int num;
    int numRow;
    int temp;
    int count;
    infile >> testCases;
    int nums[4];
    for(int i = 0; i < testCases; i++)
    {
        count = 0;
        infile >> numRow;
        
        for (int j = 0; j < 4; j++)
        {
            if(j+1 == numRow)
            {
                infile >> nums[0];
                infile >> nums[1];
                infile >> nums[2];
                infile >> nums[3];
            }
            else
            {
                infile >> junk;
                infile >> junk;
                infile >> junk;
                infile >> junk;
            }
        }
        
        infile >> numRow;
        for (int j = 0; j < 4; j++)
        {
            if(j+1 == numRow)
            {
                for(int k = 0; k < 4; k++)
                {
                    infile >> temp;
                    for (int l = 0; l < 4; l++)
                    {
                        if (temp == nums[l])
                        {
                            count ++;
                            num = temp;
                        }
                    }
                }
            }
            else
            {
                infile >> junk;
                infile >> junk;
                infile >> junk;
                infile >> junk;
            }
        }
        
        if (count == 0)
        {
            outfile << "Case #" << i+1 <<": Volunteer cheated!\n";
        }
        else if(count == 1)
        {
            outfile << "Case #" << i+1 << ": "<<num << '\n';
        }
        else
        {
            outfile << "Case #" << i+1 <<": Bad magician!\n";
        }
    }
    system("pwd");
    return 0;
}

