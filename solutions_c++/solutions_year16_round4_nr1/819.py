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

int n, r, p, s;
string res;
char znak[3] = {'p', 'r', 's'};
char bije[128];
int ile[128];
vector <char> g[20];
vector <string> v[20];

bool generuj(char x)
{
    g[0].clear();
    g[0].PB(x);
    forr(i, n)
    {
        g[i+1].clear();
        FOREACH(it, g[i])
        {
            g[i+1].PB(*it);
            g[i+1].PB(bije[*it]);
        }
    }
    CLEAR(ile);
    FOREACH(it, g[n])
    {
//        cout << *it;
        ile[*it]++;
    }
//    cout << endl;
    return ile['r'] == r && ile['p'] == p && ile['s'] == s;
}

void sortuj()
{
    v[0].clear();
    FOREACH(it, g[n])
    {
        v[0].PB( string(1, (*it)-'a'+'A'));
        //cout << string(1, *it) << endl;
    }
    forr(i, n)
    {
        v[i+1].clear();
        int dl = v[i].size();
        for(int j=0; j<dl; j+=2)
        {
            if(v[i][j] < v[i][j+1])
                v[i+1].PB(v[i][j] + v[i][j+1]);
            else
                v[i+1].PB(v[i][j+1] + v[i][j]);
        }
    }
    res = v[n][0];
}

int main()
{
    bije['r'] = 's';
    bije['s'] = 'p';
    bije['p'] = 'r';
    testy()
    {
        scanf("%d %d %d %d", &n, &r, &p, &s);
        if(generuj('r'))
        {
            sortuj();
            cout << "Case #" << _test << ": " << res << endl;
        } else if(generuj('p'))
        {
            sortuj();
            cout << "Case #" << _test << ": " << res << endl;
        } else if(generuj('s'))
        {
            sortuj();
            cout << "Case #" << _test << ": " << res << endl;
        } else
        {
            cout << "Case #" << _test << ": IMPOSSIBLE" << endl;
        }
    }

    return 0;
}
