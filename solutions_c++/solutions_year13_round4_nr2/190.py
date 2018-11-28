#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)

#define forall(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();it++)

typedef long long tint;

tint N, P;

int superLog(tint n)
{
    if (n == 1) return 0;
    return 1 + superLog(n/2);
}

int maxLoses(tint n)
{
    return superLog(n+1);
}

int maxWins(tint n)
{
    return superLog((1LL << N) - n);
}

tint worsePos(tint n)
{
    int ml = maxLoses(n);
    return ((1LL << ml) - 1) * (1LL << (N - ml));
}

tint bestPos(tint n)
{
    int mw = maxWins(n);
    return (1LL << (N - mw)) - 1;
}

int main()
{
    int TT; cin >> TT;
    forn(tt,TT)
    {
        cin >> N >> P;
        tint Y = 0; // Y es el mas grande tal que worsePos(Y) < P
        tint Yb = (1LL<<N);
        while (Yb - Y > 1LL)
        {
            tint c = (Y + Yb) / 2;
            if (worsePos(c) < P)
                Y = c;
            else
                Yb = c;
        }
        tint Z = 0; // Z es el mas grande tal que bestPos(Z) < P
        tint Zb = (1LL<<N);
        while (Zb - Z > 1LL)
        {
            tint c = (Z + Zb) / 2;
            if (bestPos(c) < P)
                Z = c;
            else
                Zb = c;
        }
        cout << "Case #" << tt+1 << ": " << Y << " " << Z << endl;
        cerr << "Case #" << tt+1 << ": " << Y << " " << Z << endl;
    }
    return 0;
}

