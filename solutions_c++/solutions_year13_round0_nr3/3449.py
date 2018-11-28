//
//  main.cpp
//  GoogleCodeJam2013_FairandSquare
//
//  Created by Surasak Sermluxananon on 4/13/56 BE.
//  Copyright (c) 2556 Surasak Sermluxananon. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <math.h>
using namespace std;

bool isPalindrome(unsigned long int value)
{
    unsigned long int reversed = 0, n = value;
    while (n > 0)
    {
        reversed = reversed * 10 + n % 10;
        n /= 10;
    }
    
    return value == reversed;
}

bool isSquare(long int value)
{
    double dValue = sqrt(value);
    int iValue = dValue;
    double dFraction = dValue - iValue;
    return (dFraction == 0.0f && isPalindrome(iValue));
}

int main(int argc, const char * argv[])
{
    string input_line;
    ifstream input_file;
    ofstream output_file;
    
    input_file.open (argv[1]);
    output_file.open(argv[2]);
    if (input_file.is_open())
    {
        int iCase = 0, iTotalCase = 0, iCount = 0;
        while (input_file.good())
        {
            getline (input_file, input_line);
            if(iTotalCase == 0)
            {
                iTotalCase = atoi(input_line.c_str());
                iCase = iTotalCase;
            }
            else if(input_line != "")
            {
                long int lMin = 0, lMax = 0;
                stringstream sInput(input_line);
                sInput >> lMin >> lMax;
                for(long int i = lMin; i <= lMax;++i)
                {
                    if(isPalindrome(i) && isSquare(i))
                    {
                        ++iCount;
                    }
                }
                --iCase;
                cout << "Case #" << iTotalCase - iCase << ": " << iCount << endl;
                output_file << "Case #" << iTotalCase - iCase << ": " << iCount << endl;
                iCount = 0;
            }
        }
    }
    
    input_file.close();
    output_file.close();
    return 0;
}
