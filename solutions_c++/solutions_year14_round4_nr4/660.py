#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<ctime>
#include<cmath>
#define int64 long long
using namespace std;
int ans,fans,i,be[1200],n,m,num[1200],T,tim;
string a[1200],b[1200];
int lcp(string a,string b){
	int la=a.length(),lb=b.length(),i;
	for(i=0;i<la && i<lb;++i)if(a[i]!=b[i])break;
	return i;
}
void dfs(int dep){
	if(dep==n+1){
		for(int i=1;i<=m;++i)if(!num[i])return;
		int res=0;
		for(int i=1;i<=m;++i){
			int tot=0;
			for(int j=1;j<=n;++j)if(be[j]==i)b[++tot]=a[j];
			sort(b+1,b+tot+1);
			res++;
			for(int j=1;j<=tot;++j)res+=b[j].length();
			for(int j=1;j<tot;++j)res-=lcp(b[j],b[j+1]);
		}
		if(res>ans)ans=res,fans=1;
		else if(res==ans)fans++;
		return;
	}
	for(int i=1;i<=m;++i){
		be[dep]=i;
		num[i]++;
		dfs(dep+1);
		num[i]--;
	}
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);
	for(scanf("%d",&T);T--;){
		scanf("%d%d",&n,&m);
		for(i=1;i<=n;++i)cin>>a[i];
		ans=-1;
		dfs(1);
		printf("Case #%d: %d %d\n",++tim,ans,fans);
	}
}
