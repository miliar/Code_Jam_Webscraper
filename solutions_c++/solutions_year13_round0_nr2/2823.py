#include <bits/stdc++.h>
#define fr(a,b,c) for(int a = b; a < c; a++)
#define rp(a,b) fr(a,0,b)
using namespace std;

int di[] = {0,1};
int dj[] = {1,0};
int n, m;
int g[111][111];
int dfs(int i, int j, int k) {
	if (i >= n || j >= m) return 1;
	if (g[i][j] == 2) return 0;
	return dfs(i+di[k], j+dj[k], k);
}

int main() {
	int cas = 1;
	int T; scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &m);
		rp(i,n) rp(j,m) scanf("%d", &g[i][j]);
		rp(i,n) if (g[i][0] != 2 && dfs(i,0,0)) {
			//printf("%d %d\n", i, 0);
			rp(j,m) g[i][j] = 3;
		}
		rp(j,m) if (g[0][j] != 2 && dfs(0,j,1)) {
			//printf("%d %d\n", 0, j);
			rp(i,n) g[i][j] = 3;
		}
		bool pode = 1;
		rp(i,n) rp(j,m) if (g[i][j] == 1) {
			pode = 0;
			break;
		}
		if (pode) printf("Case #%d: YES\n", cas++);
		else printf("Case #%d: NO\n", cas++);
	}
	return 0;
}