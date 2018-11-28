#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

//	qualification round
//	problem b - revenge of the pancakes
int main()
{
	std::wifstream infile;
	std::wofstream outFile;
	std::wistringstream iss;
	std::wostringstream oss;
	std::wstring line;

	std::wstring folderPath = L"data\\";
	std::wstring fileName = L"B-small-attempt0";
	infile.open(folderPath + fileName + L".in");
	outFile.open(folderPath + fileName + L".out.txt");

	int TotalCase = 0;
	std::getline(infile, line);
	iss.str(line);
	iss >> TotalCase;

	for (int lCnt = 0; lCnt < TotalCase; lCnt++)
	{
		//	read input
		std::getline(infile, line);

		int size = line.length();
		int * hts = new int[size];
		for (int i = size - 1; i >= 0; i--)
		{
			if (line[i] == '+')
				hts[i] = 1;
			else
				hts[i] = 0;
		}

		//	solve
		int sol = 0;
		for (int i = size - 1; i >= 0; i--)
		{
			if (hts[i] == 0)
			{
				for (int j = i; j >= 0; j--)
					hts[j] = 1 - hts[j];
				sol++;
			}
		}
		
		delete[] hts;

		//	make output
		std::wostringstream oss;
		oss << L"Case #" << lCnt + 1 << L": " << sol << std::endl;

		std::wcout << oss.str();
		outFile << oss.str();
	}

	infile.close();
	outFile.close();
	system("pause");
	return 0;
}