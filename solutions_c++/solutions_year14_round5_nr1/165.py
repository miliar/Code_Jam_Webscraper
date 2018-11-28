#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <cassert>
#include <map>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define forsn(i,s,n) for(int i=(s);i<(int)(n);i++)
#define dforn(i,n) for(int i=(n)-1;i>=0;i--)

#define forall(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)

typedef long long tint;

const int MAXN = 10000000;

tint v[MAXN];

tint N,p,q,r,s;

bool anda(tint C)
{
    int i = 0;
    forn(k,3)
    {
        tint sum = 0;
        while (i < N && sum + v[i] <= C)
        {
            sum += v[i];
            i++;
        }
    }
    return i == N;
}

int main()
{
    int TT; scanf("%d", &TT);
    forn(tt,TT)
    {
        
        cin >> N >> p >> q >> r >> s;
        tint T = 0;
        forn(i,N) {v[i] = (tint(i) * p + q) % r + s; T += v[i];}
        tint a = -1, b = T;
        while (b - a > 1)
        {
            tint c = (a+b) / 2;
            if (anda(c))
                b = c;
            else
                a = c;
        }
        printf("Case #%d: %.15lf\n" , tt+1, double(T - b) / double(T));
    }
    return 0;
}
