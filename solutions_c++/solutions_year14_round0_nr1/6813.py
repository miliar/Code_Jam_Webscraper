// MagicTrick.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

using namespace std;

const int N = 4;

typedef int CardsGrid[N][N];

void ReadGrid(istream *input, CardsGrid grid)
{
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < N; ++j)
		{
			*input >> grid[i][j];
		}
}

const int BadMagician = -1;
const int MagicianCheated = 0;

int Solve(int row1, CardsGrid grid1, int row2, CardsGrid grid2)
{
	int twoRows[N*2];
	copy(grid1[row1-1], grid1[row1-1] + N, twoRows);
	copy(grid2[row2-1], grid2[row2-1] + N, twoRows + N);
	sort(twoRows, twoRows + N * 2);
	int similar = MagicianCheated;
	for (int i = 0; i < N * 2 - 1; ++i)
	{
		if (twoRows[i] == twoRows[i + 1])
		{
			if (similar > 0)
			{
				return BadMagician;
			}
			similar = twoRows[i];
		}
	}
	return similar;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream inputFile("A-small-attempt0.in");
	if (!inputFile.is_open())
	{
		cerr << "Error reading file" << endl;
		return 1;
	}

	int T;
	inputFile >> T;
	for (int i = 0; i < T; ++i)
	{
		int row1;
		inputFile >> row1;
		CardsGrid grid1;
		ReadGrid(&inputFile, grid1);

		int row2;
		inputFile >> row2;
		CardsGrid grid2;
		ReadGrid(&inputFile, grid2);

		int solution = Solve(row1, grid1, row2, grid2);
		cout << "Case #" << (i+1) << ": ";
		switch (solution)
		{
		case BadMagician:
			cout << "Bad magician!";
			break;
		case MagicianCheated:
			cout << "Volunteer cheated!";
			break;
		default:
			cout << solution;
		}
		cout  << endl;
	}

	return 0;
}

