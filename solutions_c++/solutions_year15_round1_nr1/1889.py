#include "stdafx.h"

const char cszInputFileLocation[] = "c:\\temp\\GoogleCodeJam\\GoogleInput.txt";
const char cszOutputFileLocation[] = "c:\\temp\\GoogleCodeJam\\GoogleOutput.txt";

int _tmain(int argc, _TCHAR* argv[])
{
	FILE *pInputFile = NULL;
	FILE *pOutputFile = NULL;
	unsigned long nNumTestCases, nCaseNum;
	unsigned long nNumIntervals, nInterval;
	unsigned long nMinMushEaten, nConstantMushEaten, nRateMushEaten;
	unsigned long nMushrooms[1001];

	if (fopen_s( &pOutputFile, cszOutputFileLocation, "w") != 0)
		return false;
	if (fopen_s( &pInputFile, cszInputFileLocation, "r") != 0)
		return false;
	fscanf(pInputFile, "%d\n", &nNumTestCases);

	for (nCaseNum=1; nCaseNum<=nNumTestCases; nCaseNum++)
	{
		fscanf(pInputFile, "%d\n", &nNumIntervals);
		for (nInterval=0; nInterval<nNumIntervals-1; nInterval++)
			fscanf(pInputFile, "%d ", &nMushrooms[nInterval]);
		fscanf(pInputFile, "%d\n", &nMushrooms[nNumIntervals-1]);

		nMinMushEaten = 0;
		nRateMushEaten = 0;
		for (nInterval=1; nInterval<nNumIntervals; nInterval++)
		{
			if (nMushrooms[nInterval] < nMushrooms[nInterval-1])
			{
				nMinMushEaten += (nMushrooms[nInterval-1] - nMushrooms[nInterval]);
				if (nRateMushEaten < (nMushrooms[nInterval-1] - nMushrooms[nInterval]))
					nRateMushEaten = (nMushrooms[nInterval-1] - nMushrooms[nInterval]);
			}
		}

		nConstantMushEaten = 0;
		for (nInterval=1; nInterval<nNumIntervals; nInterval++)
		{
			if (nMushrooms[nInterval-1] < nRateMushEaten)
				nConstantMushEaten += nMushrooms[nInterval-1];
			else
				nConstantMushEaten += nRateMushEaten;
		}

		fprintf( pOutputFile, "Case #%u: %u %u\n", nCaseNum, nMinMushEaten, nConstantMushEaten);
	}

	fclose( pInputFile);
	fclose( pOutputFile);
	return 0;
}

