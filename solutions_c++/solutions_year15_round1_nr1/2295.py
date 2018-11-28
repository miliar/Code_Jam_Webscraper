/**
* File:		Round01a_ProbA.cpp
* Title:	Google Code Jam 2015 - Round 1A - Problem A - Mushroom Monster
* Author:	R.Quatrefoil
* Date:		2015-04-17
* Purpose:
* Notes:	Created using Microsoft Visual Studio 2013
*
*			First Method:	if next number is less than current number then eat the difference
*							if next number is greater than current number then eat nothing
*							running total of all eaten
*
*			Second Method:	Find the biggest difference between 2 consecutive number
*							Then go through every number
*							And either eat the maxDifference or the entire stack, whichever is smaller
*/

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream iFile("Round01A_ProbA_Input.txt", ios::in);
	ofstream oFile;		//will only open if iFile opens correctly

	int testCasesTotal = 0;		//total number of test cases to evaluate (from 1 to 1000)
	long long firstMushroomsEaten = 0;
	long long secondMushroomsEaten = 0;
	int numEats = 0;
	vector<int> mushroomList;
	int secondMaxEats = 0;
	int mushroomDifference = 0;

	if (iFile)
	{
		oFile.open("Round01A_ProbA_Output.txt", ios::out | ios::trunc);

		iFile >> testCasesTotal;
		for (int currCase = 0; currCase < testCasesTotal; currCase++)		//evaluate all test cases
		{
			//reinit variables
			firstMushroomsEaten = 0;
			secondMushroomsEaten = 0;
			//could store iFile.tellg(); and then use iFile.seekg(ios::beg, 0);
			mushroomList.clear();
			numEats = 0;
			secondMaxEats = 0;
			mushroomDifference = 0;

			iFile >> numEats;
			mushroomList.resize(numEats);

			//numEats guaranteed to be 2 or larger
			iFile >> mushroomList[0];

			for (int eat = 1; eat < numEats; eat++)
			{
				iFile >> mushroomList[eat];

				mushroomDifference = mushroomList[eat - 1] - mushroomList[eat];

				//find mushrooms eaten in first method
				if (mushroomDifference > 0)
				{
					firstMushroomsEaten += mushroomList[eat - 1] - mushroomList[eat];
				}

				//find max eaten (the rate per 10 seconds) in second method
				if (mushroomDifference > secondMaxEats)
				{
					secondMaxEats = mushroomDifference;
				}
			}

			//find mushrooms eaten in second method
			for (int eat = 0; eat < (numEats - 1); eat++)
			{
				if (secondMaxEats < mushroomList[eat])
				{
					secondMushroomsEaten += secondMaxEats;
				}
				else
				{
					secondMushroomsEaten += mushroomList[eat];
				}
			}

			//output case to file
			oFile << "Case #" << (currCase + 1) << ": " << firstMushroomsEaten << " " << secondMushroomsEaten << endl;
		}

		iFile.close();
		oFile.close();
		cout << "Output successful!!" << endl;
	}
	else
	{
		cout << "Error opening input file!!" << endl;
	}

	cout << endl << endl << "Press Enter key to continue..." << endl;
	cin.get();
	return 0;
}//endfcn main