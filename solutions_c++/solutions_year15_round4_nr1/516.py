#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

using namespace std;

int T;
int n, m;

char g[111][111];
int ci[111], cj[111];
int u[111][111], d[111][111], l[111][111], r[111][111];
int s[111][111][4];

int solve() {
    scanf("%d%d\n", &n, &m);
    FOR(i, n)
        scanf("%s", g[i] + 1);
    CC(ci, 0);
    CC(cj, 0);
    CC(u, 0);CC(d, 0);CC(l, 0);CC(r, 0);
    CC(s, 0);
    int ans = 0;
    FOR(i, n) {
        FOR(j, m) {
            if (g[i][j] == '^' || g[i][j] == '>' || g[i][j] == 'v' || g[i][j] == '<') {
                ci[i]++;
                cj[j]++;
            }
        }
    }
    FOR(i, n) FOR(j, m) if(g[i][j] != '.') {l[i][j] = true;break;}
    FOR(i, n) FORD(j, m) if(g[i][j] != '.') {r[i][j] = true;break;}
    FOR(j, m) FOR(i, n) if(g[i][j] != '.') {u[i][j] = true;break;}
    FOR(j, m) FORD(i, n) if(g[i][j] != '.') {d[i][j] = true;break;}
    FOR(i, n) FOR(j, m) if(g[i][j] != '.') {
        if (ci[i] == 1) s[i][j][2] = true, s[i][j][3] = true;
        if (cj[j] == 1) s[i][j][0] = true, s[i][j][1] = true;
        if (u[i][j]) s[i][j][0] = true;
        if (d[i][j]) s[i][j][1] = true;
        if (l[i][j]) s[i][j][2] = true;
        if (r[i][j]) s[i][j][3] = true;

        if (g[i][j] == '^' && !s[i][j][0]) continue;
        if (g[i][j] == 'v' && !s[i][j][1]) continue;
        if (g[i][j] == '<' && !s[i][j][2]) continue;
        if (g[i][j] == '>' && !s[i][j][3]) continue;

        int o = 0;
        for (o = 0; o < 4; o++) {
            if (!s[i][j][o]) {ans += 1;break;}
        }
        if (o == 4) {
            return -1;
        }
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for (int i=1; i<=T; i++) {
        int t = solve();
        printf("Case #%d: ", i);
        if (t == -1) {
            printf("IMPOSSIBLE");
        } else {
            printf("%d", t);
        }
        printf("\n");
    }
    return 0;
}
