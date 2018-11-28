#include <stdio.h>

int main()
{
	int t;
	double c,f,x,m;
	double tim;
	
	
	scanf("%d",&t);
	for(int i1=1;i1<=t;i1++)
	{
		scanf("%lf %lf %lf",&c,&f,&x);
		m=0;
		tim=0;
		while(c/f*(2+f*m)+c<x)
		{
			tim+=c/(2+f*m);
			m++;
		}
		tim+=x/(2+f*m);
		printf("Case #%d: %.7lf\n",i1,tim);
	}
	
	return 0;
}

