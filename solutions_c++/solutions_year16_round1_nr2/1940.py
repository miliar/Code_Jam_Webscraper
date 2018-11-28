// gcj-a1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdlib.h"
#include "math.h"


int main()
{
	FILE *pFile, *pFileOut;
	pFile = fopen("B-large.in", "rb");
	pFileOut = fopen("out.txt", "wb");
	char N[256] = { 0 };
	short wABN[2501] = {0};
	int nCases = 0, nMatr=0;
	fgets(N, 15, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{		
		fprintf(pFileOut, "Case #%d:", i + 1);
		memset(N, 0, 256);
		memset(wABN, 0, 2*2501);		
		fgets(N, 10, pFile);
		nMatr = atoi(N);
		for (int j = 0; j < (2 * nMatr) - 1; j++)
		{
			int nOffs = 0;
			fgets(N, 256, pFile);
			for (int k = 0; k < nMatr; k++)
			{
				wABN[atoi(N + nOffs)-1]++;
				if (atoi(N + nOffs) >= 10)
					if (atoi(N + nOffs) >= 100)
						if (atoi(N + nOffs) >= 1000)
							nOffs += 5;
						else
							nOffs += 4;
					else
						nOffs += 3;
				else
					nOffs += 2;
			}			
		}
		for (int j = 0; j < 2501; j++)
			if ((wABN[j] % 2 != 0) && (wABN[j] != 0))
				fprintf(pFileOut, " %d", j+1);
		if (i != nCases - 1)
			fprintf(pFileOut, "\n");
	}
	fcloseall();	
    return 0;
}

