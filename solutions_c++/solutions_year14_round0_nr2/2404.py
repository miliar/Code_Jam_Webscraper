#include<stdio.h>

int main()
{
	int T;
	long double C,F,X,R;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%llf %llf %llf",&C,&F,&X);
		R = 2;
		
		long double TotalTime = X/R,curTime,preTime=C/R;
//		printf("%llf ",C/R);
//		printf("%llf \n",TotalTime);
		do
		{			
			curTime  = preTime;	
			R+=F;
//			printf("%llf ",C/R);
//			printf("%llf ",preTime);
			curTime  += X/R;	
//			printf("%llf ",X/R);
			if(curTime >=  TotalTime)
			{
				break;
			}
			TotalTime = curTime;
			preTime += C/R;
//			printf("%llf \n",TotalTime);
		}while(1);
//		printf("\n");
		printf("Case #%d: %.7llf\n",i,TotalTime);

	}
}
