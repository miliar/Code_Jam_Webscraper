#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
const int maxn=100000+10;

struct nodes
{
	double beg_time;
	double end_time;
}fa[maxn*2];

void init(double c,double f,double x)
{
	fa[0].end_time=x/2.0;
	fa[0].beg_time=0.0;
}

int main ()
{
	freopen("wocaca.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int t;
	while (scanf("%d",&t)==1)
	{
		for (int ii=1;ii<=t;ii++)
		{
			double c,f,x;
			scanf("%lf%lf%lf",&c,&f,&x);
			init(c,f,x);
			int nima=x+1.0;
			for (int i=1;i<=nima;i++)
			{
				fa[i].beg_time=fa[i-1].beg_time+(c/(((double)(i-1))*f+2.0));
				fa[i].end_time=fa[i].beg_time+(x/(((double)i)*f+2.0));
			}
			double mini=100000.0;
			for (int i=0;i<=nima;i++)
			{
				mini=mini<fa[i].end_time?mini:fa[i].end_time;
			}
			printf("Case #%d: %.7f\n",ii,mini);
		}
	}
	fclose(stdout);
	fclose(stdin);
	return 0;
}