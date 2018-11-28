#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#define LL long long
#define MAXN 2222
using namespace std;
int fa[MAXN];
int getfa(int x) {
	if (x == fa[x])
		return x;
	else
		return fa[x] = getfa(fa[x]);
}
vector<int> e[1111];
bool bo[1111][1111];
int f[1111];
int r[11111], len[11111];
int tail;
int maxn;

int ans = 0;
void dfs(int cur, int fa, int dep) {
	dep++;
	if (dep > maxn)
		maxn = dep;
	for (int j = 0; j < e[cur].size(); ++j) {
		int u = e[cur][j];
		if (u == fa)
			continue;
		dfs(u, cur, dep);
	}
}
int dis[1111];
void gao(int cur,int fa,int dep){
	dis[cur]=dep;
	for(int i=0;i<e[cur].size();++i){
		int u=e[cur][i];
		if(dis[u]==-1){
			gao(u,cur,dep+1);
		}else
		{
			ans=max(ans,dis[cur]-dis[u]+1);
		}
	}
}
int mx[1111];
int main() {
	freopen("C-large (1).in","r",stdin);
	freopen("output5.out","w",stdout);
	int tt, ri = 0;
	int n;
	scanf("%d", &tt);
	while (tt--) {
		scanf("%d", &n);
		memset(dis,-1,sizeof(dis));
		for (int i = 0; i <= n; ++i)
			e[i].clear();
		for (int i = 1; i <= n; ++i) {
			scanf("%d", &f[i]);
			if (i != f[i]) {
				e[f[i]].push_back(i);
//				printf("**%d %d\n",f[i],i);
			}
		}
		tail = 0;
		ans = 0;
		for(int i=1;i<=n;++i){
			if(dis[i]==-1)
				gao(i,-1,0);
			for(int i=0;i<=n;++i)
				dis[i]=-1;
//			printf("%d %d\n",i,ans);
		}
//		for(int i=1;i<=n;++i)
//			printf("---%d %d\n",i,dis[i]);
//		printf("%d\n",ans);
		for (int i = 1; i <= n; ++i) {
			if (f[i] != i && f[f[i]] != i)
				continue;
			r[tail] = i;
			len[tail++] = 1;
			if (f[i] == i) {
				r[tail] = i;
				len[tail++] = 1;
			}
			for (int j = 0; j < e[i].size(); ++j) {
				int u = e[i][j];
				maxn = 0;
				if (u == f[i])
					continue;
				dfs(u, i, 1);

				r[tail] = i;
				len[tail++] = maxn;
				if (f[i] == i)
					ans = max(ans, maxn);
//				printf("%d %d %d\n",u,i,ans);
			}
		}
//		printf("%d\n",ans);
//		for(int i=0;i<tail;++i)
//			printf("%d %d %d\n",i,r[i],len[i]);
		int sum=0;
		memset(mx,0,sizeof(mx));
		for(int i=0;i<tail;++i){
			mx[r[i]]=max(mx[r[i]],len[i]);
		}
		for(int i=1;i<=n;++i){
			if(f[i]==i)
				sum+=mx[i];
			for(int j=i+1;j<=n;++j){
				if(f[i]==j&&f[j]==i){
					sum+=mx[i]+mx[j];
				}
			}
		}
		ans=max(ans,sum);
		for (int i = 0; i < tail; ++i) {
			for (int j = i + 1; j < tail; ++j) {
				if (r[i] == r[j]) {
					if (f[r[i]] == r[i]) {
						ans = max(ans, len[i] + len[j] - 1);
					}
				}
			}
		}
		printf("Case #%d: %d\n", ++ri, ans);



	}
	return 0;
}
