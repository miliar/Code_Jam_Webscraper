// 2016_1A_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

//------------------------------------------------------------------------------------------------------
static const uint64_t T_max = 100;
static const uint64_t L_max = 1000;

void main()
{
    uint64_t T, L;
    string TempStr;
    char OrgChars[L_max];
    char NewChars[L_max*2+1];

    // Read case number.
    cin >> T;
    // Skip first line.
    getline(cin, TempStr);

    
    for (uint64_t t = 0; t < T; ++t)
    {
        getline(cin, TempStr);
        L = TempStr.length();
        for (uint64_t l = 0; l < L; ++l)
        {
            OrgChars[l] = TempStr[l];
        }

        // Algorithm
        uint64_t HeadIndex = L_max;
        uint64_t TailIndex = L_max;
        NewChars[L_max] = OrgChars[0];
        for (uint64_t l = 1; l < L; ++l)
        {
            if (OrgChars[l] >= NewChars[HeadIndex])
            {
                HeadIndex--;
                NewChars[HeadIndex] = OrgChars[l];
            }
            else
            {
                TailIndex++;
                NewChars[TailIndex] = OrgChars[l];
            }
        }
        // Output.
        cout << "Case #" << t + 1 << ": ";
        for (uint64_t l = 0; l < L; ++l)
        {
            cout << NewChars[HeadIndex];
            HeadIndex++;
        }
        cout << endl;

    }
}

