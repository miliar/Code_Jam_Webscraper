#include<stdio.h>
#include<math.h>
int main()
{
	int t,loop,k,j;
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		double c,f,x,time=0,s=2.00,s1,s2,s3;
		scanf("%lf %lf %lf",&c,&f,&x);
		while(1)
		{
			s1=c/s;
			s2=x/s;
			s3=x/(s+f);
			if(s1+s3 > s2)
			{
				//time=time+c/s;
				//s=s+f;
				//s1=s1+time;
				break;
			}
			else
			{
				time=time+c/s;
				s=s+f;
			}
		}
		//printf("%.7lf",time);
		time=time+(x/s);
		printf("Case #%d: %.7lf\n",k,time);
	}
	return 0;
}
