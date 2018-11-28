#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <math.h>
#include <iomanip>

using namespace std;


class TestClass
{

public:
	int numCases;
	fstream fin;

	const float INITIALRATE = 2;

	// input variables
	double farmCost, targetCookies, farmRate;

	// findBestTime variables
	double currentRate, currentCookies;
	double residualTime, farmInterval, farmTime, totalTime, oldTotalTime;
	int counter;


	TestClass()
	{
		numCases = 0;
		fin.open("data.txt", ios::in);
		fin >> numCases;
		fin.get();
		currentRate = INITIALRATE;

	}

	void loadData()
	{
		fin >> farmCost >> farmRate >> targetCookies;
		fin.get();
	}

	void initializeData()
	{
		currentRate = INITIALRATE;
		currentCookies = 0;
		residualTime = 0; 
		farmInterval = 0; 
		farmTime = 0; 
		totalTime = 0; 
		oldTotalTime = targetCookies / INITIALRATE;
	}

	double runtest()
	{
		return bestTime();
	}

	double bestTime()
	{
		farmInterval = (farmCost / currentRate);
		currentRate += farmRate;
		farmTime = farmTime + farmInterval;
		residualTime = (targetCookies / currentRate);

		totalTime = farmTime + residualTime;

		//cout << "oldTotalTime		" << oldTotalTime << endl;
		////cout << "farmTime		" << farmTime << endl;
		//cout << "totalTime		" << setprecision(9) << totalTime << endl;
		//cout << "residualTime		" << setprecision(9) << residualTime << endl;
		//cout << "currentRate		" << currentRate << endl;
		//system("pause");


		if (oldTotalTime <= totalTime)
			return oldTotalTime;

		oldTotalTime = totalTime;

		bestTime();
	}

	int getCases()
	{
		return numCases;
	}

	void reset()
	{
		currentRate = 0; 
		currentCookies = 0;
		residualTime = 0; 
		farmInterval = 0; 
		farmTime = 0; 
		totalTime = 0; 
		oldTotalTime = 0;
	}
};

int main()
{
	TestClass testClass;

	fstream fout;
	fout.open("dataout.txt", ios::out);

	for (int i = 0; i < testClass.getCases(); i++)
	{
		testClass.loadData();
		testClass.initializeData();

		fout << "Case #" << i + 1 << ": ";

		fout << setprecision(10) << testClass.runtest() << endl;

		testClass.reset();
	}
	return 0;
}