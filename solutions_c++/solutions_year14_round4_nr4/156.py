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

#define DEBUG

using namespace std;

char str[11][11];
int len[11];

int s[4][8];
int sn[4];
int n, m;
int ans, method;
void dfs(int u, int cur) {
    if (u >= n) {
        REP(i, m) if (!sn[i]) return;
        if (cur > ans) {
            ans = cur;
            method = 1;
        } else if (cur == ans) method ++;
        return;
    }
    REP(i, m) {
        int res = 0;
        REP(j, sn[i]) {
            int tmp = 0;
            REP(c, min(len[u], len[s[i][j]])) {
                if (str[s[i][j]][c] == str[u][c]) tmp = c + 1;
                else break;
            }
            res = max(res, tmp);
        }
        s[i][sn[i]++] = u;
        //printf("\n%d %s %d", res, str[u], i);

        dfs(u+1, cur + len[u] - res);

        sn[i]--;
    }
}

void solve() {
    ans = method = 0;
    scanf("%d%d", &n, &m);
    REP(i, n) {
        scanf("%s", str[i]);
        len[i] = strlen(str[i]);
    }
    dfs(0, 0);
    printf("%d %d", ans + m, method);
}

typedef long long LL;
int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d",&T);
    FOR(i, T) {
        printf("Case #%d: ", i);
        solve();
        printf("\n");
    }
	return 0;
}
