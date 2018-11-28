// CodeJamTemplate.cpp : Defines the entry point for the console application.
//


#include "stdafx.h"

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

void initialize()
{
}


void solve_case(int test_case)
{
	int height, width;
	bool canDo = true;

	cin >> height >> width;

	vector <vector<int>> board;
	vector <vector<int>> target;

	board.resize(height);
	target.resize(height);
	
	for(int i = 0; i < height; i++)
	{
		int h;

		board[i].resize(width);
		target[i].resize(width);

		for(int j = 0; j < width; j++)
		{
			cin >> board[i][j];
			target[i][j] = 100;
		}
	}

	// From the left side
	for(int i = 0; i < height; i++)
	{
		// Init height
		int maxHeight = board[i][0];
		for(int j = 0; j < width; j++)
		{
			if(board[i][j] > maxHeight)
				maxHeight = board[i][j];
		}

		// Update the row
		for(int j = 0; j < width; j++)
		{
			if(target[i][j] > maxHeight)
				target[i][j] = maxHeight;
		}
	}

	// From the top side
	for(int i = 0; i < width; i++)
	{
		// Init height
		int maxHeight = board[0][i];
		for(int j = 0; j < height; j++)
		{
			if(board[j][i] > maxHeight)
				maxHeight = board[j][i];
		}

		// Update the row
		for(int j = 0; j < height; j++)
		{
			if(target[j][i] > maxHeight)
				target[j][i] = maxHeight;
		}
	}


	// Do we win?
	for(int i = 0; i < height; i++)
	{
		for(int j = 0; j < width; j++)
		{
			if(board[i][j] != target[i][j])
				canDo = false;
		}
	}

	if(canDo)
		printf("Case #%d: %s\n", test_case, "YES");
	else
		printf("Case #%d: %s\n", test_case, "NO");
}

int _tmain(int argc, _TCHAR* argv[])
{
	initialize();

	int iCases;
	cin >> iCases;

	for (int i = 1; i <= iCases; i++)
		solve_case(i);

	return 0;
}
