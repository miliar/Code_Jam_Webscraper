// gcj-a1.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdlib.h"
#include "math.h"


int main()
{
	FILE *pFile, *pFileOut;
	pFile = fopen("A-large.in", "rb");
	pFileOut = fopen("out.txt", "wb");
	char N[256] = { 0 }, sOut[1000] = {0};
	int nCases = 0;
	fgets(N, 15, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{		
		fprintf(pFileOut, "Case #%d: ", i + 1);		
		int nPos = 0;
		while (1)
		{
			size_t n = fread(N, 1, 1, pFile);
			if (n == 0)
				break;
			if ((N[0] < 65) || (N[0] > 90))
				if (nPos == 0)
					continue;
				else
					break;			
			if (N[0] >= sOut[0])
			{
				for (int j = 0; j < nPos; j++) sOut[nPos - j] = sOut[nPos - j - 1];
				sOut[0] = N[0];
			}
			else
			{
				sOut[nPos] = N[0];
			}
			nPos++;
		}
		for (int j = 0; j < nPos; j++)
			fprintf(pFileOut, "%c", sOut[j]);
		if (i != nCases - 1)
			fprintf(pFileOut, "\n");
	}
	fcloseall();	
    return 0;
}

