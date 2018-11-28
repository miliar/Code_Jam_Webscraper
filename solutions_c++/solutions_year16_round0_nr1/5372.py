//
//  main.cpp
//  GoogleCodeJamQual1
//
//  Created by Charles Ringer on 09/04/2016.
//  Copyright © 2016 Charles Ringer. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream input ("A-large.in");
    ofstream output;
    output.open ("results.txt");
    vector<int> tests;
    if (input.is_open())
    {
        int newI = -1;
        while (input >> newI)
        {
            tests.push_back(newI);
        }
    } else {
        cout << "FILE FAILED TO LOAD" << endl;
    }
    cout << "Starting" << endl;
    int currentTestCase = 1;
    while(currentTestCase < tests.size())
    {
        int base = tests[currentTestCase];
        vector<int> seenNumbers;
        int testCaseCount = 0;
        
        while(seenNumbers.size() <10)
        {
            testCaseCount++;
            int currentTest = base*testCaseCount;
            if (currentTest == 0)
            {
                break;
            }
            int intToBreakUp = currentTest;
            while (intToBreakUp > 0)
            {
                int nextNum = intToBreakUp%10;
                bool canAdd = true;
                for( int currentSeen : seenNumbers)
                {
                    if (currentSeen == nextNum)
                    {
                        canAdd = false;
                        break;
                    }
                }
                if (canAdd) seenNumbers.push_back(nextNum);
                intToBreakUp = intToBreakUp/10;
            }
        }
        if (base == 0)
        {
         output << "Case #" << currentTestCase << ": INSOMNIA" << endl;
        } else {
        output << "Case #" << currentTestCase << ": " << base*testCaseCount << endl;
        }
        currentTestCase++;
    }
    cout << "Ending" << endl;
    return 0;
}


