// =========================================================
//
//       Filename:  Fair and Square
//
//    Description:
//
//        Version:  1.0
//        Created:  04/13/2013
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/13/2013
//
// =========================================================

#include <iostream>
#include <string.h>
#include <math.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

signed int solve(unsigned int row_1, unsigned int grid_1[4][4], unsigned int row_2, unsigned int grid_2[4][4])
{
    unsigned int n = 0;
    unsigned int card = 0;

    for (unsigned int i = 0; i < 4; ++i)
    {
        for (unsigned int j = 0; j < 4; ++j)
        {
            //cout << grid_1[row_1][i] << "\t" << grid_2[row_2][j] << endl;
            if (grid_1[row_1][i] == grid_2[row_2][j])
            {
                card = grid_1[row_1][i];
                n++;
            }
        }
    }

    if (n > 1) return -1;  // bad
    if (n == 0) return 0;  // cheat
    return card;
}

int main()
{
    // load input
    unsigned int case_no;
    cin >> case_no;

    for (unsigned int t = 0; t < case_no; ++t)
    {
        unsigned int row_1, row_2;
        unsigned int grid_1[4][4], grid_2[4][4];

        cin >> row_1;
        row_1--;
        for (unsigned int i = 0; i < 4; ++i)
            for (unsigned int j = 0; j < 4; ++j)
                cin >> grid_1[i][j];

        cin >> row_2;
        row_2--;
        for (unsigned int i = 0; i < 4; ++i)
            for (unsigned int j = 0; j < 4; ++j)
                cin >> grid_2[i][j];

        // sove problem
        signed int result;
        result = solve(row_1, grid_1, row_2, grid_2);

        cout << "Case #" << t+1 << ": ";
        if (result == 0)
        {
            cout << "Volunteer cheated!" << endl;
        }
        else if (result == -1)
        {
            cout << "Bad magician!" << endl;
        }
        else
            cout << result << endl;
    }

    return 0;

}
