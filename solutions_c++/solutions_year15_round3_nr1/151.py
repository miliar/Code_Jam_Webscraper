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

int n, m, k, tab[100007];

int main()
{
    testy()
    {
        scanf("%d %d %d", &n, &m, &k);

        /*if(k == 1)
        {
            printf("%d\n", n*m);
            continue;
        }*/

        printf("Case #%d: %d\n", _test, (m/k)*n + k - (m%k == 0 ? 1 : 0));
        continue;


        FOR(i, 1, k+1)
            tab[i] = i;
        FOR(i, k+2, 2*k)
            tab[i] = k+1;
        FOR(i, 2*k+1, m)
        {
            tab[i] = INF; //max(k+1, )

            FOR(j, k+1, i-k)
                tab[i] = min(tab[i], n+max(tab[j-1], tab[i-j]));
        }

        FOR(i, 1, m)
            cout << "tab[" << i << "] = " << tab[i] << endl;

        printf("%d\n", tab[m]);
    }

    return 0;
}
