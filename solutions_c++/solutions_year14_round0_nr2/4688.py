#include<stdio.h>
#include<algorithm>
using namespace std;
double min(double a, double b)
{
	return a < b ? a : b;
}
int main()
{
	freopen("F:in.txt","r",stdin);
	freopen("F:Out.txt","w",stdout);
    int T, cas  = 0;
	double C, F, X;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf%lf%lf",&C,&F,&X);
		double sum = 0;
		double ans = 0x3fffffff;
		double rate = 2;
		int N = 2500;
		while(N--)
		{
			double t1 = C / rate;
			double t2 = X / rate;
			rate += F;
			double t3 = X / rate;
			double tmp1 = sum + t2;
			sum += t1;
			ans = min(ans, tmp1);
			ans = min(ans, sum + t3);
		}
		printf("Case #%d: %.7lf\n",++cas,ans);
    }
    return 0;
}





