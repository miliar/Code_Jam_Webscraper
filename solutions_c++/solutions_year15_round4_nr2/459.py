#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
#include<cstring>
#include<cstdlib>
#include<utility>
#include<iostream>
#include<algorithm>
#include<functional>
#define REP(x,y,z) for(int x=y;x<=z;x++)
#define FORD(x,y,z) for(int x=y;x>=z;x--)
#define MSET(x,y) memset(x,y,sizeof(x))
#define FOR(x,y) for(__typeof(y.begin()) x=y.begin();x!=y.end();x++)
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define SZ size()
#define M 105
using namespace std;
typedef long long LL;
int t,n;
double v,temp,r[M],c[M];
int main()
{
	scanf("%d",&t);
	REP(tt,1,t)
	{
		scanf("%d",&n);
		scanf("%lf %lf",&v,&temp);
		REP(i,1,n) scanf("%lf %lf",&r[i],&c[i]);

		if(n==2 && c[1]==c[2])
		{
			r[1] += r[2];
			n--;
		}

		printf("Case #%d: ",tt);
		if(n==1)
		{
			if(c[1] != temp) puts("IMPOSSIBLE");
			else printf("%.10f\n", v/r[1]);
		}
		else
		{
			double ans = v*temp - c[2]*v;
			ans /= (r[1]*c[1] - c[2]*r[1]);
			double t2 = (v-r[1]*ans)/r[2];

			if(c[1]<temp && c[2]<temp) puts("IMPOSSIBLE");
			else if(c[1]>temp && c[2]>temp) puts("IMPOSSIBLE");
			else if(ans>=-(1e-9) && t2>=-(1e-9)) printf("%.10f\n", max(ans,t2));
			else puts("IMPOSSIBLE");
			
			
		}
	}
	return 0;
}

