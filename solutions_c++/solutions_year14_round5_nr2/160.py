#include <string>
#include <cstring>
#include <cassert>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define FORD(a,b,c) for(int a=(b); a>=(c); --a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int N, Pmoje, Pwiezy;
int wynik[2][2000];
int k = 0;
int zycie[100], punkty[100];

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d", &Pmoje, &Pwiezy, &N);
        REP(a, N)
            scanf("%d%d", zycie+a, punkty+a);
        REP(p, 2000)
            wynik[k][p] = -INF;
        wynik[k][1] = 0;
        REP(a, N) {
            k = !k;
            REP(p, 2000)
                wynik[k][p] = -INF;
            REP(p, 2000)
                if (wynik[!k][p]>=0) {
                    int r = (zycie[a]+Pwiezy-1)/Pwiezy;
                    assert(p+r<2000);
                    wynik[k][p+r] = max(wynik[k][p+r], wynik[!k][p]);
                    int z = zycie[a]-Pwiezy*(r-1);
                    int ja = (z+Pmoje-1)/Pmoje;
                    int np = p+r-1-ja;
                    assert(np<2000);
                    if (np>=0)
                        wynik[k][np] = max(wynik[k][np], wynik[!k][p]+punkty[a]);
                }
        }
        int res = 0;
        REP(p, 2000)
            res = max(res, wynik[k][p]);
        printf("Case #%d: %d\n", (tt+1), res);
    }
}


