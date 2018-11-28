// gcj-q.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdlib.h"
#include "math.h"

int main()
{
	FILE *pFile, *pFileOut;
	pFile = fopen("D-small-attempt2.in", "rb");
	pFileOut = fopen("out.txt","wb");	
	char N[256] = { 0 };
	int nCases = 0, nOrigLen = 0, nFoundLev = 0, nTilesOpen = 0;
	fgets(N, 15, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{		
		fgets(N, 15, pFile);
		int nOffset = 0;
		nOrigLen = atoi(N);
		if (nOrigLen >= 10)
			if (nOrigLen >= 100)
			{
				nFoundLev = atoi(N + 3);
				nOffset = 3;
			}
			else
			{
				nFoundLev = atoi(N + 2);
				nOffset = 2;
			}
		else
		{
			nFoundLev = atoi(N + 1);
			nOffset = 1;
		}
		if (nFoundLev >= 10)
			if (nFoundLev >= 100)
				nTilesOpen = atoi(N + nOffset + 1 + 3);
			else
				nTilesOpen = atoi(N + nOffset + 1 + 2);
		else
			nTilesOpen = atoi(N + nOffset + 1 + 1);
		fprintf(pFileOut, "Case #%d:", i+1);
		int nPos = ceil(nOrigLen / 2.0);
		if ((nPos > nTilesOpen) || ((nTilesOpen < nOrigLen) && (nFoundLev == 1)))
			fprintf(pFileOut, "IMPOSSIBLE");
		else
		{
			if (nFoundLev == 1)
			{				
				for (int k = 0; k < nOrigLen; k++)
					fprintf(pFileOut, " %d", k + 1);
			}
			else
				for (int k = 0; k < nPos; k++)
				{
					fprintf(pFileOut, " %d", nOrigLen*(k + 1) - k);
				}
		}
		if (i != nCases - 1)
			fprintf(pFileOut, "\n");
	}
	fcloseall();
    return 0;
}

