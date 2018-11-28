#include <bits/stdc++.h>

using namespace std;

int dp[101][100000];

int main()
{
	int v1,v2;
	scanf("%d%d",&v1,&v2);
	int t,d;
	scanf("%d%d",&t,&d);

	dp[1][v1]=v1;

	for(int i=1;i<=t;i++)
	{
		for(int j=0;j<=500;j++)
		{
			for(int k=max(0,j-d);k<=min(500,j+d);k++)
			{
				if(dp[i][j]!=0)
				{
					dp[i+1][k]=max(dp[i+1][k],dp[i][j]+k);
				}
			}
		}
	}

	printf("%d\n",dp[t][v2]);
return 0;}