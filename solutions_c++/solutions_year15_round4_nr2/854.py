#include<cstdio>
#include<cstring>
#include<algorithm>
#include<cmath>
using namespace std;
int n,Test;
double T,V;
struct str
{
	double v,t;
}a[128];
bool cmp(str x,str y)
{
	return (x.t<y.t)||(x.t==y.t&&x.v>y.v);
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&Test);
	for(int t=1;t<=Test;t++)
	{
		scanf("%d%lf%lf",&n,&V,&T);
		for(int i=1;i<=n;i++)
			scanf("%lf%lf",&a[i].v,&a[i].t);
		sort(a+1,a+n+1,cmp);
		double A=0,B=0,C=0,D=0;
		int l;
		for(l=1;l<=n;l++)
		{
			if(a[l].t>=T-1e-9)break;
			A+=a[l].v*a[l].t;
			C+=a[l].v;
		}
		for(int i=l;i<=n;i++)
		{
			B+=a[i].v*a[i].t;
			D+=a[i].v;
		}
		if(C<1e-9 || D< 1e-9)
		{
			if(fabs(a[l].t-T)<1e-9)
			{
				double vv=0;
				for(int i=l;i<=n;i++)if(fabs(a[i].t-T)<1e-9)
					vv+=a[i].v;
				printf("Case #%d: %.8f\n",t,V/vv);
				continue;
			}
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		double Y=(T*V*C-A*V)/(B*C-A*D);
		double X=(V-D*Y)/C;
		double ans=max(X,Y);
		printf("Case #%d: %.8f\n",t,ans);
	}
}