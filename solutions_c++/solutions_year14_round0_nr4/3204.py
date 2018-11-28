
#include <math.h>
#include <iostream>
#include <vector>
#include <set>
#include <fstream>
#include <string>
#include <algorithm>
#include <iterator>

using namespace std;

typedef set<double> tDataSet;

struct InputData
{
	tDataSet naomiSet;
	tDataSet kenSet;
};

double optimalChoise(double iWeight, tDataSet& ioSet)
{
	// Select the first value bigger than iWeight. Set is ordered so the first should be the best. 
	// If it does not exist, select the smallest value.
	
	double res = *ioSet.begin();
	for (tDataSet::iterator it = ioSet.begin(); it != ioSet.end(); ++it)
	{
		if (*it > iWeight)
		{
			res = *it;
			break;
		}
	}

	ioSet.erase(res);

	return res;
}

void solve(const InputData& iData, int& oDWar, int& oWar)
{
	oWar = 0;
	oDWar = 0;
	tDataSet naomiSet = iData.naomiSet;
	tDataSet kenSet = iData.kenSet;

	// war
	for (tDataSet::iterator it = naomiSet.begin(); it != naomiSet.end(); )
	{
		double naomiWeight = *it;
		naomiSet.erase(it++);
		double kenWeight = optimalChoise(naomiWeight, kenSet);
		if (naomiWeight > kenWeight)
			++oWar;
	}

	naomiSet = iData.naomiSet;
	kenSet = iData.kenSet;

	// Deceitful War
	for (tDataSet::reverse_iterator it = naomiSet.rbegin(); it != naomiSet.rend(); )
	{
		double naomiWeightDeclared = *it;
		double kenWeight = optimalChoise(naomiWeightDeclared, kenSet);
		double naomiWeight = optimalChoise(kenWeight, naomiSet);
		if (naomiWeight > kenWeight)
			++oDWar;
		it = naomiSet.rbegin();
	}
}

void inputSet(ifstream& inFile, int size, tDataSet& oSet)
{
	for (int j = 0; j < size; ++j)
	{
		double weight;
		inFile >> weight;
		oSet.insert(weight);
	}
}

int main()
{
	ifstream inFile ("input.txt");

	if (!inFile.is_open())
		return 1;

	int numCases;
	inFile>>numCases;

	vector<InputData> inputDataVec;
	inputDataVec.resize(numCases);

	for (int i = 0; i < numCases; ++i)
	{
		int sz;
		inFile >> sz;

		inputSet(inFile, sz, inputDataVec[i].naomiSet);
		inputSet(inFile, sz, inputDataVec[i].kenSet);
	}

	ofstream outFile;
	outFile.open("output.txt");

	outFile.setf( std::ios::fixed, std:: ios::floatfield );
	outFile.precision(7);

	for (int i = 0; i < numCases; ++i)
	{
		InputData& data = inputDataVec[i];
		int dWar, war;
		solve(data, dWar, war);
		outFile << "Case #" << i+1 << ": " << dWar << " " << war << endl;
	}

	outFile.close();

	return 0;
}