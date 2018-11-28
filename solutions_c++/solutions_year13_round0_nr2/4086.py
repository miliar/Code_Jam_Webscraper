//
// Problem B. Lawnmower
// Author: Tom Richards
// Remarks: This problem is terrible.
//

#include <iostream>
#include <string.h>
using namespace std;

bool canMow(int lawn[][100], int height, int width)
{
	int rowMaxes[100] = {0};
	int colMaxes[100] = {0};

	//find row max
	for(int row=0; row < height; row++)
	{
		for(int col=0; col<width; col++)
		{
			if(lawn[row][col] > rowMaxes[row])
				rowMaxes[row] = lawn[row][col];
		}
	}

	//find column max
	for(int col=0; col < width; col++)
	{
		for(int row=0; row < height; row++)
		{
			if(lawn[row][col] > colMaxes[col])
				colMaxes[col] = lawn[row][col];
		}
	}

	//if the value inside is bigger than either the row or column max, we can't mow this pattern
	for(int row=0; row < height; row++)
	{
		for(int col=0; col < width; col++)
		{
			if(rowMaxes[row] <= lawn[row][col] || colMaxes[col] <= lawn[row][col])
				continue;
			else
				return false;
		}
	}

	return true;
}

int main()
{
	int lawn[100][100] = {0};
	int numCases = 0;
	cin >> numCases;
	for(int c=1; c<=numCases; c++)
	{
		int width = 0, height = 0;
		memset(lawn, 0, sizeof(lawn));
		cin >> height >> width;

		for(int i=0; i < height; i++)
			for(int j=0; j < width; j++)
				cin >> lawn[i][j];

		cout << "Case #" << c << ": " << (canMow(lawn, height, width) ? "YES" : "NO") << endl;
	}
	
	return 0;
}