#include<cstdio>
using namespace std;
int main()
{
	int t,T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		double c,f,x,ct=0,rate=2.0,pt=0;
		scanf("%lf%lf%lf,",&c,&f,&x);
		pt=c/rate;
		while((ct+x/rate)>(pt+x/(rate+f)))
		{
			ct=pt;
			rate=rate+f;	
			pt=pt+c/rate;
			//printf("%lf %lf\n",rate,ct);
		}
		ct=ct+x/rate;
		printf("Case #%d: %.7lf\n",t,ct); 
	}
	return 0;
}
