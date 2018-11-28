#include "stdafx.h"
#include <strstream>
#include <iostream>
#include <ctime>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

int getMax(std::vector<int> & plateVector, int & itemIndex)
{
	int maxCake = 0;
	for (int i = 0; i < plateVector.size(); i++)
	{
		int cake = plateVector.at(i);
		if (maxCake < cake)
		{
			maxCake = cake;
			itemIndex = i;
		}
	}
	return maxCake;
}

void recursiveCheck(std::vector<int> & plateVector, int itemIndex, int deliver, int nSpecialMinCnt, int & optVal)
{
	std::vector<int> plateCopy = plateVector;
	plateCopy.push_back(deliver);
	plateCopy[itemIndex] -= deliver;

	nSpecialMinCnt++;
	int newItemIndex = -1;
	int maxCake = getMax(plateCopy, newItemIndex);
	if (nSpecialMinCnt + maxCake <= optVal)
	{
		optVal = nSpecialMinCnt + maxCake;
	}

	for (int i = 2; i <= maxCake/2; i++)
		recursiveCheck(plateCopy, newItemIndex, i, nSpecialMinCnt, optVal);
}

int _tmain(int argc, _TCHAR* argv[])
{
	std::wstring inputBuffer;
	std::wifstream infile;
	infile.open("B-small-attempt4.in");
	std::wstring line;
	
	int numberOfTestCase = 0;
	infile >> numberOfTestCase;
	std::getline(infile, line);

	for (int i = 0; i < numberOfTestCase; i++)
	{
		std::getline(infile, line);
		std::wistringstream iss(line);
		int nDinersWithPlates = 0;
		if (!(iss >> nDinersWithPlates))
			break;

		std::getline(infile, line);
		std::wistringstream issc(line);
		std::vector<int> plates;

		for (int j = 0; j < nDinersWithPlates; j++)
		{
			int nCake = 0;
			issc >> nCake;
			plates.push_back(nCake);
		}

		int itemIndex = -1;
		int maxCake = getMax(plates, itemIndex);
		int optVal = maxCake;
		for (int j = 2; j <= maxCake/2; j++)
		{
			recursiveCheck(plates, itemIndex, j, 0, optVal);
		}

		int testCase = i+1;
		std::wcout << L"Case #" << testCase << L": " << optVal << std::endl;

	}
	infile.close();
	system("pause");
	return 0;
}