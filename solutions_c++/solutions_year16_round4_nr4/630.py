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

int n, tab[10][10];
char slowo[10][10];
int ile;

bool poprawne(int nr)
{
    ile = 0;
    forr(i, n*n)
        if(slowo[i%n][i/n] == '1')
        {
            if(((nr>>i)&1) == 0)
                return 0;
        }
        else
        {
            if(((nr>>i)&1) == 1)
                ile++;
        }
    return 1;
}

bool dziala(int nr)
{
    forr(i, n*n)
    {
        tab[i%n][i/n] = ((nr>>i)&1);
    }

//    forr(i, n)
//    {
//        forr(j, n)
//            cout << tab[i][j];
//        cout << endl;
//    }

    forr(i, n)
    {
        int ile = 0;
        forr(j, n)
            ile += tab[i][j];
        if(ile == 0)
        {
//            cout << "pusty wiersz" << endl;
            return 0;
        }
    }

    forr(i, n)
        forr(j, n)
        {
            int ile1=0, ile2=0;
            forr(l, n)
            {
                ile1 += tab[i][l];
                ile2 += tab[l][j];
            }
            if(tab[i][j] == 1 && ile1 != ile2)
            {
//                cout << "nierowno w " << i << " " << j << endl;
                return 0;
            }
            forr(i1, n)
                forr(j1, n)
                    if(tab[i][j] == 1 && tab[i1][j] == 1 && tab[i][j1] == 1)
                        if(tab[i1][j1] == 0)
                        {
//                            cout << "zla konf w " << i << " " << j << " i " << i1 << " " << j1 << endl;
                            return 0;
                        }
        }
//    cout << "dziala" << endl;
    return 1;
}

int main()
{
    testy()
    {
        scanf("%d", &n);
        forr(i, n)
            scanf("%s", slowo[i]);
        int res = INF;
        FORD(i, (1<<(n*n))-1, 0)
        {
            if(poprawne(i))
            {
//                cout << "poprawne " << i << endl;
                if(dziala(i))
                    res = min(res, ile);
            }
        }
        printf("Case #%d: %d\n", _test, res);
    }

    return 0;
}
