// dectfwar.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int getIntFromSi()
{
	char chBuff[16];
	char *pRet;

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return -1;

	return atoi(chBuff);
}

void getFloatsFromSi(float* pfUser, int iNoMasses)
{
	char chBuff[8003];
	char *pch;

	gets(chBuff); //read line from stdin

	pch = strtok(chBuff, " ");

	for(int i = 0; i < iNoMasses; i++)
	{
		pfUser[i] = atof(pch);
		pch = strtok(NULL, " ");
	}
}

void sortFloats(float* pfArray, int iCount)
{
	float fTmp;

	for(int i=0; i < iCount; i++)
	{
		for(int j=i+1; j < iCount; j++)
		{
			if(pfArray[i] > pfArray[j])
			{
				fTmp = pfArray[i];
				pfArray[i] = pfArray[j];
				pfArray[j] = fTmp;
			}
		}
	}
}

void printFloats(float* pfArray, int iCount)
{
	for(int i=0; i < iCount; i++)
		printf("%g ", pfArray[i]);
	printf("\n");
}

int getNextGreaterFloatIndex(float* pfKen, unsigned char* pucKenUsed, float fToFind, int iCount, int* piStartIndex)
{
	bool bContinuous = true;

	for(int i = *piStartIndex; i < iCount; i++)
	{
		if( 1 == pucKenUsed[i] )
			continue;

		if( pfKen[i] > fToFind )
		{
			if( true == bContinuous )
				*piStartIndex = i + 1;
			pucKenUsed[i] = 1;
			return i;
		}

		bContinuous = false;
	}

	//greater not found, return smallest
	for(int i = *piStartIndex; i < iCount; i++)
	{
		if( 1 == pucKenUsed[i] )
			continue;

		pucKenUsed[i] = 1;
		return i;
	}
}

bool getSmallest(float* pfValArr, unsigned char* pucUsedArr, int iCount, float* pfOut, int* piIndxOut)
{
	for(int i = 0; i < iCount; i++)
	{
		if( 1 == pucUsedArr[i] )
			continue;

		*pfOut = pfValArr[i];
		if( 0 != piIndxOut )
			*piIndxOut = i;
		return true;
	}

	return false;
}

bool getLargest(float* pfKen, unsigned char* pucKenUsed, int iCount, float* pfOut)
{
	for(int i = iCount-1; i >= 0; i--)
	{
		if( 1 == pucKenUsed[i] )
			continue;

		*pfOut = pfKen[i];
		return true;
	}

	return false;
}

bool getGreaterThan(float* pfNaomi, unsigned char* pucNaomiUsed, int iCount, float fValue, float* pfOut)
{
	for(int i = 0; i < iCount; i++)
	{
		if( 1 == pucNaomiUsed[i] )
			continue;

		if( pfNaomi[i] > fValue )
		{
			*pfOut = pfNaomi[i];
			pucNaomiUsed[i] = 1;
			return true;
		}
	}

	return false;
}

int main(int argc, char* argv[])
{
	int iNoTCases = getIntFromSi();
	//printf("%d\n", iNoTCases);
	double fC, fF, fX;
	double fCurrCookiesPerSec, fTimeTakenMS, fTimeForNextFarm;

	for(int i = 0; i < iNoTCases; i++)
	{
		int iNoMasses = getIntFromSi();
		//printf("%d\n", iNoMasses);

		float *pfNaomi = new float[iNoMasses];
		float *pfKen = new float[iNoMasses];
		unsigned char *pucNaomiUsed = new unsigned char[iNoMasses];
		for(int k = 0; k < iNoMasses; k++)
			pucNaomiUsed[k] = 0;
		unsigned char *pucKenUsed = new unsigned char[iNoMasses];
		for(int k = 0; k < iNoMasses; k++)
			pucKenUsed[k] = 0;
		float fNaomi, fNaomiDW;
		float fLarge, fSmall, fGreater;
		int iFoundIndex, iKenIndex = 0, iNaomiIndex;
		int iNaomiScoreW = 0, iNaomiScoreDW = 0;

		getFloatsFromSi(pfNaomi, iNoMasses);
		getFloatsFromSi(pfKen, iNoMasses);

		sortFloats(pfNaomi, iNoMasses);
		sortFloats(pfKen, iNoMasses);

		//printFloats(pfNaomi, iNoMasses);
		//printFloats(pfKen, iNoMasses);

		//play war
		for(int a = 0; a < iNoMasses; a++)
		{
			fNaomi = pfNaomi[a];

			iFoundIndex = getNextGreaterFloatIndex(pfKen, pucKenUsed, fNaomi, iNoMasses, &iKenIndex);

			if( fNaomi > pfKen[iFoundIndex] )
				iNaomiScoreW++;
		}

		//play dwar
		iKenIndex = 0;
		for(int k = 0; k < iNoMasses; k++)
			pucKenUsed[k] = 0;

		for(int a = 0; a < iNoMasses; a++)
		{
			if( a == (iNoMasses-1) )
			{
				getSmallest(pfNaomi, pucNaomiUsed, iNoMasses, &fNaomi, &iNaomiIndex);
				fNaomiDW = fNaomi;
				pucNaomiUsed[iNaomiIndex] = 1;
			}
			else
			{
				getSmallest(pfKen, pucKenUsed, iNoMasses, &fSmall, 0);
				
				if( true == getGreaterThan(pfNaomi, pucNaomiUsed, iNoMasses, fSmall, &fNaomi) )
				{
					if( true == getLargest(pfKen, pucKenUsed, iNoMasses, &fLarge) )
						fNaomiDW = fLarge + 0.000001;
					else
					{
						getSmallest(pfNaomi, pucNaomiUsed, iNoMasses, &fNaomi, &iNaomiIndex);
						fNaomiDW = fNaomi;
						pucNaomiUsed[iNaomiIndex] = 1;
					}
				}
				else
				{
					getSmallest(pfNaomi, pucNaomiUsed, iNoMasses, &fNaomi, &iNaomiIndex);
					fNaomiDW = fNaomi;
					pucNaomiUsed[iNaomiIndex] = 1;
				}
			}

			iFoundIndex = getNextGreaterFloatIndex(pfKen, pucKenUsed, fNaomiDW, iNoMasses, &iKenIndex);

			if( fNaomi > pfKen[iFoundIndex] )
				iNaomiScoreDW++;
		}

		printf("Case #%d: %d %d\n", i+1, iNaomiScoreDW, iNaomiScoreW);
		//printf("\n");

		delete [] pfNaomi;
		delete [] pfKen;
		delete [] pucNaomiUsed;
		delete [] pucKenUsed;
	}

	return 0;
}

