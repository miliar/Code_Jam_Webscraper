// Artur Kraska, II UWr

#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <cmath>
#include <queue>
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

int n, res, a;
int tab[10007];
priority_queue <int> pq;

int main()
{
    testy()
    {
        scanf("%d", &n);

        int maks = 0;
        int res = INF;
        CLEAR(tab);

        forr(i, n)
        {
            scanf("%d", &tab[i]);
            maks = max(maks, tab[i]);
        }

        FOR(j, 1, maks)
        {
            int w = 0;
            forr(i, n)
            {
                w += (((tab[i]+j-1)/j)-1);
            }
            res = min(res, w+j);
        }

        printf("Case #%d: %d\n", _test, res);

    /*
        while(!pq.empty())
            pq.pop();


        scanf("%d", &n);
        forr(i, n)
        {
            scanf("%d", &a);
            pq.push(a);
        }

        res = pq.top();
        int ile = 0;
        while(pq.top() > 3)
        {
            ile++;
            a = pq.top();
            pq.pop();
            pq.push(a/2);
            pq.push((a+1)/2);


            cout << " ile: " << ile << endl;
            cout << " < " << a << endl;
            cout << " > " << a/2 << endl;
            cout << " > " << (a+1)/2 << endl;

            res = min(res, pq.top() + ile);
        }

        printf("Case #%d: %d\n", _test, res); */
    }

    return 0;
}
