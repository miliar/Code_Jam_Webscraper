#include<cstdio>
#include<cstring>
#include<cmath>
#include<iomanip>
#include<algorithm>
#define LL long long
using namespace std;
int n,m;
long double X,V,Cmax,Cmin;
long double eps=1e-15;
int sgn(long double x)
{
	if (x<-eps) return -1;
	return x>eps;
}
struct point
{
	long double l,c;
}p[1010];
struct node
{
	long double r,c;
}q[1010];
bool cmp2(node x,node y)
{
	return x.c<y.c;
}
bool cmp(point x,point y)
{
	return x.c<y.c;
}
bool ok(long double k)
{
	if (n==1) return V==k*q[1].r;
//	long double tot=0;
//	for (int i=1;i<=n;i++) tot+=k*q[i].r;
//	if (sgn(tot-V)<0) return false;
//	if (n==1) return true;	
	long double T=V*(X-q[1].c);
	for (int i=2;i<=n;i++)
	p[i].c=q[i].c-q[1].c;
	for (int i=2;i<=n;i++) p[i].l=q[i].r*k;
	sort(p+2,p+n+1,cmp);
	long double L=0,R=0;
	long double Vt=V-k*q[1].r;
	for (int i=2;i<=n&&Vt>0;i++)
	{
		L+=min(Vt,p[i].l)*p[i].c;
		Vt-=min(Vt,p[i].l);
	}
	Vt=V;
	for (int i=n;i>=2&&Vt>0;i--)
	{
		R+=min(Vt,p[i].l)*p[i].c;
		Vt-=min(Vt,p[i].l);
	}
	if (sgn(L-T)<=0&&sgn(R-T)>=0) return true;
	return false;
}
void work(int lab)
{
	printf("Case #%d: ",lab);
	scanf("%d",&n);
	double vv,xx;
	scanf("%lf%lf",&vv,&xx);
	V=vv;
	X=xx;
	Cmax=-1e50;
	Cmin=1e50;
	for (int i=1;i<=n;i++)
	{
		double r,c;
		scanf("%lf%lf",&r,&c);
		q[i].r=r;
		q[i].c=c;
		Cmax=max(Cmax,q[i].c);
		Cmin=min(Cmin,q[i].c);
	}
	sort(q+1,q+n+1,cmp2);
	if (!(sgn(Cmax-X)>=0&&sgn(Cmin-X)<=0))
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	int cd=1;
	for (int i=1;i<=n;i++) if (q[i].c!=q[1].c) cd=0;
	if (cd)
	{
		double tot=0;
		for (int i=1;i<=n;i++) tot+=q[i].r;
		printf("%.15f\n",(double)V/tot);
		return;
	}
	if (n==1)
	{
		printf("%.15f\n",(double)(V/q[1].r));
		return;
	}
	if (n==2)
	{
		if (sgn(q[1].c-q[2].c)==0)
		{
			printf("%.15f\n",(double)(V/(q[1].r+q[2].r)));
			return;
		}
		double Y=(V*X-q[1].c*V)/(q[2].c-q[1].c);
		double X=V-Y;
		double ans=max(Y/q[2].r,X/q[1].r);
		printf("%.15f\n",ans);
		return;
	}
	double tmp;
	if (n==1) 
	{
		tmp=(double)(V/q[1].r);
		printf("%.15f\n",tmp);
		return;
	}
	long double l=0,r=1e10;
	for (int i=1;i<=500;i++)
	{
		long double mid=(l+r)/2;
		if (ok(mid)) r=mid;
		else l=mid;
	}

//	if (n==2&&abs(ans-l)/abs(ans)>1e-6)
//		printf("!");
	printf("%.15f\n",(double)l);
}
int main()
{
//	freopen("data.in","r",stdin);
//	freopen("data.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for (int i=1;i<=t;i++)work(i);
	return 0;
}
