/*
	Author : ChnLich
*/
#include<cstdio>
#include<cmath>
#include<iomanip>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<set>
#include<map>
#include<string>
#include<bitset>
#include<functional>
#include<utility>

using namespace std;

typedef long long llint;
typedef pair<int,int> ipair;
typedef unsigned int uint;
#define pb push_back
#define fi first
#define se second
#define mp make_pair

const int MOD=1000000007,dx[]={0,1,0,-1},dy[]={1,0,-1,0};
const double eps=1e-8;

void read(int &k)
{
	k=0; char x=getchar();
	while(x<'0'||x>'9') x=getchar();
	while(x>='0'&&x<='9') { k=k*10-48+x; x=getchar(); }
}

int T,n;
double V,X;

struct arr
{
	int r,c;
	bool operator < (const arr&b) const
	{
		return c<b.c;
	}
} a[110];

bool calc(double x)
{
	double cntV=0,cntX=0;
	for(int i=0;i<n;i++)
	{
		double ma=x*a[i].r;
		double tmp=min(ma,V-cntV);
		cntV+=tmp;
		cntX+=tmp*a[i].c;
	}
	if (cntV<V-1e-10)
		return 0;
	if (cntX>1ll*V*X)
		return 0;
	cntV=0;
	cntX=0;
	for(int i=n-1;i>=0;i--)
	{
		double ma=x*a[i].r;
		double tmp=min(ma,V-cntV);
		cntV+=tmp;
		cntX+=tmp*a[i].c;
	}
	if (cntX<1ll*V*X)
		return 0;
	return 1;
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		double tV,tX;
		scanf("%d%lf%lf",&n,&tV,&tX);
		V=int(tV*10000+0.5);
		X=int(tX*10000+0.5);
		for(int i=0;i<n;i++)
		{
			double x,y;
			scanf("%lf%lf",&x,&y);
			a[i].r=int(x*10000+0.5);
			a[i].c=int(y*10000+0.5);
		}
		sort(a,a+n);
		int fl=0,fr=0;
		for(int i=0;i<n;i++)
			if (a[i].c<=X)
				fl=1;
		for(int i=0;i<n;i++)
			if (a[i].c>=X)
				fr=1;
		if (!fl||!fr)
		{
			printf("Case #%d: IMPOSSIBLE\n",tt);
			continue;
		}
		llint flow=0;
		for(int i=0;i<n;i++)
			if (a[i].c==X)
				flow+=a[i].r;
		double R=1e9;
		if (flow) R=min(R,1.0*V/flow);
		double L=0;
		for(int p=0;p<200;p++)
		{
			double t=(L+R)/2;
			if (calc(t)) R=t; else L=t;
		}
		
		printf("Case #%d: %.10f\n",tt,R);
	}
	
	return 0;
}
