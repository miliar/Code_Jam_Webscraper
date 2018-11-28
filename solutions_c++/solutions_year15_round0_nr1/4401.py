// QualifyProblemA3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


const char cszInputFileLocation[] = "c:\\temp\\GoogleCodeJam\\A-large.in";
const char cszOutputFileLocation[] = "c:\\temp\\GoogleCodeJam\\GoogleOutput.txt";

const int kMaxWordsInLanguage=5000; // D
const int kMaxWordSize=15; // L
const int kMaxTestCases=500; // N

int _tmain(int argc, _TCHAR* argv[])
{
	int nWordLen=0; int nNumWordsInLanguage=0; int nNumTestCases=0;
	int i, nCaseNum;
	char aWordsInLanguage[kMaxWordsInLanguage][kMaxWordSize+1];
	char aTestCases[kMaxTestCases][kMaxWordSize+1];
	FILE *pInputFile = NULL;
	FILE *pOutputFile = NULL;
	int nMaxShyness = 0;
	int nGuests = 0;
	int nTotalInAudience = 0;
	int nSubtotal = 0;
	char szPeople[1010];

	if (fopen_s( &pOutputFile, cszOutputFileLocation, "w") != 0)
		return false;
	if (fopen_s( &pInputFile, cszInputFileLocation, "r") != 0)
		return false;
	fscanf(pInputFile, "%d\n", &nNumTestCases);

	for (nCaseNum=1; nCaseNum<=nNumTestCases; nCaseNum++)
	{
		fscanf(pInputFile, "%d %s\n", &nMaxShyness, &szPeople);

		nGuests = 0;
		nTotalInAudience = 0;
		for (i=0; i <= nMaxShyness; i++)
		{
			nSubtotal = szPeople[i] - 48;
			nTotalInAudience += nSubtotal;
			if (nTotalInAudience < (i+1))
			{
				nGuests++;
				nTotalInAudience++;
			}
		}

		fprintf( pOutputFile, "Case #%u: %u\n", nCaseNum, nGuests);
	}

	fclose( pInputFile);
	fclose( pOutputFile);
	return 0;
}