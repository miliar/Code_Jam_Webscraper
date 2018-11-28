#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)

#define maxn 110
#define eps 0.000001
//#define maxm 1010
//#define maxk 1010

struct node
{
	double c,r;
}a[maxn];

bool cmp(const node &x, const node &y)
{
	return x.c<y.c;
}

double cal(double r1,double r2,double x1,double x2,double v,double x)
{
	double v2=v*(x-x1)/(x2-x1);
	double v1=v-v2;
	double t2=v2/r2;
	double t1=v1/r1;
	return max(t1,t2);
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T;
	scanf("%d",&T);
	FOR(TT,1,T)
	{
		printf("Case #%d: ",TT);
		
		int n;
		double v,x;
		cin>>n>>v>>x;
		FOR(i,1,n)
			cin>>a[i].r>>a[i].c;
		sort(a+1,a+n+1,cmp);
		int n1=1;
		FOR(i,2,n)
			if (fabs(a[i].c-a[i-1].c)<=eps)
				a[n1].r+=a[i].r;
			else
			{
				n1++;
				a[n1].c=a[i].c;
				a[n1].r=a[i].r;
			}
		n=n1;
		if (x<a[1].c-eps || x>a[n].c+eps)
		{
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		
		if (n==1)
		{
			printf("%.9f\n",v/a[1].r);
			continue;
		}
		
		double sum_energy=0, sum_r=0;
		FOR(i,2,n)
		{
			sum_energy+=a[i].r*a[i].c;
			sum_r+=a[i].r;
		}
		double ans=cal(a[1].r,sum_r,a[1].c,sum_energy/sum_r,v,x);
		
		sum_energy=0, sum_r=0;
		FOR(i,1,n-1)
		{
			sum_energy+=a[i].r*a[i].c;
			sum_r+=a[i].r;
		}
		ans=min(ans,cal(a[n].r,sum_r,a[n].c,sum_energy/sum_r,v,x));
		
		printf("%.9f\n",ans);
	}
	
	return 0;
}
