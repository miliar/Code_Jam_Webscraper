// MagicTrickGCJ2014.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
const int SIZE = 4;

string solveMagic(int firstAns, int firstCards[SIZE][SIZE], int secondAns, int secondCards[SIZE][SIZE]);

int _tmain(int argc, _TCHAR* argv[])
{
	int testCount;//number of test cases
	int firstCards[SIZE][SIZE], secondCards[SIZE][SIZE];//first and second card arrangement
	int firstAns, secondAns; // first and second answer
	int i, j, k;//index of elements
	string answer;
	
	ifstream inputfile("A-small-attempt0.IN");
	ofstream outputFile("Output.OUT");
	
	if (inputfile.is_open() && outputFile.is_open())
	{
		inputfile >> testCount;

		for (i = 0; i < testCount; i++)
		{
			inputfile >> firstAns;

			for (j = 0; j < SIZE; j++)
			{
				for (k = 0; k < SIZE; k++)
				{
					inputfile >> firstCards[j][k];
				}
			}
			
			inputfile >> secondAns;

			for (j = 0; j < SIZE; j++)
			{
				for (k = 0; k < SIZE; k++)
				{
					inputfile >> secondCards[j][k];
				}
			}

			outputFile << "Case #" << i + 1 << ": " << solveMagic(firstAns, firstCards, secondAns, secondCards) << "\n";
		}
	}

	inputfile.close();
	outputFile.close();
	
	system("PAUSE");
	
	return 0;
}

string solveMagic(int firstAns, int firstCards[SIZE][SIZE], int secondAns, int secondCards[SIZE][SIZE])
{
	int counter = 0;
	int tmp;
	int magicNumer;
	int i, j;
	char *intStr;

	for (i = 0; i < SIZE; i++)
	{
		tmp = firstCards[firstAns - 1][i];
		
		for ( j = 0; j < SIZE; j++)
		{
			if (tmp == secondCards[secondAns - 1][j])
			{
				counter++;
				magicNumer = tmp;
			}
		}
	}

	if (counter == 1)
		return to_string(magicNumer);
	if (counter > 1)
		return "Bad magician!";
	else
		return "Volunteer cheated!";
}