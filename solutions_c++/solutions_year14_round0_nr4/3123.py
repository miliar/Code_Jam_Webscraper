// MagicTrickGCJ2014.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <iomanip>     
#include <string>

using namespace std;

const int SIZE = 1000;

int warPoints(double naomi[SIZE], double ken[SIZE], int numBlocks);
int deceitfulPoint(double naomi[SIZE], double ken[SIZE], int numBlocks);
void sortArray(double arr[SIZE], int len);
void copyArray(double scr[SIZE], double desc[SIZE], int len);

int _tmain(int argc, _TCHAR* argv[])
{
	double naomi[SIZE];
	double ken[SIZE];
	int testCount, numBlocks;
	int i, j;//
	int DPoint, WPoint;

	ifstream inputfile("D-small-attempt1.IN");
	ofstream outputFile("Output.OUT");

	if (inputfile.is_open() && outputFile.is_open())
	{
		inputfile >> testCount;

		for (i = 0; i < testCount; i++)
		{
			inputfile >> numBlocks;
			for (j = 0; j < numBlocks; j++)
				inputfile >> naomi[j];

			for (j = 0; j < numBlocks; j++)
				inputfile >> ken[j];

			sortArray(naomi, numBlocks);
			sortArray(ken, numBlocks);

			DPoint = deceitfulPoint(naomi, ken, numBlocks);
			WPoint = warPoints(naomi, ken, numBlocks);
			
			outputFile << "Case #" << i + 1 << ": " << DPoint << " " << WPoint << "\n";
		}
	}

	inputfile.close();
	outputFile.close();

	system("PAUSE");

	return 0;
}

int deceitfulPoint(double naomi[SIZE], double ken[SIZE], int numBlocks)
{
	double naomiCpy[SIZE], kenCpy[SIZE];
	int counter(0);
	int i, j, tmpX;

	copyArray(naomi, naomiCpy, numBlocks);
	copyArray(ken, kenCpy, numBlocks);

	tmpX = numBlocks - 1;

	for (i = tmpX; i >= 0; i--)
	{
		if (naomiCpy[i] >  kenCpy[i])
		{
			counter++;
		}
		else
		{
			for (j = 0; j < tmpX; j++)
			{
				naomiCpy[j] = naomiCpy[j + 1];
			}

			tmpX--;
		}
	}

	return counter;
}

int warPoints(double naomi[SIZE], double ken[SIZE], int numBlocks)
{
	double naomiCpy[SIZE], kenCpy[SIZE];
	int counter(0);
	int i, j;
	bool found;
	int tmpX;

	copyArray(naomi, naomiCpy, numBlocks);
	copyArray(ken, kenCpy, numBlocks);

	for (i = 0; i < numBlocks; i++)
	{
		found = false;

		for (j = 0; j < numBlocks && !found; j++)
		{
			if (naomi[i] < ken[j])
			{
				counter++;
				ken[j] = 0.0;
				found = true;
			}
		}
	}

	return (numBlocks - counter);
}

void copyArray(double scr[SIZE], double desc[SIZE], int len)
{

	for (int i = 0; i < len; i++)
	{
		desc[i] = scr[i];
	}
}


void sortArray(double arr[SIZE], int len)
{
	double tmp;
	int i, j;

	for (i = 0; i < len; i++)
	{
		for (j = 0; j < len - 1; j++)
		{
			if (arr[j] > arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
		}
	}
}
