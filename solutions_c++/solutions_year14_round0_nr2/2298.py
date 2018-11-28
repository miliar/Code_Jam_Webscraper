#include<cstdio>

int main(void)
{
	int numbersOfCases;
	
	scanf("%d",&numbersOfCases);
	for(int nowCase=1;nowCase<=numbersOfCases;++nowCase){
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		
		double secondsTillLastLastRound=0.0;
		double secondsToAchieveLastRound=X/2.0;
		double secondsToAchieveThisRound;
		double secondsToBuyFarmLastRound=C/2.0;
		int round=1;
		bool finished=false;
		while(!finished){
			secondsToAchieveThisRound=X/(2.0+(double)round*F);
			if(secondsToAchieveLastRound<=secondsToBuyFarmLastRound+secondsToAchieveThisRound){
				finished=true;
				printf("Case #%d: %.7f\n",nowCase,secondsTillLastLastRound+secondsToAchieveLastRound);
			}
			secondsTillLastLastRound+=secondsToBuyFarmLastRound;
			secondsToAchieveLastRound=secondsToAchieveThisRound;
			secondsToBuyFarmLastRound=C/(2.0+(double)round*F);
			++round;
		}
	}
	
	return 0;
}
