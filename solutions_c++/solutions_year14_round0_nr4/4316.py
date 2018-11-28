// gcj4.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"
#include <string.h>
#include <stdlib.h>

float getMax(float *fPool, int iCount);
float getMin(float *fPool, int iCount);
int getMinPos(float *fPool, int iCount);
int getMaxPos(float *fPool, int iCount);
int getHigherNeighbour(float *fPool, int iCount, float fThreshold);

int _tmain(int argc, _TCHAR* argv[])
{
	int iTestCases = 1;
	int iWeights;

	float *fNaomiPool;
	float *fKenPool;

	bool bKen = false;
	float fNaomiMax = 0;
	float fKenMax = 0;

	int   iNaomiPoint = 0;

	int iNaomiPointWar = 0;
	//read input
	FILE *fpIn = fopen("gcj4.txt", "r");
	FILE *fpOut = fopen("output.txt", "w");
	if (fpIn == NULL || fpOut == NULL) {
		return 1;
	}

	fscanf(fpIn, "%d", &iTestCases);
	for(int i = 0; i < iTestCases; i++){
		fscanf(fpIn, "%d", &iWeights);
		fNaomiPool = new float[iWeights];
		fKenPool = new float[iWeights];
		for(int j = 0; j < iWeights; j++){
			fscanf(fpIn, "%f", &fNaomiPool[j]);
		}

		for(int j = 0; j < iWeights; j++){
			fscanf(fpIn, "%f", &fKenPool[j]);
		}

		//war
		for(int j=0; j < iWeights; j++){
			fNaomiMax = getMin(fNaomiPool, iWeights);//Naomi plays min
			fKenMax = getMax(fKenPool, iWeights); // if Ken can Beat, he will
/*			for(int k = 0; k < iWeights; k++){
				printf("%f ", fKenPool[k]);
			} */
			printf("\n", fKenPool);
			if(fKenMax > fNaomiMax)
			{
				bKen = true;
			}
			else
			{
				bKen = false;
			}
			if(bKen){
				fKenPool[getHigherNeighbour(fKenPool, iWeights, fNaomiMax)] *= -1; //Ken takes nearest Higher Number
				fNaomiPool[getMinPos(fNaomiPool, iWeights)] *= -1;
			}
			else {
				iNaomiPointWar++; //Noami scores, ken takes lowest
				fNaomiPool[getMinPos(fNaomiPool, iWeights)] *= -1;
				fKenPool[getMinPos(fKenPool, iWeights)] *= -1; //Ken takes nearest Higher Number
			}
		}
		// reset
		for(int j=0; j < iWeights; j++){
			fKenPool[j] *= -1;
			fNaomiPool[j] *= -1;
		} 
		//who has the highest weight
		for(int j=0; j < iWeights; j++){
			fNaomiMax = getMax(fNaomiPool, iWeights);
			fKenMax = getMax(fKenPool, iWeights);
		
			if(fKenMax > fNaomiMax)
			{
				bKen = true;
			}
			else
			{
				bKen = false;
			}
			if(bKen) //Naomi tells her lowest Weight as < KenMaxWeight
			{
				fNaomiPool[getMinPos(fNaomiPool, iWeights)] *= -1; 
				fKenPool[getMaxPos(fKenPool, iWeights)] *= -1;
			}
			else { //Naomi plays her highest Weight and beats Kens MaxWeight
				iNaomiPoint++;
				fNaomiPool[getMaxPos(fNaomiPool, iWeights)] *= -1; 
				fKenPool[getMaxPos(fKenPool, iWeights)] *= -1;
			}
		}
		fprintf(fpOut, "Case #%d: %d %d\n", i+1, iNaomiPoint, iNaomiPointWar);
		iNaomiPoint = 0; 
		iNaomiPointWar = 0;
		fNaomiMax = 0;
		fKenMax = 0;
		delete fNaomiPool;
		delete fKenPool;
	}

	fclose(fpIn);
	fclose(fpOut);
	return 0;
}

float getMax(float *fPool, int iCount)
{
	float fRet = 0;
	for(int i = 0; i < iCount; i++){
		if(fPool[i] > fRet)
			fRet = fPool[i];
	}
	return fRet;
}

float getMin(float *fPool, int iCount)
{
	float fRet = 1;
	for(int i = 0; i < iCount; i++){
		if(fPool[i] < fRet && fPool[i] > 0.0000000000000)
			fRet = fPool[i];
	}
	return fRet;
}

int getMinPos(float *fPool, int iCount)
{
	int iRet = 0;
	float fMin = 1;
	for(int i = 0; i < iCount; i++){
		if(fPool[i] < fMin && fPool[i] > 0.0000000000000)
		{
			iRet = i;
			fMin = fPool[i];
		}
	}
	return iRet;
}

int getMaxPos(float *fPool, int iCount)
{
	int iRet = 0;
	float fMax = 0;
	for(int i = 0; i < iCount; i++){
		if(fPool[i] > fMax && fPool[i] > 0.0000000000000)
		{
			iRet = i;
			fMax = fPool[i];
		}
	}
	return iRet;
}

int getHigherNeighbour(float *fPool, int iCount, float fThreshold){
	int iRet = 0;
	int iPosMin = getMaxPos(fPool, iCount);
	bool bSet = false;
	for(int i = 0; i < iCount; i++){
		if(fPool[i] > fThreshold && fPool[i] < fPool[iPosMin]){
			iPosMin = i;
			iRet = i;
			bSet = true;
		}
	}
	if(!bSet)
		iRet = iPosMin;
	return iRet;
}