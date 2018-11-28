#include <stdio.h>

struct Test 
{
	double C,F,X;
};

int main()
{
	int T;
	double C,F,X;
	scanf("%d",&T);
	Test test[100];
	double result[100]={0.0};
	int j=0,i=0,m=0,o=0;
	for(j=0;j<T;j++)
	{
		scanf("%lf %lf %lf",&test[j].C,&test[j].F,&test[j].X);
		double nowF = 2.0;
		double totalTime = 0.0;
		while(1)
		{
			double doBuy = test[j].C/nowF+test[j].X/(nowF+test[j].F);
			double donotBuy = test[j].X/nowF;
			if (doBuy < donotBuy)
			{
				totalTime += test[j].C/nowF;
				nowF += test[j].F;
			}else
			{
				totalTime += donotBuy;
				result[j] = totalTime;
				break;
			}
		}
		
	}
	for(j=0;j<T;j++)
	{
			printf("Case #%d: %0.7f\n",j+1,result[j]);
	}

	getchar();
	getchar();
	return 0;
}
