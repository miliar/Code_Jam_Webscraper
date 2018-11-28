// magictrk.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct CardsArrgt
{
	int iaRow[4][4];
};

int getNumTCases()
{
	char chBuff[16];
	char *pRet;

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return -1;

	return atoi(chBuff);
}

void readAnsNArrgt(int* piAns, CardsArrgt* pcardArr)
{
	char chBuff[16];
	char *pRet;
	char *pch;

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	*piAns = atoi(chBuff);

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	pch = strtok(chBuff, " ");
	for(int i = 0; i < 4; i++)
	{
		pcardArr->iaRow[0][i] = atoi(pch);
		pch = strtok(NULL, " ");
	}

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	pch = strtok(chBuff, " ");
	for(int i = 0; i < 4; i++)
	{
		pcardArr->iaRow[1][i] = atoi(pch);
		pch = strtok(NULL, " ");
	}

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	pch = strtok(chBuff, " ");
	for(int i = 0; i < 4; i++)
	{
		pcardArr->iaRow[2][i] = atoi(pch);
		pch = strtok(NULL, " ");
	}

	pRet = gets(chBuff); //read line from stdin
	if( NULL == pRet )
		return;

	pch = strtok(chBuff, " ");
	for(int i = 0; i < 4; i++)
	{
		pcardArr->iaRow[3][i] = atoi(pch);
		pch = strtok(NULL, " ");
	}
}

int main(int argc, char* argv[])
{
	int iNoTCases = getNumTCases();
	int iAns1, iAns2;
	CardsArrgt cardArr1, cardArr2;

	for(int i = 0; i < iNoTCases; i++)
	{
		readAnsNArrgt(&iAns1, &cardArr1);
		readAnsNArrgt(&iAns2, &cardArr2);
		int iMatchedNum = 0;
		int iBadMagician = 0;

		for(int a = 0; a < 4; a++)
		{
			int iNumA1 = cardArr1.iaRow[iAns1-1][a];
			for(int b = 0; b < 4; b++)
			{
				if( iNumA1 == cardArr2.iaRow[iAns2-1][b] )
				{
					if( iMatchedNum > 0 )
					{
						iBadMagician = 1;
						break;
					}
					iMatchedNum = iNumA1;
				}
			}

			if( 1 == iBadMagician )
				break;
		}

		//print result
		if( 1 == iBadMagician )
			printf("Case #%d: Bad magician!\n", i+1);
		else if( iMatchedNum > 0 )
			printf("Case #%d: %d\n", i+1, iMatchedNum);
		else
			printf("Case #%d: Volunteer cheated!\n", i+1);
	}

	return 0;
}

