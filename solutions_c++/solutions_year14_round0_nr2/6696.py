// Problem2-Cookie_Clicker_Alpha.c : Defines the entry point for the console application.
//
#include <stdio.h>
#include <tchar.h>
#include <Windows.h>
#include <float.h>

/* Structure to hold in the input parameters */
typedef struct CookieClicker
{
	long double CostFarm_C;
	long double FarmRate_F;
	long double WinCount_X;
}COOKIE_CLICKER;

DWORD dwNumInputs = 0;
COOKIE_CLICKER	*AllCookieGames = NULL;

#define OUTPUT_ANSWER(x,y)			wprintf(L"Case #%d: %-11.7f\n",x,y);

void parseInput(int argc, _TCHAR* argv[])
{
	/* Read the number of TCs */
	DWORD i = 0;
	wscanf_s(L"%d",&dwNumInputs);

	if(dwNumInputs == 0)
		exit(1);

	AllCookieGames = (COOKIE_CLICKER *) malloc(dwNumInputs*sizeof(COOKIE_CLICKER));
	
	/* Read in all the inputs */
	for(i = 0 ; i < dwNumInputs; i++)
	{
		COOKIE_CLICKER CookieGame = {0.0};
		wscanf_s(L"%Lf",&CookieGame.CostFarm_C);
		wscanf_s(L"%Lf",&CookieGame.FarmRate_F);
		wscanf_s(L"%Lf",&CookieGame.WinCount_X);

		AllCookieGames[i] = CookieGame;
	}
}

int _tmain(int argc, _TCHAR* argv[])
{
	DWORD i = 0;

	/* Parse the inputs */ 
	parseInput(argc, argv);

	for( i = 0 ; i < dwNumInputs; i++)
	{
		DWORD dwFarmCount = 0;
		long double fMinTime = 0;
		long double fTotalTime = 0.0;
		long double fCurrRate = 2.0;
		long double fNewRate = 0.0;
		long double fAddTime = 0.0;
		
		/* This is the minimum time required with base rate of 2 cookies per second.*/
		fMinTime = (AllCookieGames[i].WinCount_X)/2;
		while(1)
		{
			/* Now buy a farm */
			dwFarmCount++;

			/*Calculate the addtional time spent for buying the farm*/
			fAddTime += (AllCookieGames[i].CostFarm_C) / fCurrRate;

			/*Calculate the new cookie rate after buying the farm*/
			fCurrRate += AllCookieGames[i].FarmRate_F; 

			/* So total time spent is...*/
			fTotalTime = (AllCookieGames[i].WinCount_X) / fCurrRate;
			fTotalTime += fAddTime;

			if(fMinTime < fTotalTime)
				break;
			else
				fMinTime = fTotalTime;
				
		}

		OUTPUT_ANSWER((i+1),fMinTime);
	}
	free(AllCookieGames);
	return 0;
}

