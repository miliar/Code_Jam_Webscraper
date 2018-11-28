#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <cassert>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;

#define SIZE(x) (int((x).size()))
#define rep(i,l,r) for (int i=(l); i<=(r); i++)
#define repd(i,r,l) for (int i=(r); i>=(l); i--)
#define rept(i,c) for (typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

#ifndef ONLINE_JUDGE
#define debug(x) { cerr<<#x<<" = "<<(x)<<endl; }
#else
#define debug(x) {}
#endif

double dp[210][210], p[210], chosen[210];

void lemon()
{
	int n,m; scanf("%d%d",&n,&m);
	rep(i,1,n) scanf("%lf",&p[i]);
	sort(p+1,p+n+1);
	rep(i,1,m/2) chosen[i]=p[i];
	rep(i,n-m/2+1,n) chosen[m/2+i-(n-m/2)]=p[i];
	
	double maxv=0; int maxss;
	rep(state,0,(1<<n)-1)
	{
		int all=0;
		rep(i,1,n)
			if (state&(1<<(i-1)))
			{
				all++; chosen[all]=p[i];
			}
		if (all!=m) continue;
		memset(dp,0,sizeof dp);
		dp[0][0]=1;
		rep(i,1,m)
			rep(j,0,i)
				if (j==0) 
					dp[i][j]=dp[i-1][j]*(1-chosen[i]);
				else	dp[i][j]=dp[i-1][j-1]*chosen[i]+dp[i-1][j]*(1-chosen[i]);
		
		if (dp[m][m/2]>maxv)
		{
			maxv=dp[m][m/2];
			maxss=state;
		}
	}
	printf("%.16lf\n",maxv);
	int all=0;
	rep(i,1,n)
		if (maxss&(1<<(i-1)))
		{
			all++; chosen[all]=p[i];
		}
	sort(chosen+1,chosen+all+1);
	//rep(i,1,m) printf("%.3lf ",chosen[i]); printf("\n");
}

int main()
{
	ios::sync_with_stdio(true);
	#ifndef ONLINE_JUDGE
		freopen("B.in","r",stdin);
	#endif
	int tcase; scanf("%d",&tcase);
	rep(nowcase,1,tcase)
	{
		printf("Case #%d: ",nowcase);
		lemon();
	}
	return 0;
}

