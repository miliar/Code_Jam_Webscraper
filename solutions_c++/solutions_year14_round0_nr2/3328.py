// cookieca.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getNumTCases()
{
	char chBuff[16];
	char *pRet;

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return -1;

	return atoi(chBuff);
}

void readInputCFX(double* pfC, double* pfF, double* pfX)
{
	char chBuff[50];
	char *pRet;
	char *pch;

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	pch = strtok(chBuff, " ");
	*pfC = atof(pch);

	pch = strtok(NULL, " ");
	*pfF = atof(pch);

	pch = strtok(NULL, " ");
	*pfX = atof(pch);
}

int main(int argc, char* argv[])
{
	int iNoTCases = getNumTCases();
	double fC, fF, fX;
	double fCurrCookiesPerSec, fTimeTakenMS, fTimeForNextFarm;

	for(int i = 0; i < iNoTCases; i++)
	{
		readInputCFX(&fC, &fF, &fX);

		fCurrCookiesPerSec = 2.0f;
		fTimeTakenMS = 0.0f;

		while(1)
		{
			fTimeForNextFarm = fC/fCurrCookiesPerSec;

			//if( fTimeForNextFarm + fX/(fCurrCookiesPerSec + fF) > fX/fCurrCookiesPerSec )
			if( fTimeForNextFarm*fCurrCookiesPerSec + (fX*fCurrCookiesPerSec)/(fCurrCookiesPerSec + fF) > fX )
			{
				fTimeTakenMS += fX/fCurrCookiesPerSec;
				break;
			}

			fTimeTakenMS += fTimeForNextFarm;
			fCurrCookiesPerSec += fF;
		}

		printf("Case #%d: %.7f\n", i+1, fTimeTakenMS);

		int k;
	}

	return 0;
}

