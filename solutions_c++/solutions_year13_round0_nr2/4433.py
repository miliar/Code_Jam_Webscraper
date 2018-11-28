/*
ID: junwang1
LANG: C++
TASK: maze1
*/

#include <stdio.h>

#include <stdlib.h>

#include <algorithm>

#include <sstream>

#include <memory.h>

#include <math.h>

#include <string>

#include <functional>

#include <iostream>

#include <set>

#include <vector>

#include <list>

#include <map>

#include <queue>

#include <stack>

using namespace std;

const int MAX_N =  256;

const int MAX_L = 200001;


void Work ()
{
	freopen ("Lawnmower.in", "r", stdin);
	freopen ("Lawnmower.out", "w", stdout);

	int T = 0;
	int t = 0;
	int N = 0;
	int M =  0;
	int i = 0;
	int j = 0;

	int board[100][100];
	bool flag[100][100] = {0};
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		scanf("%d%d", &N, &M);
		for (i = 0; i < N; ++i)
		{
			for (j = 0; j < M; ++j)
			{
				scanf("%d", &board[i][j]);
			}
		}

		memset(flag, 0, sizeof(flag));

		int max = -1;
		for (i = 0; i < N; ++i)
		{
			max = -1;
			for (j = 0; j < M; ++j)
			{
				if (board[i][j] > max)
				{
					max = board[i][j];
				}
			}

			for (j = 0; j < M; ++j)
			{
				if (board[i][j] == max)
				{
					flag[i][j] =  true;
				}
			}

		}

	
		for (j = 0; j < M; ++j)
		{
			max = -1;
			for (i = 0; i < N; ++i)
			{
				if (board[i][j] > max)
				{
					max = board[i][j];
				}
			}

			for (i = 0; i < N; ++i)
			{
				if (board[i][j] == max)
				{
					flag[i][j] =  true;
				}
			}
		}

		bool ok = true;
		for (i = 0; i < N; ++i)
		{
			for (j = 0; j < M; ++j)
			{
				if (!flag[i][j])
				{
					ok = false;
					break;
				}
			}
		}

		if (ok)
		{
			printf("Case #%d: YES\n", t);
		}
		else
		{
			printf("Case #%d: NO\n", t);
		}
		
	}


	
}

int main()
{
	Work ();

	return 0;
}

