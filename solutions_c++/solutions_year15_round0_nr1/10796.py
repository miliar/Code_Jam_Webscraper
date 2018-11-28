//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Pollo on 11/04/15.
//  Copyright (c) 2015 Pollo. All rights reserved.
//

#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    //Problem 1 - Standing Ovation
    int testCases;
    cin >> testCases;
    vector<int> output;
    
    for(int t = 0; t < testCases; t++)
    {
        int max = 0;
        string people;
        int friends = 0;
        int sLevel;
        
        cin >> sLevel;
        
        getline(cin, people, '\n');
        int length = sLevel + 1;
        
        for(int i = 0; i < length; i++)
        {
            max += people[i + 1] - 48;
            
            //cout << "Max - " + to_string(max);
            
            if(max < i + 1)
            {
                friends += i + 1 - max;
                max = i + 1;
            }
            
            //cout << "Friends - " + to_string(friends);
        }
        
        output.push_back(friends);
    }
    
    cout << endl;
    
    for(int i = 0; i < testCases; i++)
    {
        cout << "Case #" + to_string(i + 1) + ": " + to_string(output[i]) << endl;
    }

}

