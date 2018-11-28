// 2016_1A_B.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

                      //------------------------------------------------------------------------------------------------------
static const uint64_t T_max = 50;
static const uint64_t N_max = 50;
static const uint64_t H_max = 3000;
void main()
{
    uint64_t T;
    uint64_t N;
    uint64_t x;
    uint64_t y[N_max];
    uint64_t hMask[H_max];

    cin >> T;

    for (x = 0; x < T; ++x)
    {
        // Read parameter.
        memset(y, 0, sizeof(y));
        memset(hMask, 0, sizeof(hMask));
        cin >> N;
        for (uint64_t i = 0; i < N * ((2 * N)-1); ++i)
        {
            uint64_t h;
            cin >> h;
            if (hMask[h] == 0)
            {
                hMask[h] = 1;
            }
            else
            {
                hMask[h] = 0;
            }
       
        }

        cout << "Case #" << x + 1 << ": ";
        for (uint64_t h = 0; h < H_max; ++h)
        {
            if(hMask[h] > 0)
            {
                cout << h << " ";
            }
            
        }
        cout << endl;
    }
}

