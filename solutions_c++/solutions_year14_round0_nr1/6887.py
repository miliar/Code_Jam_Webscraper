#include <iostream>
#include <vector>
#include <stack>
#include <stdio.h>
#include <cstdlib>
#include <fstream>

using namespace std;

class TestClass
{

public:
	int numCases;
	fstream fin;

	int startCardGrid[4][4];
	int endCardGrid[4][4];

	int firstRowArray[4];
	int secondRowArray[4];

	int firstRow, secondRow;
public:
	int matches;
	int foundMatch;

	TestClass()
	{
		numCases = 0;
		fin.open("data.txt", ios::in);
		fin >> numCases;
		fin.get();
	}

	void loadData()
	{
		fin >> firstRow;
		fin.get();

		//cout << firstRow << endl;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> startCardGrid[i][j];
				//cout << startCardGrid[i][j] << " ";
			}
			fin.get();
			//cout << endl;
		}
		fin >> secondRow;
		fin.get();

		//cout << secondRow << endl;

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				fin >> endCardGrid[i][j];
				//cout << endCardGrid[i][j] << " ";
			}
			fin.get();
			// << endl;
		}
		//system("pause");
	}

	int runtest()
	{
		

		for (int i = 0; i < 4; i++)
		{
			firstRowArray[i] = startCardGrid[firstRow - 1][i];
			//cout << firstRowArray[i] << " ";
			secondRowArray[i] = endCardGrid[secondRow - 1][i];
			//cout << secondRowArray[i] << " ";
		}

		

		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (firstRowArray[i] == secondRowArray[j])
				{
					matches++;
					foundMatch = firstRowArray[i];
					//cout << foundMatch << "	";
				}
			}
		}

		//system("pause");

		if (matches == 1)
			return 1;
		if (matches > 1)
			return 2;

		return 0;
	}

	int getMatch()
	{
		return foundMatch;
	}

	int getCases()
	{
		return numCases;

	}

	void reset()
	{
		firstRow = 0;
		secondRow = 0;
		matches = 0;
		foundMatch = 0;
	}
};

int main()
{
	TestClass testClass;

	fstream fout;
	fout.open("dataout.txt", ios::out);

	
	int status = 0;
	

	for (int i = 0; i < testClass.getCases(); i++)
	{
		testClass.loadData();
		status = testClass.runtest();
		
		fout << "Case #" << i + 1 << ": ";
		if (status == 1)
		{
			fout << testClass.getMatch() << endl;
		}
		if (status == 2)
		{
			fout << "Bad magician!" << endl;
		}
		if (status == 0)
		{
			fout << "Volunteer cheated!" << endl;
		}
		testClass.reset();
	}
	return 0;
}