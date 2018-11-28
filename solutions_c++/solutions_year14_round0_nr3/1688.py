#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;

typedef double dbl;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<dbl,dbl> pdd;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<dbl> vd;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<pii> vp;

#define eps 1e-9
#define inf 1000000000
#define infll 1000000000000000000LL
#define infdbl 1e15
#define sqr(x) ((x)*(x))
#define pb push_back
#define mp make_pair
#define px first
#define py second
#define sz(x) ((int)(x).size())
#define intclz(x) __builtin_clz(x)
#define intctz(x) __builtin_ctz(x)
#define intln(x) (32-intclz(x))
#define intbc(x) __builtin_popcount(x)
#define llclz(x) __builtin_clzll(x)
#define llctz(x) __builtin_ctzll(x)
#define llln(x) (64-llclz(x))
#define llbc(x) __builtin_popcountll(x)
#define atbit(x,i) (((x)>>(i))&1)
#define tof(x) __typeof(x)
#define FORab(i,a,b) for (int i=(a); i<=(b); ++i)
#define RFORab(i,a,b) for (int i=(a); i>=(b); --i)
#define FOR1(i,n) FORab(i,1,(n))
#define RFOR1(i,n) RFORab(i,(n),1)
#define FOR(i,n) FORab(i,0,(n)-1)
#define RFOR(i,n) RFORab(i,(n)-1,0)
#define allstl(i,x,t) for (t::iterator i = (x).begin(); i!=(x).end(); ++i)
#define rallstl(i,x,t) for (t::reverse_iterator i = (x).rbegin(); i!=(x).rend(); ++i)
#define begend(x) (x).begin(),(x).end()
#define rbegend(x) (x).rbegin(),(x).rend()
#define ms(a,v) memset(a,v,sizeof(a))
#define msn(a,v,n) memset(a,v,n*sizeof(a[0]))
#define mcp(d,s,n) memcpy(d,s,n*sizeof(s[0]))
#define clamp(x,a,b) min(max(x,a),b)

void reveal(vvi& g, int r, int c, int x, int y) {
    bool prop = (g[x][y] == 0);
    g[x][y] = -2;
    if (prop) FORab(u,-1,1) FORab(v,-1,1) if (x+u >= 0 and x+u < r and y+v >= 0 and y+v < c and g[x+u][y+v] >= 0) reveal(g, r, c, x+u, y+v);
}

bool check(int bm, int r, int c, pii& ans) {
    vvi g(r, vi(c, 0));
    FOR(i,r) FOR(j,c) {
        if ( bm & (1<<(i*c+j)) ) g[i][j] = -1;
    }
    FOR(i,r) FOR(j,c) if (g[i][j] == 0) {
        FORab(u,-1,1) FORab(v,-1,1) if (i+u >= 0 and i+u < r and j+v >= 0 and j+v < c and g[i+u][j+v] == -1) {
            ++g[i][j];
        }
    }
    /*cout<<r<<" "<<c<<" "<<bm<<endl;
    cout<<"--------------"<<endl;
    FOR(i,r) {
        FOR(j,c) cout<<g[i][j]<<" ";
        cout<<endl;
    }
    cout<<"=============="<<endl;*/
    vvi og(g);
    FOR(i,r) FOR(j,c) if (g[i][j] != -1) {
        reveal(g, r, c, i, j);
        bool ok = true;
        FOR(u,r) FOR(v,c) {
            if (g[u][v] != -1 and g[u][v] != -2) ok = false;
        }
        FOR(u,r) FOR(v,c) g[u][v] = og[u][v];
        if (ok) {
            ans = pii(i,j);
            return true;
        }
    }
    return false;
}

bool D[6][6][26];
int G[6][6][26];
pii C[6][6][26];

void show(int r, int c, int t) {
    int bm = G[r][c][t];
    vvi g(r, vi(c, 0));
    FOR(i,r) FOR(j,c) {
        if (bm&(1<<(i*c+j))) {
            g[i][j] = 1;
        }
    }
    pii x = C[r][c][t];
    g[x.px][x.py] = -1;
    FOR(i,r) {
        FOR(j,c) {
            if (g[i][j] == 1) printf("*");
            else if (g[i][j] == 0) printf(".");
            else if (g[i][j] == -1) printf("c");
        }
        printf("\n");
    }
}

int main() {
    //freopen("in.txt", "rt", stdin);
    freopen("C-small-attempt1.in", "rt", stdin);
    freopen("C-small.out.txt", "wt", stdout);

    ms(D, false);
    FOR1(r,5) FOR1(c,5) {
        int t = r*c;
        FOR(bm,(1<<t)) {
            if (D[r][c][intbc(bm)]) continue;
            pii q;
            bool z = check(bm, r, c, q);
            if (z) {
                D[r][c][intbc(bm)] = true;
                G[r][c][intbc(bm)] = bm;
                C[r][c][intbc(bm)] = q;
            }
        }
    }

    int T;
    scanf("%d", &T);

    FOR1(cas,T) {
        printf("Case #%d:\n", cas);

        int r, c, m;
        scanf("%d%d%d", &r, &c, &m);

        if (D[r][c][m]) {
            show(r, c, m);
        } else {
            printf("Impossible\n");
        }
    }

    return 0;
}
