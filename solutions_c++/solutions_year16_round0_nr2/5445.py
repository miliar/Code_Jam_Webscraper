//
//  main.cpp
//  GoogleCodeJamQual2
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
    ifstream input ("B-large.in");
    ofstream output;
    output.open ("results.txt");
    vector<string> tests;

    if (input.is_open())
    {
        string newS = "";
        while (input >> newS)
        {
            
            tests.push_back(newS);
        }
    } else {
        cout << "FILE FAILED TO LOAD" << endl;
    }
    cout << "Starting" << endl;
    
    int currentTestCase = 1;
    while(currentTestCase < tests.size())
    {
        string currentStack = tests[currentTestCase];
        int flips = 0;
        
        for(long i = currentStack.length()-1; i >=0 ; i--)
        {
            if (currentStack[i] == '-')
            {
                bool hasflipped = false;
                for(int frontFlip = 0;  frontFlip < i; frontFlip++)
                {
                    
                    if(currentStack[frontFlip] == '+')
                    {
                        hasflipped = true;
                        currentStack[frontFlip] = '-';
                    } else {
                        break;
                    }
                }
                if (hasflipped)
                {
                    flips++;
                }
                string flipped = "";
                for(int j = 0; j <= i; j++)
                {
                    if (currentStack[j] == '+')
                    {
                        flipped =  '-' + flipped;
                    } else {
                        flipped =  '+' + flipped;
                    }
                }
                string unflipped = "";
                    
                for(long k = i+1; k < currentStack.length(); k++)
                {
                    unflipped += currentStack[k];
                }
                currentStack = flipped + unflipped;
                    
                flips++;
                //cout << currentStack << endl;
            }
        }
        output << "Case #" << currentTestCase << ": " << flips << endl;
        currentTestCase++;
    }
    cout << "Ending" << endl;
    return 0;
}

//string flip(string in, int stop)
//{
//    string flipped = "";
//    
//    for(int i = 0; i < stop; i++)
//    {
//        flipped += in[i];
//    }
//    for(long j = in.length()-1; j >= stop; j--)
//    {
//        if (in[j] == '+')
//        {
//            flipped = flipped + '-';
//        } else {
//            flipped = flipped + '+';
//        }
//    }
//    return flipped;
//}
