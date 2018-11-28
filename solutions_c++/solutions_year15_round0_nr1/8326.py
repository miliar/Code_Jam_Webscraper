//
//  main.cpp
//  StandingOvation
//
//  Created by Divij Kumar on 4/11/15.
//  Copyright (c) 2015 Adobe Systems Inc. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;


int getNumFriendsNeededInAudience(int maxShyness, char* shyness)
{
    int totalFriendsReqd = 0;
    int numInAudience = shyness[0] - '0';
    
    //length of shyness is maxShyness +2
    for (int i=1; i<=maxShyness; i++)
    {
        //cout<<"s["<<i<<"]="<<shyness[i]<<"\n";
        if (numInAudience < i)
        {
            int numFriendsReqd = i - numInAudience;
            totalFriendsReqd += numFriendsReqd;
            numInAudience += numFriendsReqd;
        }

        numInAudience += shyness[i] - '0';
    }
    
    return totalFriendsReqd;
}


int main(int argc, const char * argv[]) {
    // insert code here...
    //std::cout << "Hello, World!\n";
    ifstream inFile;
    char inputFilename[] = "A-large.in";//"A-small-practice.in"; //"A-small-attempt0.in";
    inFile.open(inputFilename, ios::in);
    int numTestCases=0;
    
    if (inFile.is_open())
    {
        inFile>>numTestCases;
        for (int i=1; i<=numTestCases; i++)
        {
            char * shynessString = NULL;
            int maxShyness = 0;
            int numFriendsReqd = -1;
            inFile >> maxShyness;
            shynessString = new char[maxShyness+2];
            inFile>>shynessString;
            
            //cout<<"shyness:"<<shynessString<<endl;
            numFriendsReqd = getNumFriendsNeededInAudience(maxShyness, shynessString);
            cout<<"Case #"<<i<<": "<<numFriendsReqd<<"\n";
        }
    }
    
    return 0;
}
