// Lawn.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <fstream>
using namespace std;

ifstream infile("B-large.in");
ofstream outfile("output.txt");

void readLawn(int **lawn, int rows, int cols)
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			infile >> lawn[i][j];
		}
	}
}

void solveLawn(int **lawn, int rows, int cols)
{
	int *rowmaxs = new int[rows]; 
	int *colmaxs = new int[cols];


	for (int i = 0; i < rows; i++)
	{
		rowmaxs[i] = -1;
	}

	for (int i = 0; i < cols; i++)
	{
		colmaxs[i] = -1;
	}

	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			if (lawn[i][j] > rowmaxs[i])
			{
				rowmaxs[i] = lawn[i][j];
			}
			if (lawn[i][j] > colmaxs[j])
			{
				colmaxs[j] = lawn[i][j];
			}
		}
	}
	bool possible = true;
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			if (rowmaxs[i] != lawn[i][j] && colmaxs[j] != lawn[i][j])
			{
				possible = false;
			}
		}
	}
	if (possible)
	{
		outfile << "YES" << endl;
	} 
	else
	{
		outfile << "NO" << endl;
	}

	delete rowmaxs;
	delete colmaxs;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int caseNum;
	infile >> caseNum;

	for (int i = 0; i < caseNum; i++)
	{
		int rows, cols;
		infile >> rows >> cols;
		int **lawn = new int *[rows];
		for (int j = 0; j < rows; j++)
		{
			lawn[j] = new int[cols];
		}
		readLawn(lawn, rows, cols);
		outfile << "Case #" << i+1 << ": ";
		solveLawn(lawn, rows, cols);
		for (int j = 0; j < rows; j++)
		{
			delete lawn[j];
			lawn[j] = nullptr; 
		}
		delete *lawn;
		lawn = nullptr;
	}

	infile.close();
	outfile.close();
	return 0;
}

