#include "stdafx.h"

const char cszInputFileLocation[] = "c:\\temp\\GoogleCodeJam\\Project1B\\B-small-attempt1.in";
const char cszOutputFileLocation[] = "c:\\temp\\GoogleCodeJam\\Project1B\\GoogleOutput.txt";

CWinApp theApp;
using namespace std;

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nNumTestCases=0;
	unsigned long long ullMaxMachineA=0;
	unsigned long long ullMaxMachineB=0;
	unsigned long long ullTicketsPurchased=0;
	unsigned long long ullPairs=0;
	unsigned long long ullValue;
	unsigned long long i, j;
	int nCaseNum;
	FILE *pInputFile = NULL;
	FILE *pOutputFile = NULL;

	HMODULE hModule = ::GetModuleHandle(NULL);
	AfxWinInit(hModule, NULL, ::GetCommandLine(), 0);

	if (fopen_s( &pOutputFile, cszOutputFileLocation, "w") != 0)
		return false;
	if (fopen_s( &pInputFile, cszInputFileLocation, "r") != 0)
		return false;
	fscanf_s(pInputFile, "%d\n", &nNumTestCases);

	for (nCaseNum=1; nCaseNum<=nNumTestCases; nCaseNum++)
	{
		ullPairs=0;
		fscanf_s(pInputFile, "%llu %llu %llu\n", &ullMaxMachineA, &ullMaxMachineB, &ullTicketsPurchased);
		for (i=0; i < ullMaxMachineA; i++)
		{
			for (j=0; j < ullMaxMachineB; j++)
			{
				ullValue = i & j;
				if (ullValue < ullTicketsPurchased)
				{
					ullPairs++;
				}
			}
		}

		fprintf( pOutputFile, "Case #%u: %llu\n", nCaseNum, ullPairs);
	}

	fclose( pInputFile);
	fclose( pOutputFile);
	return 0;
}
