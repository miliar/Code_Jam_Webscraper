#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
int n;
vector<int> ne;
vector<int> vis;
vector<int> b;
int ans;

void dfs(int v, int id=0)
{
	vis[v]=id;
	if(vis[ne[v]]==-1) {
		dfs(ne[v], id+1);
	} else if(vis[ne[v]]==id-1) {
		b[ne[v]]=max(b[ne[v]], id);
	} else {
		ans=max(ans, id-vis[ne[v]]+1);
	}
}

int main()
{
	scanf("%d", &t);
	for(int q=1; q<=t; q++) {
		scanf("%d", &n);
		ne.resize(n);
		vis.resize(n);
		b.resize(n);
		for(int i=0; i<n; i++) b[i]=0;
		ans=0;
		for(int i=0; i<n; i++) {
			int f;
			scanf("%d", &f);
			f--;
			ne[i]=f;
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) vis[j]=-1;
			dfs(i);
		}
		int s=0;
		for(int i=0; i<n; i++) s+=b[i];
		ans=max(ans, s);
		printf("Case #%d: %d\n", q, ans);
	}

	return 0;
}
