#include<bits/stdc++.h>
using namespace std;
double calc(double n,double f,double c,double x)
{
	if((x/n)<=(c/n)+(x/(n+f)))
        return (x/n);
	return min(x/n,(c/n)+calc(n+f,f,c,x));
}
int main()
{
	int tc;
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++)
	{
		double c,f,x;
		scanf("%lf%lf%lf",&c,&f,&x);
		double ans=min((x/2.0000000),(c/2.0000000)+calc(f+2.0000000,f,c,x));
		printf("Case #%d: %.7lf\n",t,ans);
	}
	return 0;
}
