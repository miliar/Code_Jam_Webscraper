#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;
double Time(double C, double F, double X, int NOC)
{
	double CPS=2.0;
	double t=0, t1=0;
	for(int i=0; i<NOC; i++)
	{
		t+=C/CPS;
		CPS+=F;
	}
	t1=X/CPS;
	return t+t1;	
}
void main(void)
{
	int n=0;
	double a[10000];
	double F, C, X, CPS=2.0, Cookies=0.0;
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%i",&n);
	for(int k=1; k<=n;k++)
	{
		scanf("%lf",&C);
		scanf("%lf",&F);	
		scanf("%lf",&X);
		a[0]=X/CPS;

		for(int i=1;i<10000;i++)
			a[i]=Time(C,F,X,i);
		sort(a,10000+a);
		printf("Case #%i: %.7lf\n", k, a[0]);
	}
}


