// CodeJam1.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;

typedef unsigned long long ULL;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

int T;
ULL n;
ULL occ;

void solve(int kase)
{
    if (n == 0)
    {
        cout << "Case #" << kase << ": " << "INSOMNIA" << endl;
        return;
    }
    for (ULL i = n; ; i += n)
    {
        ULL t = i;
        while (t)
        {
            occ &= ~(1ULL << (t % 10));
            t /= 10;
        }
        if (!occ)
        {
            cout << "Case #" << kase << ": " << i << endl;
            return;
        }
    }
}

int main()
{
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cin >> n;
        occ = ~(~0ULL << 10);
        solve(i);
    }
    return 0;
}

