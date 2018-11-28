#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>    // std::sort

bool payable(int C, int cost, std::vector<int>& currency)
{
	int remain = cost;
	int D = currency.size();
	for (int i = 0; i < D; i++)
	{
		int pay = currency[D - 1 - i];
		if (pay <= remain)
		{
			for (int j = 0; j < C; j++)
			{
				remain -= pay;
				if (remain < pay)
					break;
			}
		}
	}
	if (remain)	return false;
	return true;
}

int solve(int C, int D, int V, int * currency)
{
	int sol = 0;
	std::vector<int> decomp;
	for (int i = 0; i < D; i++)
		decomp.push_back(currency[i]);

	while (1)
	{
		bool bPayable = true;
		for (int i = 0; i < V; i++)
		{
			int cost = i + 1;
			if (false == payable(C, cost, decomp))
			{
				decomp.push_back(cost);
				std::sort(decomp.begin(), decomp.end());
				bPayable = false;
				break;
			}
		}
		if (true == bPayable)
		{
			sol = decomp.size() - D;
			break;
		}
	}
	return sol;
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::wstring inputBuffer;
	std::wifstream infile;
	std::wofstream outFile;

	std::wstring filePath = L"C:\\Users\\Administrator\\Desktop\\C-small-attempt0.in";
	//std::wstring filePath = L"C:\\Users\\Administrator\\Desktop\\test.in";
	infile.open(filePath);
	outFile.open(filePath + L".txt");
	std::wstring line;

	int numberOfTestCase = 0;
	infile >> numberOfTestCase;
	std::getline(infile, line);

	for (int lCnt = 0; lCnt < numberOfTestCase; lCnt++)
	{
		//	read input
		std::getline(infile, line);
		std::wistringstream iss(line);
		int C = 0, D = 0, V = 0;
		iss >> C >> D >> V;

		int * currency = new int[D];
		std::getline(infile, line);
		std::wistringstream iss2(line);
		for (int i = 0; i < D; i++)
			iss2 >> currency[i];

		int sol = solve(C, D, V, currency);
		delete[] currency;

		//	make output
		int testCase = lCnt + 1;
		std::wcout << L"Case #" << testCase << L": " << sol << std::endl;
		outFile << L"Case #" << testCase << L": " << sol << std::endl;
	}
	infile.close();
	outFile.close();
	system("pause");
	return 0;
}