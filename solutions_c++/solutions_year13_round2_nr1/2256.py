// =========================================================
//
//       Filename:  Osmos
//
//    Description:
//
//        Version:  1.0
//        Created:  05/04/2013
//       Revision:  none
//       Compiler:  gcc
//
//         Author:  Tao Lin, tlin005@gmail.com
//        Company:  U of California Riverside
//      Copyright:  Copyright (c) 05/04/2013
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

unsigned int test(long long int A, long long int mote)
{
    unsigned int n = 0;

    while (A <= mote)
    {
        if (A == 1)
            return 1000;
        ++n;
        A = A+A-1;
    }
    return n;
}

long long int solve(long long int A, long long int N, vector<long long int > motes)
{
    long long int result = 0;
    long long int mote = A;

    for (unsigned int i = 0; i < motes.size(); ++i)
    {
        // no action, just absorb it
        if (mote > motes[i])
        {
            mote = mote+motes[i];
            continue;
        }
        // 1 action of adding
        if (mote+(mote-1) > motes[i])
        {
            result++;
            mote = mote+mote-1+motes[i];
            continue;
        }
        // need more actions
        unsigned int foo = 0;
        foo = test(mote, motes[i]);
        if (foo < (motes.size()-i))  // add
        {
            result += foo;
            for (unsigned int j = 0; j < foo; ++j)
                mote = mote+mote-1;
            mote = mote + motes[i];
        }
        else  // delete
        {
            result += motes.size()-i;
            return result;
        }
    }

    return result;
}

int main()
{
    unsigned int case_no;

    // load input
    cin >> case_no;

    for (unsigned int case_count = 0; case_count < case_no; ++case_count)
    {
        long long int A;
        long long int N;
        vector< long long int > motes;

        // load input
        cin >> A >> N;
        motes.clear();

        for (unsigned int i = 0; i < N; ++i)
        {
            long long int mote;
            cin >> mote;
            motes.push_back(mote);
        }
        sort(motes.begin(), motes.end());

        // sove problem
        long long int result = 0;
        result = solve(A, N, motes);
        cout << "Case #" << case_count+1 << ": ";
        cout << result << endl;
    }

    return 0;

}
