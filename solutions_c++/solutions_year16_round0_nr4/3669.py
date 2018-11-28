//
//  main.cpp
//  GoogleCodeJamQual3
//
//  Created by Charles Ringer on 09/04/2016.
//  Copyright © 2016 Charles Ringer. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <math.h>
#include <assert.h>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream input ("D-small-attempt3.in");
    ofstream inputD;
    inputD.open ("in.txt");
    ofstream output;
    output.open ("results.txt");
    vector<vector<long>> tests;
    int curr = 1;
    
    if (input.is_open())
    {
        int count;
        long k;
        long c;
       long s;
        input >> count;
        while (input >> k >> c >>s)
        {
            vector<long> newTest;
            newTest.push_back(k);
            newTest.push_back(c);
            newTest.push_back(s);
            inputD << "Test " << curr << ":" << k << " " << c << " "<< s << " "<< endl;
            tests.push_back(newTest);
            curr++;
        }
    } else {
        cout << "FILE FAILED TO LOAD" << endl;
    }
    cout << "Starting" << endl;
    
    int currentTestCase = 0;
    while(currentTestCase < tests.size())
    {
        vector<long> currentTest = tests[currentTestCase];
        long k = currentTest[0];
        long c = currentTest[1];
        long s = currentTest[2];
        
        vector<long> studentIndexes;
        long totalLength = pow(k, c);
        long moveLength = totalLength/k;
        long currentS = 1;
        
        while(currentS <= totalLength)
        {
            studentIndexes.push_back(currentS);
            if (studentIndexes.size() >= s) break;
            currentS = currentS+moveLength;
        }
        assert(studentIndexes.size() == s);
        output << "Case #" << currentTestCase+1 << ": ";
        if (s >= k)
        {
            for(long ind : studentIndexes)
            {
                output << ind << " ";
            }
        } else {
          output << "IMPOSSIBLE";
        }
        output << endl;
        currentTestCase++;
    }
    return 0;
}
