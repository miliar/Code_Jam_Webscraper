// gcj-q.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include "stdlib.h"


int main()
{
	FILE *pFile, *pFileOut;
	pFile = fopen("B-large.in", "rb");
	pFileOut = fopen("out.txt","wb");	
	char N[4] = { 0 };
	int nCases, pncGroups = 0, j = 0;
	bool isPlus = 0;
	fgets(N, 4, pFile);
	nCases = atoi(N);
	for (int i = 0; i < nCases; i++)
	{
		j = 0;
		pncGroups = 0;
		isPlus = false;
		N[1] = 0;
		while (1)
		{
			fread(N, 1, 1, pFile);
			if (feof(pFile))
				break;
			if ((N[0] != '+') && (N[0] != '-'))
				if (j == 0)
					continue;
				else
					break;
			if (N[1] != N[0])
				pncGroups++;
			N[1] = N[0];
			if (N[0] == '+')
				isPlus = true;
			else
				isPlus = false;
			j++;
		}
		if (!isPlus)
			pncGroups++;
		fprintf(pFileOut, "Case #%d: %d", i + 1, pncGroups-1);
		if (i != nCases - 1)
			fprintf(pFileOut, "\n");
	}
	fcloseall();
    return 0;
}

