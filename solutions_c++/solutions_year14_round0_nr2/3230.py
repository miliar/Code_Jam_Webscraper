#include <stdio.h>

int main()
{
	int t;
	scanf("%d",&t);
	for(int ti=1;ti<=t;ti++)
	{
		printf("Case #%d: ",ti);
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		double time=X/2.0;
		for(int m=1;m<=10000000;m++)
		{
			double cur=time+C/(2.0+(m-1)*F)+X/(2.0+m*F)-X/(2.0+(m-1)*F);
			if(cur>time)
			{
				printf("%.7lf\n",time);
				break;	
			}
			time=cur;
		}
	}
	return 0;
}
