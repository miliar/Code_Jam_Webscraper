#include<cstdio>
#include<string>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;
#define rep(i,n) for (int i=0;i<n;++i)
typedef long long LL;
const int N=1005;
int T,Case,ans,res,n,m,a[N],c[N][28];
string s[N];
void dfs(int t)
{
	if (t==m){
		rep(i,n){
			int flag=1;
			rep(j,m) if (a[j]==i) flag=0;
			if (flag) return;
		}
		int z=n; memset(c,0,sizeof(c));
		rep(i,m){
			int x=a[i]+1;
			rep(j,s[i].size()){
				int y=s[i][j]-65;
				if (!c[x][y]) c[x][y]=++z;
				x=c[x][y];
			}
		}
		if (z>ans) ans=z,res=1;
		else if (z==ans) ++res;
		return;
	}
	rep(i,n) a[t]=i,dfs(t+1);
}
int main()
{
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		scanf("%d%d",&m,&n),ans=0,res=0; rep(i,m) cin>>s[i]; dfs(0);
		printf("Case #%d: %d %d\n",++Case,ans,res);
	}
	return 0;
}

