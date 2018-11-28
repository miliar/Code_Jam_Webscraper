// CodeJam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

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

			for (itr = 0; itr < T; itr++)
			{
				cCount = 0;
				caseOutput = 0;
				curVal = 0;
				getline(inputFile, line);

				maxSVal = atoi(&line[0]);
				//cout << "Case #" << itr + 1 << endl;
				if (maxSVal == 0)
					caseOutput = 0;
				else
				{
					for (size_t j = 0; j <= maxSVal; j++)
					{
						char curChar = line[j + 2];
						curVal = atoi(&curChar);
						//cout << caseOutput << " " << curVal << " " << j << endl;
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


int infinite_house_of_pancakes(int argc, _TCHAR* argv[])
{
	cout << "Infinite House of Pancakes!!\n";
	int iLen = 0;
	int T = 0;
	int itr = 0;
	int addMinCount = 0;
	int maxDVal = 0;
	int caseOutput = 0;
	int curVal = 0;
	string line, cont, buf;

	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("infinite_house_of_pancakes_input.txt");
	outputFile.open("infinite_house_of_pancakes_output.txt", std::ofstream::out | std::ofstream::trunc);

	if (inputFile.is_open() && outputFile.is_open())
	{
		if (inputFile.good())
		{
			getline(inputFile, line);
			T = stoi(line);

			for (itr = 0; itr < T; itr++)
			{
				addMinCount = 0;
				caseOutput = 0;
				curVal = 0;
				getline(inputFile, line);

				maxDVal = stoi(line);
				cout << "Case #" << itr + 1 << endl;
				if (maxDVal == 0)
					caseOutput = 0;
				else
				{
					getline(inputFile, line);
					std::stringstream ss(line);

					vector<int> panCakes;

					while (ss >> buf)
						panCakes.push_back(stoi(buf));

					for (size_t j = 0; j < maxDVal; j++)
					{
						curVal = panCakes[j];
						cout << "Start" << line << endl << curVal << " " << addMinCount << " " << caseOutput << endl;
						if (curVal > 3) {
							if (curVal == 4) {
								caseOutput += 1;
								if (addMinCount < 2)
									addMinCount = 2;
							}
							else {
								int divVal = curVal / 3;
								if (curVal % 3 == 0)
									divVal--;
								caseOutput += divVal;
								addMinCount = 3;
							}
						}
						else if (addMinCount < 3 && curVal == 3) {
							addMinCount = 3;
						}
						else if (addMinCount < 2 && curVal == 2) {
							addMinCount = 2;
						}
						else if (addMinCount < 1 && curVal == 1) {
							addMinCount = 1;
						}
					}
					caseOutput += addMinCount;
					cout << "End" << line << endl << curVal << " " << addMinCount << " " << caseOutput << endl;
				}

				outputFile << "Case #" << itr + 1 << ": " << caseOutput;
				if (itr < T - 1)
					outputFile << endl;
			}
		}

	}

	system("pause");
	return 0;
}

vector<int> evalCurVal(vector<int> inputVec, int fromIndex, int len)
{
	int convArr[5][5] = { { 0, 1, 2, 3, 4 },
	{ 1, 1, 2, 3, 4 },
	{ 2, 2, -1, 4, -3 },
	{ 3, 3, -4, -1, 2 },
	{ 4, 4, 3, -2, -1 } };

	vector <int> outVector;
	int curVal = inputVec[fromIndex];

	outVector.push_back(inputVec[fromIndex]);
	for (size_t i = fromIndex + 1; i < len; i++)
	{
		if (curVal < 0) {
			curVal = -curVal;
			curVal = convArr[curVal][inputVec[i]];
			curVal = -curVal;
		}
		else {
			curVal = convArr[curVal][inputVec[i]];
		}
		outVector.push_back(curVal);
	}

	return outVector;
}

int dijkstra(int argc, _TCHAR* argv[])
{
	cout << "Dijkstra!!\n";
	int iLen = 0;
	int j = 0;
	int T = 0;
	int itr = 0;
	int L = 0;
	int X = 0;
	int iFound = 0;
	int jFound = 0;
	int kFound = 0;
	int curVal = 0;
	string line, cont, buf;
	int convArr[5][5] = { { 0, 1, 2, 3, 4 },
						{ 1, 1, 2, 3, 4 },
						{ 2, 2, -1, 4, -3 },
						{ 3, 3, -4, -1, 2 },
						{ 4, 4, 3, -2, -1 }};

	ifstream inputFile;
	ofstream outputFile;
	inputFile.open("dijkstra_input.txt");
	outputFile.open("dijkstra_output.txt", std::ofstream::out | std::ofstream::trunc);

	if (inputFile.is_open() && outputFile.is_open())
	{
		if (inputFile.good())
		{
			getline(inputFile, line);
			T = stoi(line);

			for (itr = 0; itr < T; itr++)
			{
				L = 0;
				X = 0;
				iFound = 0;
				jFound = 0;
				kFound = 0;
				curVal = 0;
				getline(inputFile, line);
				std::stringstream ss(line);

				vector<string> LX;

				while (ss >> buf)
					LX.push_back(buf);

				L = stoi(LX[0]);
				X = stoi(LX[1]);
				iLen = L*X;
				cout << "Case #" << itr + 1 << " L : " << L << " X : " << X << endl;
				getline(inputFile, line);
				if (L < 2 || X < 1 || iLen < 3)
					outputFile << "Case #" << itr + 1 << ": NO" << endl;
				else
				{
					vector<int> inputLine;

					for each (char var in line)
					{
						switch (var)
						{
							case 'i':
								inputLine.push_back(2);
								break;
							case 'j':
								inputLine.push_back(3);
								break;
							case 'k':
								inputLine.push_back(4);
								break;
							default:
								break;
						}
					}

					j = 0;
					while (X > 1) {
						for (size_t i = 0; i < L; i++)
						{
							inputLine.push_back(inputLine[i]);
						}
						X--;
					}

					vector <int> iArr;
					curVal = inputLine[0];
					iArr.push_back(inputLine[0]);

					for (int i = 1; i < iLen; i++)
					{
						if (curVal < 0) {
							curVal = -curVal;
							curVal = convArr[curVal][inputLine[i]];
							curVal = -curVal;
						}
						else {
							curVal = convArr[curVal][inputLine[i]];
						}
						iArr.push_back(curVal);
					}

					vector <int> kArr;

					curVal = inputLine[iLen - 1];
					kArr.push_back(inputLine[iLen - 1]);

					for (int i = iLen - 2; i >= 0; i--)
					{
						if (curVal < 0) {
							curVal = -curVal;
							curVal = convArr[inputLine[i]][curVal];
							curVal = -curVal;
						}
						else {
							curVal = convArr[inputLine[i]][curVal];
						}
						kArr.insert(kArr.begin(), curVal);
					}

					int iSize = iArr.size();
					if (iSize > 0) {
						for (size_t i = 0; i < iLen-1; i++)
						{
							if (iArr[i] == 2) {
								vector <int> jArr = evalCurVal(inputLine, i + 1, iLen);
								int jSize = jArr.size();
								if (jSize < 1)
									break;
								for (size_t j = 0; j < jSize; j++)
								{
									if (jArr[j] == 3) {
										if (i + j + 2 < iLen && kArr[i + j + 2] == 4) {
											iFound = 1;
											break;
										}
									}
								}
								if (iFound == 1)
									break;
							}
						}
					}
					if (iFound == 1)
						outputFile << "Case #" << itr + 1 << ": YES";
					else
						outputFile << "Case #" << itr + 1 << ": NO";
					if (itr < T - 1)
						outputFile << endl;
				}

			}
		}

	}

	system("pause");
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	return dijkstra(argc, argv);
}

