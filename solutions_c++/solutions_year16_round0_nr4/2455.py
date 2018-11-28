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
	std::wstring fileName = L"D-small-attempt0";
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
		iss.clear();
		iss.str(line);

		int K, C, S;
		iss >> K >> C >> S;

		int * sol = new int[S];
		memset(sol, 0, sizeof(int)*S);
		for (int i = 0; i < S; i++)
			sol[i] = i+1;

		oss << L"Case #" << lCnt + 1 << L": ";//
		for(int i=0; i<S; i++)
			oss << L" " << sol[i];
		oss << std::endl;
		delete[]sol;
	}

	std::wcout << oss.str();
	outFile << oss.str();

	infile.close();
	outFile.close();
	system("pause");
	return 0;
}