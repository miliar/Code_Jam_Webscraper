#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <list>
#include <queue>
#include <vector>
#include <ctime>
#include <set>
#include <bitset>
#include <deque>
#include <fstream>
#include <stack>
#include <map>
#include <utility>
#include <cassert>
#include <string>
#include <iterator>
#include <cctype>
using namespace std;
typedef long long LL;
typedef long double LD;
double getd()
{
    double d=0,d2=0,d3=1; char ch; bool flag=0;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')flag=true;else d=ch-48;
    while(isdigit(ch=getchar()))d=d*10+ch-48;
    if(ch=='.')
    {
        while(isdigit(ch=getchar()))d2=d2*10+ch-48,d3=d3*0.1;
        d+=d3*d2;
    }
    if(flag)return -d;else return d;
}
int get()
{
    int f=0,v=0;char ch;
    while(!isdigit(ch=getchar()))if(ch=='-')break;
    if(ch=='-')f=1;else v=ch-48;
    while(isdigit(ch=getchar()))v=v*10+ch-48;
    if(f==1)return -v;else return v;
}
const int maxn=1000;
int n;
double V,C;
double rr[maxn],c[maxn];
pair<double,double> a[maxn];
const LD eps=1e-12;
int sig(LD x)
{
	if(fabs(x)<=eps)return 0;
	else if(x>eps)return 1;
	else return -1;
}
bool check(long double x)
{
	long double vv,cc;
	long double L,R;
	vv=0,cc=0;
	long double tot=0;
	for(int i=1;i<=n;i++)
	{
		tot+=a[i].second*x;
	}
	if(sig(tot-V)<0)return 0;
	for(int i=1;i<=n;i++)
	{
		long double tmp=min(a[i].second*x,LD(V-vv));
		cc=(vv*cc+tmp*a[i].first)/(vv+tmp);
		vv+=tmp;
	}
	L=cc;
	vv=cc=0;
	for(int i=n;i>=1;i--)
	{
		long double tmp=min(a[i].second*x,LD(V-vv));
		cc=(vv*cc+tmp*a[i].first)/(vv+tmp);
		vv+=tmp;
	}
	R=cc;
	return sig(C-L)>=0&&sig(R-C)>=0;
}
int main()
{
	freopen("Bl.in","r",stdin);
	freopen("Bl.out","w",stdout);
	int T=get();
	for(int _=1;_<=T;_++)
	{
		cerr<<_<<endl;
		long double l=0,r=0;
		n=get();
		scanf("%lf%lf",&V,&C);
		for(int i=1;i<=n;i++)
		{
			scanf("%lf%lf",&rr[i],&c[i]);
			r=max(r,LD(V/rr[i]));
			a[i]=make_pair(c[i],rr[i]);
		}
		sort(a+1,a+1+n);
		bool have=0;
		r+=100;
		while(r-l>1e-10)
		{
			long double mid=(l+r)*0.5;
			if(check(mid))r=mid,have=1;else l=mid;
		}
		if(have)printf("Case #%d: %.10lf\n",_,double(l));
		else printf("Case #%d: IMPOSSIBLE\n",_);
	}
	return 0;
}
