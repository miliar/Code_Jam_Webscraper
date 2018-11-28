#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <cmath>
#include <assert.h>
using namespace std;


bool solve(char grid[][101], int N, int M, long Max)
{
	char sol[101][101];
	memset(sol,Max,sizeof(sol));
	bool result = true;

	for (int i =0; i<N; i++)
	{
		int lineMax = 0;
        for(int j = 0; j<M; j++)
		{
			if(lineMax < grid[i][j])
				lineMax = grid[i][j];
		}

		for(int j = 0; j<M; j++)
			sol[i][j] = lineMax;
	}

	for (int j =0; j<M; j++)
	{
		int columnMax = 0;
        for(int i = 0; i<N; i++)
		{
			if(columnMax < grid[i][j])
				columnMax = grid[i][j];
		}

		for(int i = 0; i<N; i++)
		{
			if(sol[i][j] > columnMax)
				sol[i][j] = columnMax;
		}
	}



	for(int i =0; i<N; i++)
	{
		for(int j = 0; j<M; j++)
		{
			if(sol[i][j]!=grid[i][j])
				return false;
		}
	}

	return result;
}


int _tmain(int argc, _TCHAR* argv[])
{ 
	int numCase = 0;
	int N, M;
	char grid [101][101];
	cin >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		memset(grid,0,sizeof(grid));
		cin >> N >> M;
		
		long Max = 0;
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<M;k++)
			{
				cin >> grid[j][k];
				if(Max < grid[j][k])
					Max = grid[j][k];
			}
		}

		cout << "Case #" << (i+1) << ": ";
		
		if(solve(grid, N, M, Max))
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}

	return 0;
}



