// ConsoleApplication1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	const int numRows = 4;
	const int numColumns = 4;
	int numLoops;
	int firstRow;
	int secondRow;
	int firstRowNums[4];
	int secondRowNums[4];
	int matches;
	int matchingNum;

	in >> numLoops;

	for (int i = 1; i <= numLoops; i++) // Number of times the trick is performed
	{
		in >> firstRow;
		for (int j = 1; j <= numRows; j++) // Number of rows
		{
			for (int k = 0; k < numColumns; k++) // Number of columns
			{
				int number;
				in >> number;
				if (j == firstRow)
				{
					firstRowNums[k] = number;
				}
			}
		}
		in >> secondRow;
		for (int j = 1; j <= numRows; j++) // Number of rows
		{
			for (int k = 0; k < numColumns; k++) // Number of columns
			{
				int number;
				in >> number;
				if (j == secondRow)
				{
					secondRowNums[k] = number;
				}
			}
		}
		matches = 0;
		for (int j = 0; j < numColumns; j++)
		{
			for (int k = 0; k < numColumns; k++)
			{
				if (firstRowNums[j] == secondRowNums[k])
				{
					matches++;
					matchingNum = firstRowNums[j];
				}
			}
		}
		if (matches == 0)
		{
			out << "Case #" << i << ": Volunteer cheated!" << endl;
		}
		else if (matches == 1)
		{
			out << "Case #" << i << ": " << matchingNum << endl;
		}
		else
		{
			out << "Case #" << i << ": Bad magician!" << endl;
		}
	}
	return 0;

}

