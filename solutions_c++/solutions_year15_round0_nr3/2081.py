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

int n, l, x;
char slowo[1000007];

struct elem
{
    char val;
    bool minus;
};
elem tab[1000007], pre[1000007], post[1000007];

elem pomnoz(elem a, elem b)
{
    elem e;
    e.minus = a.minus^b.minus;
    if(a.val * b.val == 0)
    {
        e.val = a.val + b.val;
    }
    else
    {
        if(a.val == b.val)
        {
            e.val = 0;
            e.minus ^= 1;
        }
        else
        {
            e.val = 6 - a.val - b.val;
            if((a.val - b.val + 3)%3 == 1)
                e.minus ^= 1;
        }
    }
    return e;
}

bool dzialaj()
{
    forr(i, l*x)
    {
        elem sr = tab[i+1];
        FOR(j, i+2, l*x-1)
        {
            if(pre[i].val == 1 && sr.val == 2 && post[j].val == 3 &&
               pre[i].minus == 0 && sr.minus == 0 && post[j].minus == 0)
                return 1;
            sr = pomnoz(sr, tab[j]);
        }
    }
    return 0;
}

int main()
{
    testy()
    {
        scanf("%d %d", &l, &x);
        x = min(x, 12 + x%4);

        scanf("%s", slowo);

        forr(i, l*x)
        {
            tab[i].minus = 0;
            tab[i].val = slowo[i%l]-'i' + 1;
        }

        pre[0] = tab[0];
        FOR(i, 1, x*l-1)
        {
            pre[i] = pomnoz(pre[i-1], tab[i]);
            //cout << "pre[" << i << "] = " << (int)(pre[i].val) << ", " << pre[i].minus << endl;
        }

        post[x*l-1] = tab[x*l-1];
        FORD(i, x*l-2, 0)
            post[i] = pomnoz(tab[i], post[i+1]);

        printf("Case #%d: %s\n", _test, dzialaj() ? "YES" : "NO");
    }

    return 0;
}
