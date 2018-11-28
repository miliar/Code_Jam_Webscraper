#include<cstdio>
#include<cmath>
#define	PI 3.14159265359
#define ln long long
int main()
{
	int tt,run=1;
	double r,t;
	scanf("%d",&tt);
	while(run<=tt)	
	{
		scanf("%lf %lf",&r,&t);
		double tmp = t;
		double lr = r+1;
		double tmp2=(lr-1)*(lr-1);
		long long count = 0;
		while(tmp>0)
		{
			tmp -= (lr*lr-tmp2);
			count++;
			tmp2 = (lr+1)*(lr+1);
			lr+=2;
			//printf("%lf= ",tmp);
		}
		if(tmp==0)
			printf("Case #%d: %lld\n",run,count);
		else
			printf("Case #%d: %lld\n",run,count-1);
		run++;
	}
	return 0;
}
