// Lawn.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

void readCRLF(std::ifstream& fin)
{
	//char newline;
	//fin >> newline >> newline;
}

const int BIGINT = 9999;
bool IsPossible(int n, int m, int a[100][100])
{
	for (int i=0; i<n; ++i)
	{
		int smallestRow = BIGINT;
		bool isRowLast = true;
		for (int j=0; j<m; ++j)
		{
			if (a[i][j] < smallestRow)
				smallestRow = a[i][j];
		}
		for (int j=0; j<m; ++j)
		{
			if (a[i][j] != smallestRow)
				isRowLast = false;
		}
		if (isRowLast)
			continue;
		for (int j=0; j<m; ++j)
		{
			bool isColOK = true;
			if (smallestRow == a[i][j])
			{
				int smallestCol = BIGINT;
				for (int k = 0; k<n; ++k)
				{
					if (a[k][j] < smallestCol)
						smallestCol = a[k][j];
				}
				for (int k = 0; k<n; ++k)
				{
					if (a[k][j] != smallestCol)
					{
						isColOK = false;
						return false;
					}
				}
			}
		}
	}
	return true;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin(argv[1], ios::binary);

	int cases = 0;
	fin >> cases;


	for (int i = 0; i<cases; ++i)
	{
		int n = 0, m = 0, a[100][100];
		fin >> n >> m;

		readCRLF(fin);

		bool isOK = false;
		for (int j=0; j<n; ++j)
		{
			for (int k=0; k<m; ++k)
			{
				fin >> a[j][k];
			}
			readCRLF(fin);
		}

		isOK = IsPossible(n, m, a);
		std::cout << "Case #" << i+1 << ": " << (isOK ? "YES" : "NO") << std::endl;

		if (i != cases-1)
			readCRLF(fin);
	}
}

