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
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int tab[1001][1001];

int xs, ys, B;

int xd[4] = {-1, 0, 1, 0};
int yd[4] = {0, 1, 0, -1};

void dfs(int x, int y, int d) {
    tab[x][y] = 1;
    if (y==ys-1)
        throw 0;
    REP(dm, 3) {
        int dn = (d+dm)%4;
        int xn = x+xd[dn];
        int yn = y+yd[dn];
        if (xn<0 || xn>=xs || yn<0 || yn>=ys || tab[xn][yn])
            continue;
        int dnn = (dn+3)%4;
        dfs(xn, yn, dnn);
    }
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d", &xs, &ys, &B);
        REP(x, xs)
            REP(y, ys)
                tab[x][y] = 0;
        REP(a, B) {
            int x0, y0, x1, y1;
            scanf("%d%d%d%d", &x0, &y0, &x1, &y1);
            FOR(x, x0, x1)
                FOR(y, y0, y1)
                    tab[x][y] = -5;
        }
        int wyn = 0;
        REP(x, xs)
            try {
                if (!tab[x][0])
                    dfs(x, 0, 0);
            } catch (...) {
                ++wyn;
            }
        printf("Case #%d: %d\n", (tt+1), wyn);
    }
}


