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

int n, tab[10007];
list <char> res;

int main()
{
    testy()
    {
        scanf("%d", &n);
        forr(i, n)
            scanf("%d", &tab[i]);

        forr(j, 1005)
        {
            forr(i, n)
                if(tab[i] > 0)
                {
                    tab[i]--;
                    res.push_front(i+'A');
                }
        }

        printf("Case #%d:", _test);
        int ile = res.size();
        while(ile > 0)
        {
            if(ile&1)
            {
                printf(" %c", res.front());
                res.pop_front();
                ile--;
            }
            else
            {
                printf(" %c", res.front());
                res.pop_front();
                printf("%c", res.front());
                res.pop_front();
                ile -= 2;
            }
        }
        printf("\n");

        res.clear();
    }

    return 0;
}
