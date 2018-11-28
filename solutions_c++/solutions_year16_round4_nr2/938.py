#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<string>
#define N 42
using namespace std;
double p[N],dp[N][N],v[N];
int test,n,m;
double dfs(int dep,int now)
{
	if (dep>n)
	{
		if (now==m)
		{
			memset(dp,0,sizeof(dp));
			dp[0][m]=1;
			for (int i=1;i<=n;i++)
			if (v[i]) 
			for (int j=0;j<=2*m;j++)
			{
				double temp=0;
				if (j) temp+=dp[i-1][j-1]*p[i];
				if (j<2*m) temp+=dp[i-1][j+1]*(1-p[i]);
				dp[i][j]=temp;
//				cout<<i<<' '<<j<<' '<<dp[i][j]<<endl;
			}
			else
			for (int j=0;j<=2*m;j++) dp[i][j]=dp[i-1][j];
			return dp[n][m];
		}
		return 0;
	}
	double temp=0;
	v[dep]=1;
	temp=dfs(dep+1,now+1);
	v[dep]=0;
	temp=max(temp,dfs(dep+1,now));
	return temp;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("21.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n>>m;
		for (int i=1;i<=n;i++)
		scanf("%lf",&p[i]);
		printf("%.6lf\n",dfs(1,0));
	}
	return 0;
}
