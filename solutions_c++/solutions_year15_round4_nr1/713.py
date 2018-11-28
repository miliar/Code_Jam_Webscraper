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

int n, m;
char slowo[1007][1007];

int main()
{
    testy()
    {
        scanf("%d %d", &n, &m);
        forr(i, n)
        {
            scanf("%s", slowo[i]);
        }
        int res = 0;

        bool impossible = 0;
        forr(i, n)
        {
            forr(j, m)
            {
                int ile = 0;
                if(slowo[i][j] == '.')
                    continue;
                forr(k, n)
                    if(slowo[k][j] != '.')
                        ile++;
                forr(k, m)
                    if(slowo[i][k] != '.')
                        ile++;
                if(ile == 2)
                    impossible = 1;
   //             cout << ile << endl;
            }
        }

        if(impossible)
        {
            printf("Case #%d: IMPOSSIBLE\n", _test);
            continue;
        }

        forr(i, n)
        {
            forr(j, m)
            {
                if(slowo[i][j] != '.')
                {
                    if(slowo[i][j] == '<')
                        res++;
                    break;
                }
            }
            FORD(j, m-1, 0)
            {
                if(slowo[i][j] != '.')
                {
                    if(slowo[i][j] == '>')
                        res++;
                    break;
                }
            }
        }

        forr(j, m)
        {
            forr(i, n)
            {
                if(slowo[i][j] != '.')
                {
                    if(slowo[i][j] == '^')
                        res++;
                    break;
                }
            }
            FORD(i, n-1, 0)
            {
                if(slowo[i][j] != '.')
                {
                    if(slowo[i][j] == 'v')
                        res++;
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", _test, res);
    }

    return 0;
}
