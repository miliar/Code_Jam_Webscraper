// gcj2.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#define BASE_PRODUCTION 2

int _tmain(int argc, _TCHAR* argv[])
{
	int iTestCases = 0;
	
	double dPriceC = 0; 
	double dProductionF = 0;
	double dGoalX = 0; 

	double dActualModifier = 0;
	double dMinimumSecounds = 0;
	double dTimeNextFarm=0;
	double dTimeMod = 0;
	
	//read input
	FILE *fpIn = fopen("gcj2.txt", "r");
	FILE *fpOut = fopen("output.txt", "w");
	if (fpIn == NULL || fpOut == NULL) {
		return 1;
	}

	fscanf(fpIn, "%d", &iTestCases);
	for(int i = 0; i < iTestCases; i++){
		fscanf(fpIn, "%lf %lf %lf", &dPriceC, &dProductionF, &dGoalX);
		dMinimumSecounds = dGoalX/(BASE_PRODUCTION + dActualModifier);
		do{			
			dTimeNextFarm = dPriceC/(BASE_PRODUCTION+dActualModifier);
			dActualModifier += dProductionF;
			//minimum Number of Seconds
			if(dTimeMod + dTimeNextFarm + dGoalX/(BASE_PRODUCTION+dActualModifier) < dMinimumSecounds){
				dTimeMod += dTimeNextFarm;
				dMinimumSecounds = dTimeMod + dGoalX/(BASE_PRODUCTION+dActualModifier);
				
			}
			else
			{
				break;
			}
		}while (true);
		//Output

		fprintf(fpOut, "Case #%d: %lf\n", i+1,dMinimumSecounds);
		dActualModifier = 0;
		dTimeMod = 0;
	}
	fclose(fpIn);
	fclose(fpOut);
	return 0;
}

