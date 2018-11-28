// =========================================================
//
//       Filename:  Lawnmower
//
//    Description:
//
//        Version:  1.0
//        Created:  04/12/2013
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 04/12/2013
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

const int MAX_SIZE = 100;

unsigned long long int solve(unsigned int N, unsigned int K, vector< unsigned long long int >::iterator a)
{
    unsigned long long int result = 0l;

    return result;
}

int main()
{
    unsigned int case_no;

    // load input
    cin >> case_no;

    for (unsigned int t = 0; t < case_no; ++t)
    {
        unsigned int N;
        unsigned int M;

        unsigned int lawn[MAX_SIZE][MAX_SIZE];
        unsigned int max_x[MAX_SIZE];
        unsigned int max_y[MAX_SIZE];

        // load input
        cin >> N >> M;

        for (unsigned i = 0; i < N; ++i)
            max_x[i] = 0;
        for (unsigned j = 0; j < M; ++j)
            max_y[j] = 0;

        for (unsigned i = 0; i < N; ++i)
            for (unsigned j = 0; j < M; ++j)
            {
                cin >> lawn[i][j];
                if (lawn[i][j] > max_x[i])
                    max_x[i] = lawn[i][j];
                if (lawn[i][j] > max_y[j])
                    max_y[j] = lawn[i][j];
            }

        // sove problem
        bool possible = true;
        for (unsigned i = 0; i < N; ++i)
        {
            for (unsigned j = 0; j < M; ++j)
            {
                if ((lawn[i][j] < max_x[i]) && (lawn[i][j] < max_y[j]))
                {
                    cout << "Case #" << t+1 << ": NO" << endl;
                    possible = false;
                    break;
                }
            }
            if (not possible)
                break;
        }

        if (possible)
            cout << "Case #" << t+1 << ": YES" << endl;
    }

    return 0;

}
