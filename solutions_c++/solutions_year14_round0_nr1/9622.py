#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;
ofstream myfile;


void magician(int const firstChoice, int const secondChoice, vector<vector<int> >const &firstGrid, vector<vector<int> >const &secondGrid, int caseCount)
{

	vector<int> result;
	int twoCount = 0;
	int gotChar = -1;
	result.resize(17, 0);


	for (int j = 0; j < 4; j++)
	{
		result[firstGrid[firstChoice - 1][j]]++;
		result[secondGrid[secondChoice - 1][j]]++;
	}


	for (int i = 1; i < 17; i++)
	{
		if (result[i] >= 2)
		{
			twoCount++;
			gotChar = i;
		}

	}
	if (twoCount == 0)
	{
		myfile << "Case #" << caseCount << ": Volunteer cheated!" << endl;
	}
	else if (twoCount == 1)
	{
		myfile << "Case #" << caseCount << ": " << gotChar << endl;
	}
	else
	{
		myfile << "Case #" << caseCount << ": Bad magician!" << endl;
	}

	//cout << "first C:" << firstChoice << endl;
	//
	//for (int i = 0; i < 4; i++)
	//{
	//	for (int j = 0; j < 4; j++)
	//	{
	//		cout << firstGrid[i][j]<<"\t";
	//	}
	//	cout << endl;
	//}
	//cout << "second C:" << secondChoice << endl;
	//for (int i = 0; i < 4; i++)
	//{
	//	for (int j = 0; j < 4; j++)
	//	{
	//		cout << secondGrid[i][j]<<"\t";
	//	}
	//	cout << endl;
	//}
}


int main()
{
	myfile.open("c:\\output.txt");
	int testCase = 0;
	int countForTestCase = 0;
	int firstChoice = 0;
	int secondChoice = 0;
	int const ROW = 4;
	int const COL = 4;
	int const EACH_CASE = 5;
	int n = 0;
	vector<vector<int> > firstGrid;
	vector<vector<int> > secondGrid;

	firstGrid.resize(4);
	secondGrid.resize(4);

	ifstream myfile("c:\\a.txt");

	myfile >> testCase;

	while (countForTestCase < testCase)
	{
		countForTestCase++;
		//read 1st choice and 1st grid
		myfile >> firstChoice;
		for (int i = 0; i < ROW; ++i)
		{
			firstGrid[i].resize(4);
			for (int j = 0; j < COL; ++j)
			{
				myfile >> firstGrid[i][j];
			}
		}

		//read 2nd choice and 2end grid
		myfile >> secondChoice;
		for (int i = 0; i < ROW; ++i)
		{
			secondGrid[i].resize(4);
			for (int j = 0; j < COL; ++j)
			{
				myfile >> secondGrid[i][j];
			}
		}
		magician(firstChoice, secondChoice, firstGrid, secondGrid, countForTestCase);
	}



	cout << testCase << endl;
	system("pause");
}