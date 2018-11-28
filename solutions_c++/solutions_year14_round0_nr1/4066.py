//
//  main.cpp
//  Magic Trick
//
//  Created by Dylan Stenico on 12/04/14.
//  Copyright (c) 2014 Dylan Stenico. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, const char * argv[])
{

    ifstream input("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Magic Trick/A-small-attempt0.in.txt");
    ofstream output("/Users/dylanstenico/Documents/School/InformationTechnology/2014/GoogleCodeJam/Magic Trick/A-small-practice.ou.txt");
    
    int tests;
    input >> tests;
    //cout << tests << " ";
    int m[4][2];
    for(int i = 0; i < tests; i++)
    {
        int row;
        input >> row;
        //cout << row << " "<< endl;
        for(int correct = 0; correct < row; correct++)
        {
            for(int x = 0; x < 4; x++)
            {
                int tmp;
                input >> tmp;
                m[x][0] = tmp;
            }
        }
        
        for(int correct = 0; correct < 4 - row; correct ++)
        {
            for(int x = 0; x < 4; x++)
            {
                int c;
                input >> c;
            }
        }
        
        input >> row;
        for(int correct = 0; correct < row; correct ++)
        {
            for(int x = 0; x < 4; x++)
            {
                input >> m[x][1];
            }
        }
        
        for(int correct = 0; correct < 4 - row; correct ++)
        {
            for(int x = 0; x < 4; x++)
            {
                int c;
                input >> c;
            }
        }
        
        int quanti = 0;
        int index = 0;
        for(int k = 0; k < 4; k++)
        {
            for(int z = 0; z < 4; z++)
            {
                if(m[k][0] == m[z][1])
                {
                    quanti++;
                    index = k;
                }
            }
        }
        if(quanti == 1)
        {
            output << "Case #" << i + 1 << ": " << m[index][0];
        }
        if(quanti ==0)
        {
            output << "Case #" << i + 1 << ": Volunteer cheated!" ;
        }
        if(quanti > 1)
        {
            output << "Case #" << i + 1 << ": Bad magician!" ;
        }
        output << endl;
        
    }
        
}

