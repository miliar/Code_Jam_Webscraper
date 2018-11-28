/*
 * lawn.cpp
 *
 *  Created on: Apr 12, 2013
 *      Author: firat
 */

#include <iostream>
using namespace std;

int lawn[100][100];
int rows, cols;

bool test_row(int r, int c)
{
	int val = lawn[r][c];
	for(int c1 = 0; c1 < cols; c1++)
	{
		if(lawn[r][c1] > val)
		{
			return true;
		}
	}
	return false;
}

bool test_col(int r, int c)
{
	int val = lawn[r][c];
	for(int r1 = 0; r1 < rows; r1++)
	{
		if(lawn[r1][c] > val)
		{
			return true;
		}
	}
	return false;
}

int main()
{
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{

		cin >> rows;
		cin >> cols;

		bool result = false;

		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				cin >> lawn[r][c];
			}
		}
		for(int r = 0; r < rows; r++)
		{
			for(int c = 0; c < cols; c++)
			{
				result = test_row(r,c) && test_col(r,c);
				if(result)
				{
					break;
				}
			}
			if(result)
			{
				break;
			}
		}
		if(result)
		{
			cout << "Case #" << i+1 << ": NO" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": YES" << endl;
		}
	}
	return 0;
}


