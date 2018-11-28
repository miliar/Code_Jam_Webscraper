// gcj-1c.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdlib.h"
#include "math.h"


int main()
{
	FILE *pFile, *pFileOut;
	pFile = fopen("A-large.in", "rb");
	pFileOut = fopen("out.txt", "wb");
	char N[256] = { 0 };
	int nCases = 0, nParties = 0, nSenators[26] = {0};
	fgets(N, 15, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{
		fprintf(pFileOut, "Case #%d: ", i + 1);
		fgets(N, 15, pFile);
		nParties = atoi(N);
		memset(nSenators, 0, 26 * 4);
		fgets(N, 256, pFile);
		int nOffset = 0;
		int nSum = 0;
		for (int j = 0; j < nParties; j++)
		{
			nSenators[j] = atoi(N + nOffset);
			nSum += nSenators[j];
			if (nSenators[j] >= 10)
				if (nSenators[j] >= 100)
					if (nSenators[j] >= 1000)
						nOffset += 5;
					else
						nOffset += 4;
				else
					nOffset += 3;
			else
				nOffset += 2;
		}		
		while (true)
		{
			int nMax = 0, nMax2 = 0;
			int nNumEv = -1, nNumEv2 = -1;
			for (int j = 0; j < nParties; j++)
				if (nSenators[j] > nMax)
				{
					nNumEv = j;
					nMax = nSenators[j];
				}
			if (nNumEv < 0)
				break;
			for (int j = 0; j < nParties; j++)
				if ((nSenators[j] > nMax2) && (j != nNumEv))
				{
					nNumEv2 = j;
					nMax2 = nSenators[j];
				}
			if (nSum == 3)
			{
				if (nSenators[nNumEv] > nSenators[nNumEv2])
					nNumEv2 = -1;
				else
				{
					nNumEv = nNumEv2;
					nNumEv2 = -1;
				}
			}
			if (nNumEv2 >= 0)
			{
				if (nSenators[nNumEv] - nSenators[nNumEv2] >= 2)
					nNumEv2 = nNumEv;
				nSenators[nNumEv2]--;
				nSum--;
			}
			nSenators[nNumEv]--;
			nSum--;
			if (nNumEv2 >= 0)
				fprintf(pFileOut, "%c%c ", nNumEv + 65, nNumEv2 + 65);
			else
				fprintf(pFileOut, "%c ", nNumEv + 65);
		}
		if (i != nCases - 1)
			fprintf(pFileOut, "\n");
	}
	fcloseall();
	return 0;
}

