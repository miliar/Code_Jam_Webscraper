#include <bits/stdc++.h>

using namespace std;

int n;
int val[1005];
int memo[1005][1005];
int pgkt2[15];

int dp(int ask, int bts)
{
	if(ask<=bts)return 0;
	if(memo[ask][bts]!=-1)return memo[ask][bts];
	
	return memo[ask][bts]=1+dp(ask-bts,bts);
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
		
	memset(memo,-1,sizeof memo);
	
	int teskes;
	scanf("%d",&teskes);
	for(int tc=1;tc<=teskes;tc++)
	{
		scanf("%d",&n);
		for(int x=0;x<n;x++)
		{
			scanf("%d",&val[x]);
		}
		
		int ans=1000000;
		
		for(int x=1000;x>=1;x--)
		{
			int total=0;
			for(int y=0;y<n;y++)
			{
				total+=dp(val[y],x);
			}
			total+=x;
			ans=min(ans,total);
		}
		printf("Case #%d: %d\n",tc,ans);
	}
	return 0;
}
