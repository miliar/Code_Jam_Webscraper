#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstring>

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

#define maxn 1010
#define INF 1000000000

int sum[maxn], c[maxn], maxv[maxn], minv[maxn], w[maxn], low[maxn], high[maxn];

void lemon()
{
	int n,m; scanf("%d%d",&n,&m);
	//x1 ~ xm
	rep(i,m,n) scanf("%d",&sum[i]);
	//x_i-x_{i-m}=sum_i-sum_{i-1}
	//x_i=x_{i-m}+sum_i-sum_{i-1}
	rep(i,1,m) c[i]=0;
	rep(i,m+1,n)
		c[i]=c[i-m]+sum[i]-sum[i-1];
	
	rep(i,1,m) maxv[i]=-INF, minv[i]=INF;
	rep(i,1,m)
	{
		int j=i;
		while (j<=n)
		{
			maxv[i]=max(maxv[i],c[j]);
			minv[i]=min(minv[i],c[j]);
			j+=m;
		}
	}
	int target=sum[m];
	//minimize ans 
	//such that (x_i+maxv_i)-(x_j+minv_j)<=ans
	//and x_1+..+x_m=target
	//let y_i=x_i+maxv_i
	//then y_1+..+y_m=target+maxv_1+..+maxv_m
	//y_i-(y_j-maxv_j+minv_j)<=ans
	//y_i-y_j+maxv_j-minv_j)<=ans
	//let w_j=maxv_j-minv_j
	//for any j,
	//y_i<=y_j-w_j+ans for all i
	LL final=1000000000000000;
	rep(i,1,m) w[i]=maxv[i]-minv[i];
	rep(i,1,m) target+=maxv[i];
	rep(k,1,m)
	{
		//suppose k is the one such that y_k-w_j is minimum
		//then y_k-w_k+w_i<=y_i<=y_k-w_k+ans for all i
		rep(i,1,m) low[i]=-w[k]+w[i], high[i]=-w[k];
		//now limit becomes
		//m*y_k+sum(z)=target where low[i]<=z[i]<=high[i]+ans
		//y_k,z[i] integer, minimize ans
		int rm=target%m;
		//want sum(z)%m=rm
		LL ans=-1000000000000000;
		rep(i,1,m) ans=max(ans,LL(low[i]-high[i]));
		//sum(low)<=sum(z)<=sum(high)+ans*m
		LL slow=0, shigh=0;
		rep(i,1,m) slow+=low[i], shigh+=high[i];
		
		int rlow=slow%m, rhigh=shigh%m;
		int flag=0;
		if (rlow<=rhigh && rlow<=rm && rm<=rhigh) flag=1;
		if (rlow>rhigh && (rm>=rlow || rm<=rhigh)) flag=1;
		
		if (flag)
		{
			//find min ans s.t. slow<=shigh+ans*m
			LL want=slow-shigh;
			if (want%m==0) ans=max(ans,want/m); else ans=max(ans,want/m+1);
		}
		else
		{
			//need to plus an extra 1
			LL want=slow-shigh;
			if (want%m==0) ans=max(ans,want/m+1); else ans=max(ans,want/m+2);
		}
		final=min(final,ans);
	}
	cout<<final<<endl;
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

