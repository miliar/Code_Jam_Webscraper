// gcj2015_qual.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileIn, *pFileOut;
	char readLine[5000] = {0};
	int nCases = 0, nShyMax, nShyness[1001], nOffset = 0, nNeed = 0, nAud;
	pFileIn = fopen("data.in", "r");
	int ret = fopen_s(&pFileOut, "data.out", "wb");
	fgets(readLine, 10, pFileIn);
	sscanf(readLine, "%d", &nCases);
	for (int i = 0; i < nCases; i++)
	{		
		nOffset = 0;
		nNeed = 0;
		fgets(readLine, 2000, pFileIn);
		sscanf(readLine, "%d", &nShyMax);
		if (nShyMax >= 1000)
				nOffset += 5;
			else if (nShyMax >= 100)
				nOffset += 4;
				else if (nShyMax >= 10)
					nOffset += 3;
					else
						nOffset += 2;		
		for (int j = 0; j < nShyMax+1; j++)
		{			
			sscanf(readLine + nOffset, "%1d", &nShyness[j]);
			nAud = 0;
			for (int k = 0; k <= j; k++)
				nAud += nShyness[k];
			if ((nAud + nNeed) < j+1)
				nNeed += (j+1) - (nAud + nNeed);
			nOffset++;			
		}		
		fprintf(pFileOut, "Case #%d: %d\n", i+1, nNeed);		
	}
	fcloseall();	
	return 0;
}

