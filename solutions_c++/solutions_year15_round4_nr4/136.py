// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <list>
#include <set>
#include <map>

#define forr(i, n)                  for(int i=0; i<n; i++)
#define FOREACH(iter, coll)         for(typeof(coll.begin()) iter = coll.begin(); iter != coll.end(); ++iter)
#define FOREACHR(iter, coll)        for(typeof(coll.rbegin()) iter = coll.rbegin(); iter != coll.rend(); ++iter)
#define lbound(P,R,PRED)            ({typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})
#define testy()                     int _tests; scanf("%d", &_tests); FOR(_test, 1, _tests)
#define CLEAR(tab)                  memset(tab, 0, sizeof(tab))
#define CONTAIN(el, coll)           (coll.find(el) != coll.end())
#define FOR(i, a, b)                for(int i=a; i<=b; i++)
#define FORD(i, a, b)               for(int i=a; i>=b; i--)
#define MP                          make_pair
#define PB                          push_back
#define deb(X)                      X;

#define M 1000000007
#define INF 1000000007

long long M24 =  M * (long long)24;


using namespace std;

int n, m;
long long tab[1007][17][32], ile[10][10][32];

long long wyn(int n, int d, int r)
{
    if(n >= 0)
        return tab[n][d][r];
    return 0;
}

int nwd(int a, int b)
{
    if(b == 0)
        return a;
    return nwd(b, a%b);
}

int nww(int a, int b)
{
    return a*b/nwd(a, b);
}

int main()
{
    testy()
    {
        scanf("%d %d", &n, &m);

        CLEAR(tab);
        CLEAR(ile);
        tab[0][0][1] = tab[0][1][1] = 1;

        ile[0][2][1]++;
        ile[1][1][1]++;
        if(m%3 == 0)
            ile[1][2][3]+=3;
        if(m%6 == 0)
            ile[1][2][6]+=6;
        if(m%4 == 0)
            ile[1][3][4]+=4;

        FOR(i, 1, n)
        {
            FOR(maks, 1, 6)
            {
                FOR(maks2, 1, 6)
                {
                    FOR(d, 1, 5)
                        tab[i][0][max(maks, maks2)] += wyn(i-d, 1, maks)*ile[0][d][maks2];
                    FOR(d, 1, 5)
                        tab[i][1][max(maks, maks2)] += wyn(i-d, 0, maks)*ile[1][d][maks2];
                }

                //cout << i << " - " << tab[i][0] << ", " << tab[i][1] << endl;

            }

            FOR(maks, 1, 6)
            {
                tab[i][0][maks] %= M24;
                tab[i][1][maks] %= M24;
            }
        }

        long long res = 0;

        FOR(maks, 1, 6)
        {
            res += tab[n][0][maks]/maks;
            res += tab[n][1][maks]/maks;
        }

        printf("Case #%d: %d\n", _test, (int)(res%M));
    }

    return 0;
}
