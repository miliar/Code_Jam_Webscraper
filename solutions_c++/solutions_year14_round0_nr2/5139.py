#include<stdio.h>

int main()
{
	int t,z=0;
	scanf("%d",&t);
	while(t--)
	{
		z++;
		double c,f,x,g,m;
		scanf("%lf%lf%lf",&c,&f,&x);
		double time=0;
		double p=x/2;
		double ptr=2;
		while(1)
		{
			 g=c/ptr;
			ptr=ptr+f;
			m=x/ptr;
		//	printf("%lf %lf %lf %lf\n",p,g,m,time);
			if(p<g+m)
			break;


			else
			{
				time=time+g;
				p=m;
			}
		}
		time=time+p;
		printf("Case #%d: %0.7lf\n",z,time);
	}
	return 0;
}
