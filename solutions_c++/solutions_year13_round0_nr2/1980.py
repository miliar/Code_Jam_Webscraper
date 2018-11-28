#include<iostream>
#include<queue>
#include<map>
#include<cstring>
#include<utility>
#include<vector>
#include<climits>
#include<iomanip>
#include<set>
#include<algorithm>
#include<string>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<stack>
#include<cstdio>
#include<stdio.h>
using namespace std;
int garden[101][101];
int rowsMax[101];
int columnsMax[101];
int rows, columns;


int rowMax(int row)
{
	int res = 0;
	for(int i = 0; i < columns; i++)
		if(garden[row][i] > res)
			res = garden[row][i];

	return res;
}


int columnMax(int column)
{
	int res = 0;
	for(int i = 0; i < rows; i++)
		if(garden[i][column] > res)
			res = garden[i][column];
	return res;
}

void findMaxs()
{
	for(int i = 0; i < rows; i++)
		rowsMax[i] = rowMax(i);

	for(int i = 0; i < columns; i++)
		columnsMax[i] = columnMax(i);
}

int main()
{
	freopen("output.txt", "w", stdout);
	freopen("B-large.in", "r", stdin);
	int t;
	cin >> t;
	bool possible;
	for(int i = 1; i <= t; i++)
	{
		possible = true;
		cin >> rows >> columns;	
		for(int j = 0; j < rows; j++)
			for(int k = 0; k < columns; k++)
				cin >> garden[j][k];
		
		findMaxs();

		for(int j = 0; j < rows; j++)
		{
			for(int k = 0; k < columns; k++)
				if(garden[j][k] < rowsMax[j] &&garden[j][k] < columnsMax[k])
				{
					possible = false;
					break;
				}
				if(!possible)
					break;
		}

		cout << "Case #" << i << ": ";
		if(possible)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
		

	}

	
	
	return 0;
		
}	
