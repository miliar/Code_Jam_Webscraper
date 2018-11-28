#include "stdafx.h"

const char cszInputFileLocation[] = "c:\\temp\\GoogleCodeJam\\C-small-attempt0.in";
const char cszOutputFileLocation[] = "c:\\temp\\GoogleCodeJam\\GoogleOutput.txt";

const int kNegI='m';
const int kNegJ='n';
const int kNegK='o';
const int kNegOne='p';

int nRepeatedTotal, nPhraseLen;
int nRepeatIdx, nStartIdx;
char szPhrase[10002];

void multiply( char ch1, char ch2, char &chOut, bool &bNeg)
{
	if (ch1 == 1)
		chOut = ch2; // bNeg stays the same
	else if (ch2 == 1)
		chOut = ch1; // bNeg stays the same
	else if (ch1 == ch2)
	{
		chOut = 1;
		bNeg = !bNeg;
	}
	else if ((ch1 == 'i') && (ch2 == 'j'))
		chOut = 'k';
	else if ((ch1 == 'i') && (ch2 == 'k'))
	{
		chOut ='j';
		bNeg = !bNeg;
	}
	else if ((ch1 == 'j') && (ch2 == 'i'))
	{
		chOut ='k';
		bNeg = !bNeg;
	}
	else if ((ch1 == 'j') && (ch2 == 'k'))
		chOut = 'i';
	else if ((ch1 == 'k') && (ch2 == 'i'))
		chOut = 'j';
	else if ((ch1 == 'k') && (ch2 == 'j'))
	{
		chOut ='i';
		bNeg = !bNeg;
	}
}

bool multipyUntilLetterFound( char cDesiredChar, char cStartingChar)
{
	if (nStartIdx >= nPhraseLen)
	{
		// we're at the end of the phrase, so repeat
		nStartIdx = 0;
		nRepeatIdx++;
	}
	if (nRepeatIdx >= nRepeatedTotal)
		return false; // we have run out of letters to multiply

	char chOut = cStartingChar;
	bool bNeg = false;
	bool bDone = false;

	while (!bDone)
	{
		multiply( chOut, szPhrase[nStartIdx], chOut, bNeg);

		nStartIdx++; // go to the next letter in the phrase
		if (nStartIdx >= nPhraseLen)
		{
			// we're at the end of the phrase, so repeat
			nStartIdx = 0;
			nRepeatIdx++;
		}

		if ((chOut == cDesiredChar) && (bNeg == false))
			return true; // we have a match

		if (nRepeatIdx >= nRepeatedTotal)
			return false; // we have run out of letters to multiply
	}

	return false; // should never reach here
}

bool PossibleToGetK()
{
	if (nStartIdx >= nPhraseLen)
	{
		// we're at the end of the phrase, so repeat
		nStartIdx = 0;
		nRepeatIdx++;
	}
	if (nRepeatIdx >= nRepeatedTotal)
		return false; // we have run out of letters to multiply

	char chOut = 1;
	bool bNeg = false;
	bool bDone = false;

	while (!bDone)
	{
		multiply( chOut, szPhrase[nStartIdx], chOut, bNeg);

		nStartIdx++; // go to the next letter in the phrase
		if (nStartIdx >= nPhraseLen)
		{
			// we're at the end of the phrase, so repeat
			nStartIdx = 0;
			nRepeatIdx++;
		}

		if (nRepeatIdx >= nRepeatedTotal)
			bDone = true; // we have run out of letters to multiply, so time to exit
	}

	if ((chOut == 'k') && (bNeg == false))
		return true; // we have a match for 'K'

	return false; // unable to find "K" given these "IJ" substrings
}

bool PossibleToGetJK()
{
	bool bDone = false;
	char cStartChar = 1;
	while (!bDone)
	{
		if (!multipyUntilLetterFound( 'j', cStartChar))
			bDone = true; // couldn't do it
		else
		{
			int nRepeatIdxSaved = nRepeatIdx;
			int nStartIdxSaved = nStartIdx;
			
			if (PossibleToGetK())
				return true;
			else
			{
				cStartChar = 'j';
				nRepeatIdx = nRepeatIdxSaved;
				nStartIdx = nStartIdxSaved;
			}
		}
	}

	return false; // unable to find "JK" given this "I" substring
}

bool PossibleToSolve()
{
	nRepeatIdx = 0;
	nStartIdx = 0;
	bool bDone = false;
	char cStartChar = 1;
	while (!bDone)
	{
		if (!multipyUntilLetterFound( 'i', cStartChar))
			bDone = true; // couldn't do it
		else
		{
			int nRepeatIdxSaved = nRepeatIdx;
			int nStartIdxSaved = nStartIdx;
			
			if (PossibleToGetJK())
				return true;
			else
			{
				cStartChar = 'i';
				nRepeatIdx = nRepeatIdxSaved;
				nStartIdx = nStartIdxSaved;
			}
		}
	}

	return false; // unable to solve
}

int _tmain(int argc, _TCHAR* argv[])
{
	int nNumTestCases=0;
	int nCaseNum;
	FILE *pInputFile = NULL;
	FILE *pOutputFile = NULL;

	if (fopen_s( &pOutputFile, cszOutputFileLocation, "w") != 0)
		return false;
	if (fopen_s( &pInputFile, cszInputFileLocation, "r") != 0)
		return false;
	fscanf(pInputFile, "%d\n", &nNumTestCases);

	bool bPossible = false;

	for (nCaseNum=1; nCaseNum<=nNumTestCases; nCaseNum++)
	{
		fscanf(pInputFile, "%d %d\n", &nPhraseLen, &nRepeatedTotal);
		fscanf(pInputFile, "%s\n", &szPhrase);
		bPossible = false;

		if (nPhraseLen == 1)
			bPossible = false; // cannot get enough variations to get all three letters
		else if (nPhraseLen*nRepeatedTotal < 3)
			bPossible = false; // not enough letters to split into three groups
		else
			bPossible = PossibleToSolve();

		if (bPossible)
			fprintf( pOutputFile, "Case #%u: YES\n", nCaseNum);
		else
			fprintf( pOutputFile, "Case #%u: NO\n", nCaseNum);
		//fprintf( pOutputFile, "Case #%u: %u %s\n", nCaseNum, nRepeatedTotal, szPhrase);
	}

	fclose( pInputFile);
	fclose( pOutputFile);
	return 0;
}
