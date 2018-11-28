#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
using namespace std;
int T,counter=0,N,ans;
int F[3000];
void dfs(int f[],int l,int cnt)
{
	int i,pos,maxn=0,nl=0;int tmp[5000];
	if(cnt>ans)
		return ;
	if(l==0)
	{
		ans=min(ans,cnt);
		return ;
	}
	for(i=1;i<=l;i++)
		if(f[i]>maxn)
		{ maxn=f[i];pos=i;}
	for(i=1;i<=l;i++)
		if(f[i]-1>0)
		{
			nl++;tmp[nl]=f[i]-1;
		}
	dfs(tmp,nl,cnt+1);
	nl=l;
	if(maxn!=1)
	{
		nl++;f[nl]=0;
		for(i=1;i<maxn;i++)
		{
			f[pos]-=i;f[nl]+=i;
			dfs(f,nl,cnt+1);
			f[pos]+=i;f[nl]-=i;
		}
	}
}
int main()
{
	freopen("xx.in","r",stdin);
	freopen("xx.out","w",stdout);
	int i;
	scanf("%d",&T);
	while(T--)
	{
		ans=0;
		counter++;scanf("%d",&N);
		for(i=1;i<=N;i++)
		{
			scanf("%d",&F[i]);
			ans=max(ans,F[i]);
		}
		dfs(F,N,0);
		printf("Case #%d: %d\n",counter,ans);
	}
	return 0;
}
