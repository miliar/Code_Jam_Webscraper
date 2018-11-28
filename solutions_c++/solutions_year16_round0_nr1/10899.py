// SheepCount.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	int nTestCases = 0;
	int nNumber = 0, nDigit = 0;	
	int nDigitCount[10] = { 0 };
	int nFinalNumber = 0;
	int nTempNumber = 0, nCurNumber = 0;
	char chBuff[20];

	FILE* fInput = NULL;
	fopen_s(&fInput, "E:\\A-large.in", "r");
	if (fInput == NULL) { return (-1); }

	FILE* fOutput = NULL;
	fopen_s(&fOutput, "E:\\A-large.out", "w+");

	memset(chBuff, '\0', 20);
	fgets(chBuff, 20, fInput);

	nTestCases = atoi(chBuff);

	int nOutput[100] = { 0 };

	if (nTestCases < 1 && nTestCases > 100)
	{
		cout << "No of test cases should not exceed 100!" << endl;
		return (-1);
	}

	int i = 1;
	bool bFlag = false;
	for (int krow = 0; krow < nTestCases; krow++)
	{
		memset(chBuff, '\0', 20);
		fgets(chBuff, 20, fInput);
		nNumber = atoi(chBuff);
		nTempNumber = nNumber;
		i = 1;
		for (int irow = 0; irow < 10; irow++)
		{
			nDigitCount[irow] = 0;
		}

		do
		{
			bFlag = false;			
			if (nTempNumber > 0)
			{
				do {
					nDigit = nTempNumber % 10;
					if (nDigitCount[nDigit] == 0) { nDigitCount[nDigit] = 1; }
				} while (nTempNumber /= 10);

				for (int jrow = 0; jrow < 10; jrow++)
				{
					if (!nDigitCount[jrow]) 
					{ 
						bFlag = true; 
						break; 
					}
				}

				if (bFlag) { nTempNumber = (i + 1) * nNumber; nCurNumber = nTempNumber; }
				else { nFinalNumber = nCurNumber; bFlag = false;		}
				i++;
			}
			else
			{
				nOutput[krow] = -1;
				bFlag = false;
			}			
		} while (bFlag);		
		if (nOutput[krow] != -1) { nOutput[krow] = nFinalNumber; }
	}

	for (int krow = 0; krow < nTestCases; krow++)
	{
		fprintf(fOutput, "Case #%d: ", krow + 1);
		if (nOutput[krow] == -1) { fprintf(fOutput, "INSOMNIA\n"); }
		else { fprintf(fOutput, "%d\n", nOutput[krow]); }
	}
    return 0;
}

