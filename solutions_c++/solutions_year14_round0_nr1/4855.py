//
//  main.cpp
//  Magic_Trick
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

const char* small_data = "/Users/Rosalio/Desktop/Code Jam/Magic_Trick/Magic_Trick/A-small-attempt0.in";
const char* outputFile = "/Users/Rosalio/Desktop/Code Jam/Magic_Trick/Magic_Trick/A-small-attempt0.out";


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
    
    int caseNum = 0;
    input >> caseNum;
    
    for(int i = 0; i < caseNum; ++i)
    {
        int answerOne = 0;
        input >> answerOne;
        int cardsOne[4][4];
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                input >> cardsOne[j][k];
            }
        }
        
        int answerTwo = 0;
        input >> answerTwo;
        int cardsTwo[4][4];
        for(int j = 0; j < 4; j++)
        {
            for(int k = 0; k < 4; k++)
            {
                input >> cardsTwo[j][k];
            }
        }
    
        vector<int> v(8);
        vector<int>::iterator it;
        sort(&cardsOne[answerOne - 1][0], &cardsOne[answerOne - 1][0] + 4);
        sort(&cardsTwo[answerTwo - 1][0], &cardsTwo[answerTwo - 1][0] + 4);
        
        it = set_intersection(&cardsOne[answerOne -1][0],&cardsOne[answerOne - 1][0] + 4, &cardsTwo[answerTwo - 1][0], &cardsTwo[answerTwo - 1][0] + 4, v.begin());
        v.resize(it - v.begin());
      
        output << "Case #" << i + 1 << ": ";
        
        if(v.empty())
        {
            output << "Volunteer cheated!";
        }
        else if(v.size() > 1)
        {
            output << "Bad magician!";
        }
        else
        {
            output << v[0];
        }
        
        output << endl;
        
    }
    
    input.close();
    output.close();
    
    return 0;
}

