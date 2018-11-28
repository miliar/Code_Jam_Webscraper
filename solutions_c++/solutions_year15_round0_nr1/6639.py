// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>>
#include <string>

using namespace std;

int standing_ovation(int argc, _TCHAR* argv[])
{
	cout << "Standing Ovation!!\n";
	int iLen = 0;
	int T = 0;
	int itr = 0;
	int cCount = 0;
	int maxSVal = 0;
	int caseOutput = 0;
	int curVal = 0;
	string line, cont;

	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("standing_ovation_input.txt");
	outputFile.open("standing_ovation_output.txt", std::ofstream::out | std::ofstream::trunc);

	if (inputFile.is_open() && outputFile.is_open())
	{
		if (inputFile.good())
		{
			getline(inputFile, line);
			T = stoi(line);

			for(itr = 0; itr < T; itr++)
			{
				cCount = 0;
				caseOutput = 0;
				curVal = 0;
				getline(inputFile, line);

				maxSVal = atoi(&line[0]);
				cout << "Case #" << itr + 1 << endl;
				if (maxSVal == 0)
					caseOutput = 0;
				else
				{
					for (size_t j = 0; j <= maxSVal; j++)
					{
						char curChar = line[j + 2];
						curVal = atoi(&curChar);
						cout << caseOutput << " " << curVal << " " << j << endl;
						if (cCount < j) {
							caseOutput += (j - cCount);
							cCount += (j - cCount);
						}
						cCount += curVal;
					}
				}

				outputFile << "Case #" << itr + 1 << ": " << caseOutput << endl;
			}
		}

	}

	system("pause");
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	return standing_ovation(argc, argv);
}

