#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;
#define MAX 20


int R, C, L;
int lovers[MAX][2];
int maze[MAX][MAX];
bool was[MAX][MAX][4];

int dirs[4][2] = { {-1, 0},{ 0, 1 },{ 1, 0 },{ 0, -1 } };

void dfs(int x, int y, int cell)
{
	was[x][y][cell] = true;

	int xx = x + dirs[cell][0];
	int yy = y + dirs[cell][1];
	int cc = (cell + 2) % 4;
	if (xx >= 0 && xx < R && yy >= 0 && yy < C && !was[xx][yy][cc])
		dfs(xx, yy, cc);

	if (maze[x][y] == 0)
	{
		if (cell == 1 || cell == 3)
			cc = (cell + 1) % 4;
		else
			cc = (cell + 3) % 4;
		if (!was[x][y][cc])
			dfs(x, y, cc);
	}
	else
	{
		if (cell == 1 || cell == 3)
			cc = (cell + 3) % 4;
		else
			cc = (cell + 1) % 4;
		if (!was[x][y][cc])
			dfs(x, y, cc);
	}
}

pair<pair<int, int>, int> f(int a)
{
	a--;
	if (a < C)
		return make_pair(make_pair(0, a), 0);
	if (a < C + R)
		return make_pair(make_pair(a - C, C - 1), 1);
	if (a < C + R + C)
		return make_pair(make_pair(R - 1, C - 1 - (a - R - C)), 2);
	return make_pair(make_pair(R - 1 - (a - C - R - C), 0), 3);
}

bool check()
{
	
	bool ok = true;
	for (int i = 0; i < L; i++)
	{
		auto from = f(lovers[i][0]);
		auto to = f(lovers[i][1]);
		memset(was, 0, sizeof(was));
		dfs(from.first.first, from.first.second, from.second);
		if (!was[to.first.first][to.first.second][to.second])
		{
			ok = false;
			break;
		}
	}
	return ok;
}

void print()
{
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
			cout << ((maze[i][j] == 0) ? "/" : "\\");
		cout << "\n";
	}
		
}

void process(int t)
{
	cout << "Case #" << t << ":\n";
	cin >> R >> C;
	L = R + C;
	for (int i = 0; i < L; i++)
	{
		cin >> lovers[i][0] >> lovers[i][1];
	}
	int NN = 1 << (R * C);
	bool found = false;
	for (int i = 0; i < NN; i++)
	{
		for (int j = 0; j < R * C; j++)
			if (i & (1 << j))
				maze[j / C][j % C] = 1;
			else
				maze[j / C][j % C] = 0;
		if (check())
		{
			found = true;
			print();
			break;
		}
	}
	if (!found)
	{
		cout << "IMPOSSIBLE\n";
	}
}



int main()
{
	freopen("c:\\Projects\\CodeJam2016R2\\C\\C.in", "r", stdin);
	freopen("c:\\Projects\\CodeJam2016R2\\C\\C.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
		process(t + 1);



	fclose(stdin);
	fclose(stdout);
	return 0;
}