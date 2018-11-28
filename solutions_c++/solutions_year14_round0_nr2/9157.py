#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;


// Read next test case from input file, and write solution for it into out file
void SolveTest(ifstream& inFile, ofstream& outFile, int testNum)
{

	double c,f,x;

	double buyTime, curSpeed, waitTime, nextBuy, nextWait, totalTime;


	inFile >> c;
	inFile >> f;
	inFile >> x;

	//n = (f*(x-c)-2*c)/(f*c);

	// 0 farms

	buyTime = 0;
	curSpeed = 2;
    waitTime = x/curSpeed;
	//	totalTime = buyTime + waitTime;


	while (1)
	{
		nextBuy = c/(curSpeed);
		nextWait = x/(curSpeed+f);

		if (waitTime > nextBuy + nextWait)
		{
			// buy next farm
			buyTime += nextBuy;
			curSpeed += f;
			waitTime = nextWait;
		}
		else
		{
			break;
		}
	};

	totalTime = buyTime + waitTime;

	//outFile << "Case #" << testNum << ": N = " << n << "iterations\n";
	outFile << "Case #" << testNum << ": " << totalTime << "\n";
}

int main()
{
	int T;	// number of Test cases
	int i;
	ifstream inFile("in.txt");
	ofstream outFile;
	outFile.open("out.txt"); 

	outFile.precision(7);
	outFile << fixed;
	
	if (!inFile.is_open())
	{
		outFile << "Input file not found!\n";
		outFile.close();
		return 1;
	}

	inFile >> T;	// read number of tests
	for (i = 0; i < T; i++)
	{
		SolveTest(inFile, outFile, i+1);
	}
	outFile.close();

	return 0;
}

