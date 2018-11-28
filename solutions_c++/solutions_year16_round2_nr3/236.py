#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int q;
int n;
int cntl, cntr;
map<string,int> ml, mr;
vector<int> next[12345];
int mat[12345];
int vis[12345];

int dfs(int v, int f=-1, int l=0)
{
	vis[v]=f;
	if(l==0) {
		for(int i=0; i<next[v].size(); i++) {
			int s=next[v][i];
			if(mat[s]==-1) {
				mat[v]=s;
				mat[s]=v;
				while(vis[v]!=-1) {
					v=vis[v];
					mat[v]=vis[v];
					mat[vis[v]]=v;
					v=vis[v];
				}
				return 1;
			} else {
				int ret;
				if(!vis[s]) {
					ret=dfs(s, v, 1);
					if(ret) return 1;
				}
			}
		}
	} else {
		if(!vis[mat[v]]) {
			dfs(mat[v], v, 0);
		}
	}
}

int main()
{
	scanf("%d\n", &q);
	for(int x=1; x<=q; x++) {
		scanf("%d\n", &n);
		cntl=cntr=0;
		ml.clear();
		mr.clear();
		for(int i=0; i<2*n; i++) {
			next[i].clear();
			mat[i]=-1;
		}
		for(int i=0; i<n; i++) {
			char s1[12345], s2[12345];
			scanf("%s %s\n", s1, s2);
			int n1=strlen(s1), n2=strlen(s2);
			if(ml.find(string(s1))==ml.end()) ml[string(s1)]=cntl++;
			if(mr.find(string(s2))==mr.end()) mr[string(s2)]=n+cntr++;
			next[ml[string(s1)]].push_back(mr[string(s2)]);
			next[mr[string(s2)]].push_back(ml[string(s1)]);
		}
		int prev=0;
		while(1) {
			int cur=0;
			for(int i=0; i<cntl; i++) {
				if(mat[i]==-1) {
					for(int j=0; j<2*n; j++) vis[j]=0;
					dfs(i);
				}
			}
			for(int i=0; i<cntr; i++) {
				if(mat[n+i]==-1) {
					for(int j=0; j<2*n; j++) vis[j]=0;
					dfs(n+i);
				}
			}
			for(int i=0; i<cntl; i++) cur+=(mat[i]!=-1);
			if(cur==prev) break;
			prev=cur;
		}
		int ans=0;
		for(int i=0; i<cntl; i++) ans+=(mat[i]!=-1);
		printf("Case #%d: %d\n", x, n-ans-(cntl+cntr-2*ans));
	}

	return 0;
}
