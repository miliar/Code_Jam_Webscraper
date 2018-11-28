//
//  main.cpp
//  Standing Ovation
//
//  Created by Xiaochen Dai on 4/10/15.
//  Copyright (c) 2015 Xiaochen Dai. All rights reserved.
//

#include <iostream>
#include <cstdlib>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const char* small_data = "/Users/Rosalio/Desktop/Code Jam/Standing Ovation/Standing Ovation/A-large.in";
const char* outputFile = "/Users/Rosalio/Desktop/Code Jam/Standing Ovation/Standing Ovation/A-large.out";

int getNumOfFriends(int maximum, string data) {
    int numToInvite = 0;
    int numOfStanding = 0;
    
    for(int level = 0; level <= maximum; level++) {
        int numAtLevel = data.at(level) - '0';
        if(level == 0 || numOfStanding >= level) {
            numOfStanding += numAtLevel;
        } else {
            int numToInviteAtThis = level - numOfStanding;
            numOfStanding += numToInviteAtThis;
            numOfStanding += numAtLevel;
            numToInvite += numToInviteAtThis;
        }
    }
    
    return numToInvite;
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
    
    int caseNum = 0;
    input >> caseNum;
    
    for(int i = 1; i <= caseNum; ++i)
    {
        int maxShyness = 0;
        input >> maxShyness;
        
        string audienceData;
        input >> audienceData;
        
        int result = getNumOfFriends(maxShyness, audienceData);
        
        output << "Case #" << i << ": ";
        
        output << result;
        
        output << endl;
    }
    
    input.close();
    output.close();
    
    return 0;
}
