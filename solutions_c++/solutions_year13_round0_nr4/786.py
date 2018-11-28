#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
using namespace std;
const int maxn=22;
int dp[1<<maxn];
int cur[maxn*2],tp[maxn];
vector<int> have[maxn];
int up,n,tx;
int cal(int a)
{
	if(dp[a]!=-1)
		return dp[a];
	int res=a;
	int lef=res^up;
	if(lef==0)
		return dp[a]=1;
	int i,j;
	for(i=0;i<n;i++)
	{
		if(lef&(1<<i))
		{
			if(cur[tp[i]])
			{
				cur[tp[i]]--;
				for(j=0;j<have[i].size();j++)
					cur[have[i][j]]++;
				int s=cal(a|(1<<i));
				cur[tp[i]]++;
			    	for(j=0;j<have[i].size();j++)
					cur[have[i][j]]--;	 
				if(s==1)
					return dp[a]=1;
			}
		}
	}
	return dp[a]=0;

}
void out(int a)
{
	if(a==up)
	{
		printf("\n");
		return;
	}
	int lef=a^up;
	int i;
	for(i=0;i<n;i++)
	{
		if(cur[tp[i]]&&(lef&(1<<i))&&dp[a|(1<<i)])
		{
				cur[tp[i]]--;
				 for(int j=0;j<have[i].size();j++)
					cur[have[i][j]]++;
				printf(" %d",i+1);
				out(a|(1<<i));
				return;
		}
	}
}
int main()
{
	freopen("G:\\dd.in","r",stdin);
	freopen("G:\\output.txt","w",stdout);
	int cas;
	int cc=0;
	scanf("%d",&cas);
	while(cas--)
	{
		memset(cur,0,sizeof(cur));
		int i,j,k;
		scanf("%d%d",&tx,&n);
		up=(1<<n)-1;
		for(i=0;i<tx;i++)
		{
			scanf("%d",&k);
			k--;
			cur[k]++;
		}
		for(i=0;i<=up;i++)
			dp[i]=-1;
		for(i=0;i<n;i++)
			have[i].clear();
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&j,&k);
			j--;
			tp[i]=j;
			while(k--)
			{
				int f;
				scanf("%d",&f);
				f--;
				have[i].push_back(f);
			}
		}
		k=cal(0);
		printf("Case #%d:",++cc);
		if(k==0)
		{
			puts(" IMPOSSIBLE");
			continue;

		}
		else
		{
			out(0);
		}
	}
	return 0;
}