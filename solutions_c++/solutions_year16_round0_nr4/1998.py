// CodeJam4.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("D-large.in");
ofstream fout("D-large.out");
#define cin fin
#define cout fout

typedef long long LL;

int main()
{
    int T, K, C, S;
    cin >> T;
    for (int kase = 1; kase <= T; ++kase)
    {
        cin >> K >> C >> S;
        S -= (K - 1) / C + 1;
        if (S < 0)
        {
            cout << "Case #" << kase << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << kase << ":";
        bool out_end = false;
        int idx = 0;
        while (!out_end)
        {
            LL factor = 1;
            LL ans = 0;
            for (int i = 0; i < C; ++i)
            {
                ans += factor * idx;
                factor *= K;
                idx += 1;
                if (idx == K)
                {
                    idx -= 1;
                    out_end = true;
                }
            }
            cout << ' ' << ans + 1;
        }
        cout << endl;
    }
    return 0;
}

