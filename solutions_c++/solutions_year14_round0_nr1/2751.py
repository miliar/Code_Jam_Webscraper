/*
 * MagickTrick.cpp
 * Copyright (C) 2014 mikhail <mikhail@mikhail-UL50VT>
 *
 * Distributed under terms of the MIT license.
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char *argv[])
{
    ifstream ifs(argv[1]);
    int countTestCases;
    ifs >> countTestCases;
    for (int i = 0; i < countTestCases; ++i)
    {
        int line1;
        ifs >> line1;
        int cards1[4][4];
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                ifs >> cards1[j][k];
            }
        }

        int line2;
        ifs >> line2;
        int cards2[4][4];
        for (int j = 0; j < 4; j++) {
            for (int k = 0; k < 4; k++) {
                ifs >> cards2[j][k];
            }
        }

        int card = -1;
        bool res = true;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                if (cards1[line1 - 1][j] == cards2[line2 - 1][k])
                {
                    if (card == -1)
                        card = cards1[line1 - 1][j];
                    else
                    {
                        cout << "Case #" << i + 1 << ": Bad magician!" << endl;
                        res = false;
                        break;
                    }
                }
            }
            if (!res)
                break;
        }
        if (!res)
            continue;

        if (card == -1)
        {
            cout << "Case #" << i + 1 << ": Volunteer cheated!" << endl;
        }
        else
        {
            cout << "Case #" << i + 1 << ": " << card << endl;
        }
    }

    return 0;
}
