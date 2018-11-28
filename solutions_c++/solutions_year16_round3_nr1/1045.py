// 2016_1A_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

                      //------------------------------------------------------------------------------------------------------
static const uint64_t T_max = 50;
static const uint64_t Pi_max = 1000;
static const uint64_t N_max = 26;

void main()
{
    uint64_t T;
    uint64_t N;
    uint64_t Pi[N_max];
    uint64_t x, y;

    cin >> T;

    for (x = 0; x < T; ++x)
    {
        // Read parameter.
        memset(Pi, 0, sizeof(Pi));

        cin >> N;
        uint64_t Total = 0;
        for (uint64_t n = 0; n < N; ++n)
        {
            cin >> Pi[n];
            Total += Pi[n];
        }

        cout << "Case #" << x + 1 << ":";

        // Escape
        uint64_t Rest = Total;
        while (Rest > 0)
        {
            if (Rest == 2)
            {
                cout << " ";
                for (uint64_t n = 0; n < N; ++n)
                {
                    if (Pi[n] > 0)
                    {
                        cout << (char)(n + 'A');
                    }
                }
                Rest -= 2;
                break;
            }
            else if (Rest == 3)
            {
                for (uint64_t n = 0; n < N; ++n)
                {
                    if (Pi[n] > 0)
                    {
                        cout << " " << (char)(n + 'A');
                    }
                    Pi[n]--;
                    break;
                }
                Rest -= 1;
            }
            else
            {
                uint64_t MaxId = 0;
                for (uint64_t n = 0; n < N; ++n)
                {
                    if (Pi[n] > Pi[MaxId])
                    {
                        MaxId = n;
                    }
                }
                cout << " " << (char)(MaxId + 'A');
                Pi[MaxId]--;
                Rest -= 1;

                MaxId = 0;
                for (uint64_t n = 0; n < N; ++n)
                {
                    if (Pi[n] > Pi[MaxId])
                    {
                        MaxId = n;
                    }
                }
                cout << (char)(MaxId + 'A');
                Pi[MaxId]--;
                Rest -= 1;
            }
            
        }
        
        // Output.
        cout << endl;
    }
}

