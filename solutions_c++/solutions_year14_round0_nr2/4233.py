#include<stdio.h>

int main()
{
	int t,T = 1;
	scanf("%d",&t);
	while(t--)
	{
		double C,F,X,coins = 2,time = 0,temp_1,temp_2,ans;
		scanf("%lf %lf %lf",&C,&F,&X);
		printf("Case #%d: ",T++);
		while(1)
		{
			temp_1 = time + (X/coins);
			temp_2 = time + (C/coins) + (X/(coins+F));
			if(temp_1 <= temp_2)
			{
				ans = temp_1;
				break;
			}
			time = temp_2 - + (X/(coins+F));
			coins += F;
		}
		printf("%0.7lf\n",ans);
	}
	return 0;
}
