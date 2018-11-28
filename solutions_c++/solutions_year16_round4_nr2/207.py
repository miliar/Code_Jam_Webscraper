#include<bits/stdc++.h>
using namespace std;

#define sd(a) scanf("%d",&a)
#define ss(a) scanf("%s",&a)
#define sl(a) scanf("%lld",&a)
#define clr(a) memset(a,0,sizeof(a))
#define debug(a) printf("check%d\n",a)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define ll long long

double dp[210][210];
double p[210];
int main()
{
	// freopen("B1.in","r",stdin);
	// freopen("B1.out","w",stdout);
	int t,i,j,k,n,x,l;
	sd(t);
	for(int tt=1;tt<=t;tt++)
	{
		sd(n);sd(k);
		for(i=0;i<n;++i)
			scanf("%lf",&p[i]);
		sort(p,p+n);
		double maxx=-1.0;
		for(l=0;l<=k;++l)
		{
			vector<int> v(0);
			v.PB(0);
			for(i=0;i<l;++i)
				v.PB(i);
			for(i=l+n-k;i<n;++i)
				v.PB(i);
			for(i=0;i<=k;++i)
				for(j=0;j<=k;++j)
					dp[i][j]=0;
			dp[0][0]=1;
			for(i=1;i<=k;++i)
				for(j=0;j<=k;++j)
					dp[i][j]=dp[i-1][j-1]*p[v[i]]+dp[i-1][j]*(1-p[v[i]]);
			maxx=max(maxx,dp[k][k/2]);
		}
		printf("Case #%d: %.9lf\n",tt,maxx);
	}
}