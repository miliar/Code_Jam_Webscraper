#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int done[10],vis[10];
int A[10][10],p[10];
char s[10][10];
int n,t,T,ans;

bool judge(int u) {
	if (u > n) return true;
	bool flag = false;
	for (int i = 1; i <= n; i++) {
		if (vis[i] || (A[p[u]][i] == 0)) continue;
		flag = true;
		vis[i] = 1;
		if (!judge(u + 1)) {
			vis[i] = 0;
			return false;
		}
		vis[i] = 0;
	}
	return flag;
}

bool dfs_(int u) {
	if (u > n) {
		if (!judge(1)) return false;
		return true;
	}
	for (int i = 1; i <= n; i++) {
		if (done[i]) continue;
		done[i] = 1;
		p[u] = i;
		if (!dfs_(u + 1)) { done[i] = 0; return false; }
		done[i] = 0;
	}
	return true;
}

void solve(int u) {
	if (dfs_(1)) ans = min(ans,u);
}

void dfs(int x,int y,int u) {
	if (y > n) y = 1, x++;
	if (x == n + 1) { solve(u); return; }
	if (A[x][y] == 0) {
		dfs(x, y + 1, u);
		A[x][y] = 1;
		dfs(x, y + 1, u + 1);
		A[x][y] = 0;
	}
	else dfs(x, y + 1, u);
}

int main() {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

	for (scanf("%d",&T), t = 1; t <= T; t++) {
		scanf("%d",&n);
		printf("Case #%d: ",t);
		for (int i = 1; i <= n; i++) scanf("%s",s[i] + 1);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				A[i][j] = (s[i][j] == '1');
			}
		ans = n * n;
		dfs(1,1,0);
		printf("%d\n",ans);
	}
	
	return 0;
}
