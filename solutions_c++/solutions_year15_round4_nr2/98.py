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

#define eps 1e-10
#define maxn 110

struct atype
{
	double r, t;
};
atype a[maxn];

int cmp(const atype &a, const atype &b)
{
	if (fabs(a.t-b.t)>eps) return a.t<b.t;
	return a.r<b.r;
}

int n; 
double V,X; 

int check(double t)
{
	double z=V, w=0;
	rep(i,1,n)
	{
		double cz=a[i].r*t;
		if (z>=cz)
		{
			z-=cz; w+=a[i].t*cz;
		}
		else
		{
			w+=a[i].t*z; z=0; 
		}
	}
	if (z>eps) return 0;
	double wlow=w/V;
	
	z=V, w=0;
	repd(i,n,1)
	{
		double cz=a[i].r*t;
		if (z>=cz)
		{
			z-=cz; w+=a[i].t*cz;
		}
		else
		{
			w+=a[i].t*z; z=0; 
		}
	}
	if (z>eps) return 0;
	double whigh=w/V;
	
	if (wlow<=X+eps && X<=whigh+eps) return 1;
	return 0;
}

void lemon()
{
	scanf("%d%lf%lf",&n,&V,&X);
	rep(i,1,n) scanf("%lf%lf",&a[i].r,&a[i].t);
	sort(a+1,a+n+1,cmp);
	double left=0, right=1e9;
	rep(it,0,200)
	{
		double mid=(left+right)/2;
		if (check(mid)) right=mid; else left=mid;
	}
	if (left>5e8) 
		printf("IMPOSSIBLE\n");
	else  printf("%.10lf\n",left);
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

