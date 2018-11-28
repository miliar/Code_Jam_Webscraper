#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
using namespace std;
typedef long long lld;
#define X first
#define Y second
#define mp make_pair
#define pb push_back
double dp[2][1010];
double dp1[1010];
double dp2[1010];
double s[1010];
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n;
		scanf("%d",&n);
		int now,pre;

		now=0;
		pre=1;
		for(int i=0;i<n;i++)
			dp[now][i]=i;
		for(int k=0;k<n;k++)
		{
			now^=1;
			pre^=1;
			for(int i=0;i<k;i++)
				dp[now][i]=dp[pre][i];
			double sum=0;
			for(int i=k;i<n;i++)
				sum+=dp[pre][i];
			int T=n-k;
			dp[now][k]=sum/T;
			for(int i=k+1;i<n;i++)
				dp[now][i]=dp[pre][i]*(T-1)/T+dp[pre][k]/T;
		}
		for(int i=0;i<n;i++)
			dp1[i]=dp[now][i];

		now=0;
		pre=1;
		for(int i=0;i<n;i++)
			dp[now][i]=i;
		for(int k=0;k<n;k++)
		{
			now^=1;
			pre^=1;
			double sum=0;
			for(int i=0;i<n;i++)
				sum+=dp[pre][i];
			int T=n;
			dp[now][k]=sum/T;
			for(int i=0;i<n;i++)
			{
				if(i == k)
					continue;
				dp[now][i]=dp[pre][i]*(T-1)/T+dp[pre][k]/T;
			}
		}
		for(int i=0;i<n;i++)
			dp2[i]=dp[now][i];

//		double r1=0;
//		double r2=0;
//		for(int i=0;i<n;i++)
//		{
//			r1+=i+1;
//			r2+=dp1[i];
//		}
//		printf("%.4f %.4f\n",r1,r2);

		for(int i=0;i<n;i++)
			scanf("%lf",&s[i]);
		double tmp1=0;
		for(int i=0;i<n;i++)
			tmp1+=(s[i]-dp1[i])*(s[i]-dp1[i]);
		double tmp2=0;
		for(int i=0;i<n;i++)
			tmp2+=(s[i]-dp2[i])*(s[i]-dp2[i]);
//		for(int i=0;i<n;i++)
//			printf("%.4f ",dp1[i]);
//		printf("\n");
//		for(int i=0;i<n;i++)
//			printf("%.4f ",dp2[i]);
//		printf("\n");
		if(tmp1 < tmp2)
			printf("Case #%d: GOOD\n",cc);
		else
			printf("Case #%d: BAD\n",cc);
	}
	return 0;
}
/*
2
3
0 1 2
3
2 0 1

 */
