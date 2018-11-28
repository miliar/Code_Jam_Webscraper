// 2016_1A_C.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

                      //------------------------------------------------------------------------------------------------------
static const uint64_t T_max = 100;
static const uint64_t B_max = 50;

void main()
{
    uint64_t T;
    uint64_t B, M;
    uint64_t x;
    uint64_t Power2[61];
    cin >> T;

    for (x = 0; x < T; ++x)
    {
        cin >> B >> M;

        uint64_t i = 60;
        uint64_t tempM = M;
        while(true)
        {
            if (pow(2, i) <= tempM)
            {
                Power2[i] = pow(2, i);
            }
            else
            {
                Power2[i] = 0;
            }
            tempM -= Power2[i];
            if (i == 0)
            {
                break;
            }
            i--;
        }

        if (pow(2, B-2) < M)
        {
            cout << "Case #" << x + 1 << ": IMPOSSIBLE" << endl;
        }
        else if (pow(2, B - 2) == M)
        {
            cout << "Case #" << x + 1 << ": POSSIBLE" << endl;
            for (uint64_t row = 0; row < B - 1; row++)
            {
                for (uint64_t col = 0; col < B; col++)
                {
                    if (col > row)
                    {
                        cout << "1";
                    }
                    else
                    {
                        cout << "0";
                    }
                }
                cout << endl;
            }
            for (uint64_t col = 0; col < B; col++)
            {
                cout << "0";
            }
            cout << endl;
        }
        else
        {
            cout << "Case #" << x + 1 << ": POSSIBLE" << endl;
            uint64_t row = 0;
            for (uint64_t col = 0; col < B - 1; col++)
            {
                if (col > row)
                {
                    if (Power2[B - 2 - col] > 0)
                    {
                        cout << "1";
                    }
                    else
                    {
                        cout << "0";
                    }
                }
                else
                {
                    cout << "0";
                }
            }
            cout << "0";
            cout << endl;
            uint64_t Flag = 0;
            for (row++; row < B - 1; row++)
            {
                
                if ((Power2[B - 2 - row] > 0) || (Flag > 0))
                {
                    Flag = 1;
                    for (uint64_t col = 0; col < B; col++)
                    {
                        if (col > row)
                        {
                            cout << "1";
                        }
                        else
                        {
                            cout << "0";
                        }
                    }
                    
                }
                else
                {
                    for (uint64_t col = 0; col < B; col++)
                    {
                       cout << "0";
                    }
                }
                cout << endl;
            }
            for (uint64_t col = 0; col < B; col++)
            {
                cout << "0";
            }
            cout << endl;
        }

        i++;
    }
}

