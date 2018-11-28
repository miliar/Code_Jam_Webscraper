#include<bits/stdc++.h>
using namespace std;
vector<double> a;
#define PB push_back
const int maxn=201;
double p[maxn],dp[maxn][maxn];
int main()
{
	int T,n,k;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;++i)
			scanf("%lf",&p[i]);
		sort(p,p+n);
		double res=0;
		for(int i=0;i<=k;++i)
		{
			a.clear();
			//cout <<i<<" "<<n+i-k<<endl;
			for(int j=0;j<n;++j)
				if(j<i||j>=n-k+i)a.PB(p[j]);
			//for(int j=0;j<a.size();++j)cout <<a[j]<<" ";cout <<endl;
			memset(dp,0,sizeof(dp));
			dp[0][0]=1;
			for(int j=0;j<a.size();++j)
				for(int k=0;k<=a.size();++k)
				{
					dp[j+1][k+1]+=dp[j][k]*a[j];
					dp[j+1][k]+=dp[j][k]*(1-a[j]);
				}
			//printf("%.7f\n",dp[k][k/2]);
			res=max(res,dp[k][k/2]);
		}
		printf("Case #%d: %.7f\n",cas,res);
	}
	return 0;
}
