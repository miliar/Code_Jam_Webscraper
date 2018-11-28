#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <cmath>

using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif
const int N = 7;
const int DX[] = {0, 1, 0, -1};
const int DY[] = {1, 0, -1, 0};
int n, m;
int matrix[N][N];
int colValue[N];

bool check(int x, int y)
{
	return x >= 0 && y >= 0 && x < n && y < m;
}

bool checkCol(int y)
{
	for (int i = 0; i < n; i++)
	{
		int cnt = 0;
		for (int d = 0; d < 4; d++)
		{
			int nx = i + DX[d];
			int ny = y + DY[d];
			if (ny >= m)
				ny -= m;
			if (ny < 0)
				ny += m;
			if (check(nx, ny) && matrix[nx][ny] == matrix[i][y])
				cnt++;
		}
		if (cnt != matrix[i][y])
			return false;
	}
	return true;
}

bool checkColSafety(int y)
{
	for (int i = 0; i < n; i++)
	{
		int cnt = 0;
		int f = 0;
		for (int d = 0; d < 4; d++)
		{
			int nx = i + DX[d];
			int ny = y + DY[d];
			if (ny >= m)
				ny -= m;
			if (ny < 0)
				ny += m;
			if (check(nx, ny) && matrix[nx][ny] == matrix[i][y])
				cnt++;
			if (check(nx, ny) && matrix[nx][ny] == 0)
				f++;
		}
		if (cnt > matrix[i][y] || cnt + f < matrix[i][y])
			return false;
	}
	return true;
}

int ans = 0;

void bruteOther(int x, int y)
{
	if (x == n)
	{
		if (!checkColSafety(y))
			return;
		if (y - 1 > 0 && !checkCol(y - 1))
			return;
		bruteOther(0, y + 1);
		return;
	}
	if (y == m)
	{
		if (!checkCol(0) || !checkCol(m - 1))
			return;
		for (int i = 1; i < m; i++)
		{
			bool ok = true;
			for (int s = 0; s < m; s++)
			{
				int a = s;
				int b = (i + s) % m;
				if (colValue[a] < colValue[b])
					break;
				if (colValue[a] > colValue[b])
				{
					ok = false;
					break;
				}
			}
			if (!ok)
				return;
		}
		ans++;
		return;
	}
	for (int i = 1; i <= 4; i++)
	{
		matrix[x][y] = i;
		colValue[y] *= 5;
		colValue[y] += i;
		bruteOther(x + 1, y);
		colValue[y] /= 5;
	}
	matrix[x][y] = 0;
}
int it = 0;

void bruteFirst(int x)
{
	if (x == n)
	{
//		for (int i = 0; i < n; i++)
//			cout << matrix[i][0];
//		cout << "!!!" << endl;
		bruteOther(0, 1);
		return;
	}
	for (int i = 1; i <= 4; i++)
	{
		matrix[x][0] = i;
		colValue[0] *= 5;
		colValue[0] += i;
		bruteFirst(x + 1);
		colValue[0] /= 5;
	}
}

void solve()
{
	ans = 0;
	scanf("%d%d", &n, &m);
	bruteFirst(0);
	printf("%d\n", ans);
}

int main()
{
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		eprintf("i = %d\n", i);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}
