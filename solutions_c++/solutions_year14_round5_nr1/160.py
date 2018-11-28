#include <string>
#include <cstring>
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

int N, p,q,r,s;
int tab[1000000];
LL suma;
LL res;

inline void rozw(LL a, LL b, LL c) {
    res = max(res, a+b+c-max(a, max(b, c)));
}


int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d%d%d", &N, &p, &q, &r, &s);
        suma = 0;
        res = 0;
        REP(a, N)
            suma += tab[a] = ((a * (LL)p + q) % r + s);
        LL do_teraz = 0;
        LL lewa = 0;
        int p2 = 0;
        int p1 = 0;
        for (;;) {
            do_teraz += tab[p2];
            ++p2;
            for (;;) {
                rozw(lewa, do_teraz-lewa, suma-do_teraz);
                if (p1==p2-1) break;
                if (lewa+tab[p1]>do_teraz-lewa-tab[p1]) {
                    rozw(lewa+tab[p1], do_teraz-lewa-tab[p1], suma-do_teraz);
                    break;
                }
                lewa += tab[p1];
                ++p1;
            }
            if (p2==N) break;
        }
        printf("Case #%d: %.10f\n", (tt+1), res/(double)suma);
    }
}


