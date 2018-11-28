#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>
using namespace std;
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define inf 0xfffffff
typedef long long lld;
#define pi acos(-1.0)
#define eps 1e-8
int myabs(int x)
{
	return max(x,-x);
}
int total[10]={0,1,6,15,28};
double dp[2][110][110];
int main()
{
//	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d: ",cc);
		int n,x,y;
		scanf("%d %d %d",&n,&x,&y);
		if(n == 1)
		{
			if(x == 0 && y == 0)
				printf("1.0\n");
			else
				printf("0.0\n");
			continue;
		}
		int t=myabs(x)+myabs(y);
		t/=2;
		t++;
		int dep,level;
		if(n <= 1)
			dep=0,level=1;
		else if(n <= 6)
			dep=2,level=2;
		else if(n <= 15)
			dep=4,level=3;
		else
			dep=6,level=4;
		if(t < level)
		{
			printf("1.0\n");
			continue;
		}
		if(t > level)
		{
			printf("0.0\n");
			continue;
		}
		if(n == 6)
		{
			printf("1.0\n");
			continue;
		}
		if(n == 15)
		{
			printf("1.0\n");
			continue;
		}
		n-=total[level-1];
		memset(dp,0,sizeof(dp));
		int now=0;
		int pre=1;
		dp[now][0][0]=1.0;
//		printf("%d %d\n",n,dep);
		for(int l=0;l<n;l++)
		{
			now^=1;
			pre^=1;
			memset(dp[now],0,sizeof(dp[now]));
			for(int i=0;i<=dep;i++)
				for(int j=0;j<=dep;j++)
				{
					if(dp[pre][i][j] == 0)
						continue;
					double add=dp[pre][i][j];
					if(i == dep)
						dp[now][i][j+1]+=add;
					else if(j == dep)
						dp[now][i+1][j]+=add;
					else
					{
						dp[now][i+1][j]+=add*0.5;
						dp[now][i][j+1]+=add*0.5;
					}
				}
		}
		double ans=0;
		for(int i=0;i<=dep;i++)
			for(int j=0;j<=dep;j++)
				if(dp[now][i][j] != 0)
				{
//					printf("--%d %d\n",i,j);
					int x1,x2;
					x1=-dep+i;
					x2=dep-j;
					if(x < x1)
						ans+=dp[now][i][j];
					if(x > x2)
						ans+=dp[now][i][j];
				}
		printf("%.9f\n",ans);
	}
	return 0;
}
/*
7
1 0 0
1 0 2
3 0 0
3 2 0
3 1 1
4 1 1
4 0 2

 */
