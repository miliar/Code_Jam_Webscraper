// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
using namespace std;




int _tmain(int argc, _TCHAR* argv[])
{
	int round;
	ifstream testfile("A-small-attempt1.in");
	testfile >> round;		
	ofstream outputfile("result.out");
	int num[17];
	int firstRow, secondRow;
	for (int i = 1; i <= round; i++)
	{
		memset(num, 0, sizeof(int)* 17);
		testfile >> firstRow;
		int temp;
		for (int row = 0; row < 4; row++)
		{
			for (int col = 0; col < 4; col++)
			{
				testfile >> temp;
				if (row + 1 == firstRow)
					num[temp] = 1;
			}
		}

		testfile >> secondRow;

		int match = 0;
		int matched = -1;
		for (int row = 0; row < 4; row++)
		{
			for (int col = 0; col < 4; col++)
			{
				testfile >> temp;
				if (row + 1 == secondRow)
				{
					if (num[temp] == 1) //
					{
						match++;
						matched = temp;
					}
				}
					
			}
		}

		if (match == 1)
		{
			outputfile << "Case #"<<i <<": "<< matched <<endl;
		}
		else if (match == 0)
		{
			outputfile << "Case #"<<i << ": Volunteer cheated!" << endl;
		}
		else
		{
			outputfile<<"Case #"<<i <<": Bad magician!" << endl;
		}
	}

	testfile.close();
	outputfile.close();
	
}

