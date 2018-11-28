#include "stdafx.h"


const char cszInputFileLocation[] = "c:\\temp\\GoogleCodeJam\\D-small-attempt1.in";
const char cszOutputFileLocation[] = "c:\\temp\\GoogleCodeJam\\GoogleOutput.txt";


int _tmain(int argc, _TCHAR* argv[])
{
	int nNumTestCases=0;
	int nCaseNum;
	FILE *pInputFile = NULL;
	FILE *pOutputFile = NULL;
	int nOminoSides, nRows, nCols;
	bool bPossible;

	if (fopen_s( &pOutputFile, cszOutputFileLocation, "w") != 0)
		return false;
	if (fopen_s( &pInputFile, cszInputFileLocation, "r") != 0)
		return false;
	fscanf(pInputFile, "%d\n", &nNumTestCases);

	for (nCaseNum=1; nCaseNum<=nNumTestCases; nCaseNum++)
	{
		fscanf(pInputFile, "%d %d %d\n", &nOminoSides, &nRows, &nCols);
		bPossible = true;

		// Are the total squares divisible by the blocks in one omino?
		int nTotalSquares = nRows*nCols;
		int nOminoNumberPieces = nTotalSquares / nOminoSides;
		if (nTotalSquares != nOminoNumberPieces * nOminoSides)
			bPossible = false;

		// If I pick a straight line omino, it must be able to fit in one row or one col
		if ( (nOminoSides > nRows) && (nOminoSides > nCols) )
			bPossible = false;

		// If I pick a staircase omino, it must have rows & cols to fit
		int nMax1 = (nOminoSides+1)/2;
		int nMax2 = (nOminoSides+1) - nMax1;
		if ((nMax1 > nRows) || (nMax1 > nCols))
			bPossible = false;
		else if ((nMax1 == nRows) && (nMax2 > nCols))
			bPossible = false;
		else if ((nMax1 == nCols) && (nMax2 > nRows))
			bPossible = false;

		// It must also leave room to wrap into open spaces
		if (nOminoSides > 3)
		{
			if ((nMax1 == nRows) || (nMax1 == nCols))
			{
				if (nOminoNumberPieces < nOminoSides*3)
					bPossible = false;
			}
		}

		if (bPossible)
			fprintf( pOutputFile, "Case #%u: GABRIEL\n", nCaseNum);
		else
			fprintf( pOutputFile, "Case #%u: RICHARD\n", nCaseNum);
	}

	fclose( pInputFile);
	fclose( pOutputFile);
	return 0;
}
