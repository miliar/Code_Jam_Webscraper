// OACR_SampleProj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "OACR_SampleProj.h"
#include <iostream>
#include <fstream>
using namespace std;

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// Function to solve the problem A: Magician
ifstream fin("C:\\users\\ankulg\\desktop\\GCJ\\Ainput.txt");
ofstream fout("C:\\users\\ankulg\\desktop\\GCJ\\Aoutput.txt");

void Magician()
{
	int T;
	fin >> T;

	for (int iCase = 1; iCase <= T; iCase++)
	{
		fout << "Case #" << iCase << ": ";
		int firstAns;
		int secondAns;
		fin >> firstAns;

		int magic[4][4];
		int firstPossible[4];
		int secondPossible[4];
		int k = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> magic[i][j];
				if (i == firstAns-1)
				{
					firstPossible[k++] = magic[i][j];
				}
			}
		}

		k = 0;
		fin >> secondAns;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> magic[i][j];
				if (i == secondAns-1)
				{
					secondPossible[k++] = magic[i][j];
				}
			}
		}

		int countPoss = 0;
		int possNum = -1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (firstPossible[i] == secondPossible[j])
				{
					countPoss++;
					possNum = firstPossible[i];
				}
			}
		}
		
		if (countPoss == 1)
		{
			fout << possNum << "\n";
		}
		else if (countPoss == 0)
		{
			fout << "Volunteer cheated!\n";
		}
		else
		{
			fout << "Bad magician!\n";
		}
	}
}

int _tmain(int argc, TCHAR* argv[], TCHAR* envp[])
{
	int nRetCode = 0;

	HMODULE hModule = ::GetModuleHandle(NULL);

	if (hModule != NULL)
	{
		// initialize MFC and print and error on failure
		if (!AfxWinInit(hModule, NULL, ::GetCommandLine(), 0))
		{
			// TODO: change error code to suit your needs
			_tprintf(_T("Fatal Error: MFC initialization failed\n"));
			nRetCode = 1;
		}
		else
		{
			// TODO: code your application's behavior here.
			Magician();
		}
	}
	else
	{
		// TODO: change error code to suit your needs
		_tprintf(_T("Fatal Error: GetModuleHandle failed\n"));
		nRetCode = 1;
	}

	return nRetCode;
}
