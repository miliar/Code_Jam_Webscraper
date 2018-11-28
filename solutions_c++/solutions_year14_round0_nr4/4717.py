//
//  main.cpp
//  Deceitful_War
//
//  Created by Xiaochen Dai on 4/12/14.
//  Copyright (c) 2014 Xiaochen Dai. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const char* small_data = "/Users/Rosalio/Desktop/Code Jam/Deceitful_War/Deceitful_War/D-large.in";
const char* outputFile = "/Users/Rosalio/Desktop/Code Jam/Deceitful_War/Deceitful_War/D-large.out";


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
    
    int numTest = 0;
    input >> numTest;
    
    for(int i = 1; i <= numTest; ++i)
    {
        int N = 0;
        input >> N;
        vector<double> weights_Naomi(N);
        vector<double> weights_Ken(N);
        for(int j = 0; j < N; ++j)
        {
            input >> weights_Naomi[j];
        }
        for(int j = 0; j < N; ++j)
        {
            input >> weights_Ken[j];
        }
        
        int scoreDeceitfulWar = 0;
        int scoreWar = 0;
        
        sort(weights_Naomi.begin(), weights_Naomi.end());
        sort(weights_Ken.begin(), weights_Ken.end());
        //reverse(weights_Ken.begin(), weights_Ken.end());
        
        int pNaomi = N - 1, pKen = N - 1;
        while(pKen >= 0)
        {
            if(weights_Naomi[pNaomi] > weights_Ken[pKen])
            {
                ++scoreDeceitfulWar;
                --pNaomi;
                --pKen;
            }
            else
            {
                --pKen;
            }
        }
        
        // optimal war game
        pNaomi = N - 1;
        pKen = N - 1;
        
        while(pNaomi >= 0)
        {
            if(weights_Naomi[pNaomi] > weights_Ken[pKen])
            {
                ++scoreWar;
                --pNaomi;
            }
            else
            {
                --pNaomi;
                --pKen;
            }
        }
        
        cout << "Case #" << i << ": " << scoreDeceitfulWar << " " << scoreWar << endl;
        output << "Case #" << i << ": " << scoreDeceitfulWar << " " << scoreWar << endl;
    }
    
    input.close();
    output.close();
    
    return 0;
}


