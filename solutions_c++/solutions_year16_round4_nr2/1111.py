#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
int n,k;
double p[20];
int vis[20],vss[20];
double  ans,tmp;
void dfs2(int level,int last,int dst){
	if (level==dst){
		double tt=1.0;
		for (int i=1;i<=dst*2;i++) if (vss[i]==1) tt*=p[vis[i]]; else tt*=(1-p[vis[i]]);
		tmp+=tt;
		return;
	}
	for (int i=last+1;i<=dst*2-(dst-level)+1;i++){
		vss[i]=1;
		dfs2(level+1,i,dst);
		vss[i]=0;
	}
}
void dfs(int level,int last,int dst){
	if (level==dst){
		// printf("1\n");
		// for (int i=1;i<=level;i++)
		// 	printf("%d ",vis[i] );
		// printf("\n");
		tmp=0;
		memset(vss,0,sizeof(vss));
		dfs2(0,0,dst/2);
		ans=max(ans,tmp);
		return;
	}
	for (int i=last+1;i<=n-(dst-level)+1;i++){
		vis[level+1]=i;
		dfs(level+1,i,dst);
	}
}
int main(int argc, char const *argv[])
{
	int t;
	scanf("%d",&t);
	for (int TT=1;TT<=t;TT++){
		ans=0;
		scanf("%d%d",&n,&k);
		for (int i=1;i<=n;i++) scanf("%lf",&p[i]);
		memset(vis,0,sizeof(vis));
		dfs(0,0,k);
		printf("Case #%d: %.10f\n",TT,ans );
	}
	return 0;
}