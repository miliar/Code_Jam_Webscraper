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

using namespace std;

int n, k;
double p[1007];
vector <double> v;

int zlicz(int x)
{
    int r = 0;
    while(x > 0)
    {
        r += (x&1);
        x >>= 1;
    }

    return r;
}

void ustaw(int x)
{
    v.clear();
    forr(i, n)
        if(((x>>i)&1) == 1)
            v.PB(p[i]);
}

long double sprawdzaj()
{
    long double rr = 0, r;
    forr(i, (1<<k))
    {
        if(zlicz(i)*2 == k)
        {
            r = 1;
            forr(j, k)
            {
                if(((i>>j)&1) == 1)
                    r *= v[j];
                else
                    r *= 1-v[j];
            }
            rr += r;
        }
    }
    return rr;
}

int main()
{
    testy()
    {
        scanf("%d %d", &n, &k);
        forr(i, n)
            scanf("%lf", &p[i]);
        long double res = 0;
        forr(i, (1<<n))
            if(zlicz(i) == k)
            {
                ustaw(i);
                res = max(res, sprawdzaj());
            }
        printf("Case #%d: %.10lf\n", _test, (double)res);
    }

    return 0;
}
