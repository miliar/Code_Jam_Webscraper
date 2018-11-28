#include<iostream>
#include<cstdio>
#include<queue>
#include<cstring>
#include<algorithm>
using namespace std;

void solve(int ca)
{
	int g1[4][4],g2[4][4];

	int n=4;
	int ans1,ans2;
	scanf("%d",&ans1);
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			scanf("%d",&g1[i][j]);
		}
	}
	scanf("%d",&ans2);
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			scanf("%d",&g2[i][j]);
		}
	}
	--ans1;--ans2;
	int cnt = 0;
	int nn ;
	for(int i=0;i<n;++i)
	{
		for(int j=0;j<n;++j)
		{
			if(g1[ans1][i] == g2[ans2][j])
			{
				nn = g1[ans1][i];
				++cnt;
			}
		}
	}
	printf("Case #%d: ",ca);
	if(cnt == 1)
	{
		printf("%d\n",nn);
	}else if(cnt ==0)
	{
		printf("Volunteer cheated!\n");
	}
	else
	{
		printf("Bad magician!\n");
	}
}
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
	{
		solve(i);
	}
	return 0;
}