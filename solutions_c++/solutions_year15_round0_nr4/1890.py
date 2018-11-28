// gcj2015_qual.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pFileIn, *pFileOut;
	char readLine[5000] = {0}, bWin[8] = "NO";
	int nCases = 0, nDimension, nCols, nRows, nOffset;
	pFileIn = fopen("data.in", "r");
	int ret = fopen_s(&pFileOut, "data.out", "wb");
	fgets(readLine, 10, pFileIn);
	sscanf(readLine, "%d", &nCases);
	for (int i = 0; i < nCases; i++)
	{		
		nOffset = 0;
		fgets(readLine, 500, pFileIn);
		sscanf(readLine, "%d", &nDimension);
		if (nDimension >= 1000)
				nOffset += 5;
			else if (nDimension >= 100)
				nOffset += 4;
				else if (nDimension >= 10)
					nOffset += 3;
					else
						nOffset += 2;
		sscanf(readLine + nOffset, "%d", &nRows);
		if (nRows >= 1000)
				nOffset += 5;
			else if (nRows >= 100)
				nOffset += 4;
				else if (nRows >= 10)
					nOffset += 3;
					else
						nOffset += 2;
		sscanf(readLine + nOffset, "%d", &nCols);		
		if ((((nCols*nRows)%nDimension) != 0)||((nCols*nRows) == nDimension)||(nDimension >= 7)||((nCols*nRows) == 2*nDimension))
			sprintf(bWin, "RICHARD");
		else
			sprintf(bWin, "GABRIEL");
		if ((nCols == 1) && (nRows == 1) && (nDimension == 1))
			sprintf(bWin, "GABRIEL");
		if ((nCols*nRows == 2)&&((nDimension == 2)||(nDimension == 1)))
			sprintf(bWin, "GABRIEL");
		if ((nCols*nRows == 4)&&(nDimension == 2))
			sprintf(bWin, "GABRIEL");
		if ((nCols*nRows == 6)&&(nDimension == 3))
			sprintf(bWin, "GABRIEL");
		fprintf(pFileOut, "Case #%d: %s\n", i+1, bWin);
	}
	fcloseall();	
	return 0;
}

