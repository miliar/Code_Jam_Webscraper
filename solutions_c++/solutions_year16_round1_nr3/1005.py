#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
using namespace std;
const int maxn = 1000 + 10;
int f[maxn];
vector <int> Q[maxn];

int ans, n;
int degree[maxn], vis[maxn];

void dfs(int u, int cnt){
	int t = Q[u].size(), flag = 0;
	for(int i = 0; i < t; i++){
		int v = Q[u][i];
		if(vis[v]) continue;
		flag = 1;
		vis[v] = 1;
		dfs(v, cnt+1);
		vis[v] = 0;
	}
	if(flag) ans = max(ans, cnt);
	return;
}

int main(){
	int T, kase = 0;
	freopen("Cin.txt", "r", stdin);
	//freopen("Cout.txt", "a", stdout);
	scanf("%d", &T);
	while(T--){
		for(int i = 0; i < maxn; i++){
			Q[i].clear();
		}
		ans = 0;
		memset(degree, 0, sizeof(degree));
		memset(vis, 0, sizeof(vis));
		scanf("%d", &n);
		for(int i = 1; i <= n; i++){
			scanf("%d", &f[i]);
			degree[f[i]]++;
			Q[i].push_back(f[i]);
		}
		for(int i = 1; i <= n; i++){
			vis[i] = 1;
			dfs(i, 1);
			vis[i] = 0;
		}
		printf("Case #%d: ", ++kase);
		printf("%d\n", ans);
	}
}
