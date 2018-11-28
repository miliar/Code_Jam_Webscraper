#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>


int _tmain(int argc, _TCHAR* argv[])
{
	std::wstring inputBuffer;
	std::wifstream infile;
	std::wofstream outFile;
	infile.open("test.in");
	outFile.open(L"output.txt");
	std::wstring line;
	
	int numberOfTestCase = 0;
	infile >> numberOfTestCase;
	std::getline(infile, line);

	for (int i = 0; i < numberOfTestCase; i++)
	{
		std::getline(infile, line);
		std::wistringstream iss(line);
		int nObservation = 0;
		iss >> nObservation;

		int * stock = new int[nObservation];
		//int minEatup = INT_MAX;
		int maxEatup = 0;
		std::getline(infile, line);
		std::wistringstream iss2(line);
		for (int j = 0; j < nObservation; j++)
		{
			iss2 >> stock[j];
			if (j > 0)
			{
				int tmpEatup = stock[j-1] - stock[j];
				if (tmpEatup > maxEatup)
					maxEatup = tmpEatup;
			}
		}

		int nEatup1 = 0;
		int nEatup2 = 0;
		for (int j = 1; j < nObservation; j++)
		{
			int tmpEatup = stock[j-1] - stock[j];
			if (tmpEatup > 0)
			{
				nEatup1 += tmpEatup;
			}
			if (maxEatup > stock[j - 1])
				nEatup2 += stock[j - 1];
			else
				nEatup2 += maxEatup;
		}

		
		int testCase = i+1;
		std::wcout << L"Case #" << testCase << L": " << nEatup1 << L" " << nEatup2 << std::endl;
		outFile << L"Case #" << testCase << L": " << nEatup1 << L" " << nEatup2 << std::endl;

		delete[] stock;

	}
	infile.close();
	outFile.close();
	system("pause");
	return 0;
}