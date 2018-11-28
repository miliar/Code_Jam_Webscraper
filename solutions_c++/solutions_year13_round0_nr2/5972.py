#include <algorithm>
#include <cstring>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;
int n,m;

int **loadLawn()
{
	cin >> n;
	cin >> m;

	int **lawn = (int **)malloc(sizeof(int *)*n);

	for (int i = 0; i < n; i++)
	{
		lawn[i] = (int *)malloc(sizeof(int)*m);
		for (int j = 0; j < m; j++)
		{
			cin >> lawn[i][j];
		}
	}

	return lawn;
}

bool isLinePossible (int **lawn, int column)
{
	for (int j = 0; j < m; j++)
		if (lawn[column][j] == 2)
			return false;

	return true;
}

bool isColumnPossible (int **lawn, int line)
{
	for (int i = 0; i < n; i++)
			if (lawn[i][line] == 2)
				return false;

	return true;
}

bool isPossible()
{
	int **lawn = loadLawn();

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			if (lawn[i][j] == 1)
			{
				if (isLinePossible(lawn,i))
					break;

				if (isColumnPossible(lawn,j))
					continue;

				return false;
			}
		}
	}

	return true;
}


int main (int argc, char *argv[])
{
	int T = 0;
	cin >> T;

	for (int i = 0; i < T; i++)
	{
		cout << "Case #" << i+1 << ": " << (isPossible() ? "YES" : "NO") << "\n";
	}
}
