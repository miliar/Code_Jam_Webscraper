#include <stdio.h>

double C,F,X;
double result;

void work()
{
	int i;
	double t,now,rate;
	result=X/2;
	t=0;
	rate=2.0;
	for (i=1; ; ++i)
	{
		t+=C/rate;
		rate+=F;
		if (t+X/rate<result)
			result=t+X/rate;
		if (t>=result-(1e-7))
			break;
	}
}

int main()
{
	int i,j,k,w,T,x;
	freopen("B.in","r",stdin);
	scanf("%d",&T);
	for (w=1; w<=T; ++w)
	{
		printf("Case #%d: ",w);
		scanf("%lf%lf%lf",&C,&F,&X);
		work();
		printf("%.7lf\n",result);
	}
	return 0;
}
