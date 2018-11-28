// OACR_SampleProj.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include "OACR_SampleProj.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

// Function to solve the problem A: Magician
ifstream fin("C:\\users\\ankulg\\desktop\\GCJ\\BSmallInput.txt");
ofstream fout("C:\\users\\ankulg\\desktop\\GCJ\\BSmallOutput.txt");

void Cookie()
{
	int T;
	fin >> T;

	for (int iCase = 1; iCase <= T; iCase++)
	{
		fout << "Case #" << iCase << ": ";
		double C, F, X;
		fin >> C >> F >> X;

		double rate = 2.0;
		double ans = 0.0;
		while (true)
		{
			double t1 = (X / rate);
			if (X <= C)
			{
				ans += t1;
				break;
			}
			double t2 = C / rate + X / (F + rate);
			if (t1 < t2 || fabs(t1-t2) <= 1e-7)
			{
				ans += t1;
				break;
			}
			ans += C / rate;
			rate += F;
		}
		fout << fixed;
		fout << std::setprecision(7);
		fout << ans << "\n";
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
			Cookie();
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
