#include <stdio.h>
#include <math.h>

int tc;
double c,f,x;

double t(int n)
{
	int i;
	double r=0;
	for(i=0;i<n;++i)
		r+=c/(2.0+i*f);
	r+=x/(2.0+n*f);
	return r;
}

int max(int p,int q){return p>q?p:q;}

int ans()
{
	return max(0,ceil((f*x/c-2)/f-1));
}

int main()
{
	int o;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	for(scanf("%d",&tc),o=1;o<=tc;++o)
	{
		scanf("%lf%lf%lf",&c,&f,&x);
		printf("Case #%d: %.7lf\n",o,t(ans()));
	}
	return 0;
}