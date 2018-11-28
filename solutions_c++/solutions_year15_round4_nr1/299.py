#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <math.h>
#include <memory.h>


using namespace std;

#define MAX 100

int matr[MAX][MAX];
bool can[MAX][MAX][4];
int dirs[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

int main()
{

	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int N, M;
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			char s[2000];
			cin >> s;
			for (int j = 0; j < M; j++)
			{
				if (s[j] == '.')
					matr[i][j] = -1;
				if (s[j] == '>')
					matr[i][j] = 0;
				if (s[j] == 'v')
					matr[i][j] = 1;
				if (s[j] == '<')
					matr[i][j] = 2;
				if (s[j] == '^')
					matr[i][j] = 3;
			}
		}
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				for (int k = 0; k < 4; k++)
					can[i][j][k] = true;

		for (int i = 0; i < N; i++)
		{
			int j = 0;
			while (j < M && matr[i][j] == -1)
				j++;
			if (j < M)
				can[i][j][2] = false;

			j = M-1;
			while (j >=0 && matr[i][j] == -1)
				j--;
			if (j >= 0)
				can[i][j][0] = false;
		}

		for (int j = 0; j < M; j++)
		{
			int i = 0;
			while (i < N && matr[i][j] == -1)
				i++;
			if (i < N)
				can[i][j][3] = false;

			i = N-1;
			while (i >=0 && matr[i][j] == -1)
				i--;
			if (i >= 0)
				can[i][j][1] = false;
		}

		bool ok = true;
		int res = 0;
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				if (matr[i][j] != -1)
				{
					bool ex = false;
					for (int d = 0; d < 4; d++)
						if (can[i][j][d])
							ex = true;
					if (!ex)
						ok = false;
					if (!can[i][j][matr[i][j]])
						res++;
				}
		if (!ok)
			printf("Case #%d: IMPOSSIBLE\n", t+1);
		else
			printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}