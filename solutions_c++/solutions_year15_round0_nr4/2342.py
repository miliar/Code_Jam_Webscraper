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
	infile.open("D-small-attempt3.in");
	std::wstring line;
	
	int numberOfTestCase = 0;
	infile >> numberOfTestCase;
	std::getline(infile, line);

	const wchar_t * winner[] = {L"RICHARD", L"GABRIEL"};
	for (int i = 0; i < numberOfTestCase; i++)
	{
		std::getline(infile, line);
		std::wistringstream iss(line);
		int nRows = 0;
		int nCols = 0;
		int nBlock = 0;
		if (!(iss >> nBlock >> nRows >> nCols))
			break;
		
		int sol = -1;
		if ((nRows*nCols) % nBlock)
			sol = 0;

		else
		{
			if (nBlock == 1)
			{
				sol = 1;
			}
			else if (nBlock == 2)
			{
				sol = 1;
			}
			else if (nBlock == 3)
			{
				if (nRows <= 1 || nCols <= 1)
					sol = 0;
				else
					sol = 1;
			}
			else if( nBlock == 4)
			{
				if (nRows < 3 || nCols < 3)
					sol = 0;
				else
					sol = 1;
			}
		}

		int testCase = i+1;
		std::wcout << L"Case #" << testCase << L": " << winner[sol] << std::endl;

	}
	infile.close();
	system("pause");
	return 0;
}