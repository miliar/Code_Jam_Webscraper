#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 8;

int n, m, c;

int mx[N][N];
bool used[N][N];

bool get_bit(int mask, int pos)
{
 	return (mask & (1 << pos)) != 0;
}

void build(int mask)
{
	for (int i = 0; i < n; i++)
	{
	 	for (int j = 0; j < m; j++)
	 	{
	 	 	if (get_bit(mask, i * m + j))
	 	 		mx[i][j] = 1;
	 	 	else
	 	 		mx[i][j] = 0;
	 	}
	}
}

int bits_count(int mask)
{
 	int cnt = 0;
 	while (mask > 0)
 	{
 	 	if (mask % 2 == 1)
 	 		cnt++;
 	 	mask /= 2;
 	}

 	return cnt;
}

int cnt = 0;

void DFS(int x, int y)
{
	used[x][y] = true;
	cnt++;

	for (int dx = -1; dx <= 1; dx++)
	{
	 	for (int dy = -1; dy <= 1; dy++)
	 	{
	 		if (dx == 0 && dy == 0)
	 			continue;

	 		int new_x = x + dx;
	 		int new_y = y + dy;

	 	 	if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= m)
	 	 		continue;	

	 	 	if (mx[new_x][new_y] == 1)
	 	 		return;
	 	}
	}

	for (int dx = -1; dx <= 1; dx++)
	{
	 	for (int dy = -1; dy <= 1; dy++)
	 	{
	 		if (dx == 0 && dy == 0)
	 			continue;

	 		int new_x = x + dx;
	 		int new_y = y + dy;

	 	 	if (new_x < 0 || new_x >= n || new_y < 0 || new_y >= m)
	 	 		continue;

	 	 	if (!used[new_x][new_y])
	 	 		DFS(new_x, new_y);	
	 	}
	}
}

void solve()
{
 	scanf("%d%d%d", &n, &m, &c);
 	int size = n * m;
 		
 	for (int mask = 0; mask < (1 << size); mask++)
 	{
 		if (bits_count(mask) != c)
 			continue;

		build(mask);
		for (int i = 0; i < n; i++)
		{
		 	for (int j = 0; j < m; j++)
		 	{
		 		if (mx[i][j] == 1)
		 			continue;

		 	 	memset(used, 0, sizeof(used));
		 	 	cnt = 0;
		 	 	DFS(i, j);
		 	 	if (cnt == size - c)
		 	 	{
		 	 		//cout << "mask " << mask << endl;

		 	 	 	mx[i][j] = -1;

		 	 	 	for (int t = 0; t < n; t++)
		 	 	 	{
		 	 	 	 	for (int k = 0; k < m; k++)
		 	 	 	 	{
							if (mx[t][k] == 1)
								printf("*");
							if (mx[t][k] == 0)
								printf(".");
							if (mx[t][k] == -1)
								printf("c");
		 	 	 	 	}
		 	 	 	 	printf("\n");
		 	 	 	}

		 	 	 	return;
		 	 	}
		 	}
		}
 	}

 	printf("Impossible\n");
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#endif

	int it;
	scanf("%d", &it);
	for (int i = 0; i < it; i++)
	{
	 	printf("Case #%d:\n", i + 1);
	 	solve();
	}

 	return 0;
}