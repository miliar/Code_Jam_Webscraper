#include <cstdio>
#include <climits>


int main()
{
	int testy; scanf("%d",&testy);
	
	for( int test = 1 ; test <= testy ; test ++ )
	{
		double C, F, X;
		scanf("%lf%lf%lf",&C,&F,&X);
		
		double totalTime = 0;
		double currentProductionTime = 2.0;
		
		while( true )
		{
			double waitStd = X/currentProductionTime;
			
			// simulate buying farm
			
			double waitToBuild = C/currentProductionTime;
			double tmpProductionTime = currentProductionTime+F;
			double waitWithFarm = X/tmpProductionTime;
			
			//printf("CURTIME: %lf CURSPEED: %lf\n",totalTime,currentProductionTime);
			//printf("WAITSTD: %lf --- WAITFARM: %lf\n",waitStd, waitWithFarm+waitToBuild);
			
			if( waitStd <= waitWithFarm+waitToBuild ) {
				totalTime += waitStd;
				//printf("TIME: %lf\n",totalTime);
				break;
			}
			else {
				totalTime += waitToBuild;
				currentProductionTime = tmpProductionTime;
				//printf("TIME: %lf SPEED: %lf\n",totalTime,currentProductionTime);
			}
		}
		
		printf("Case #%d: %lf\n",test,totalTime);
	}
	
	return 0;
}