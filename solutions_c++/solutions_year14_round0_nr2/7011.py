#include<stdio.h>
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B_output2.txt","w",stdout);
	int T,q;
	double rate,C,F,X,time;
	scanf("%d",&T);
	for(q=1;q<=T;q++)
	{
		rate=2;time=0;
		scanf("%lf %lf %lf",&C,&F,&X);
		refind:
		double t=X/rate;
		double s=X/(rate+F)+C/rate;
		if(s<t){time+=(C/rate);rate+=F;goto refind;}
		else time+=t;
		printf("Case #%d: %.7lf\n",q,time);
	}
	return 0;
}