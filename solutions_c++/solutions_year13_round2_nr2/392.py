#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <cassert>

#define LL long long

using namespace std;

const int maxn = 25;

bool center[2 * maxn][maxn];
int n, total, p, X1, Y1;
double answer;

inline bool get_c(int x, int y, bool flag)
{
	if (!flag)
		assert(x + n < 50 && y < 25 && x + n >= 0);
	if (x + n >= 50 || y >= 25 || x + n < 0)
		return false;
	return center[x + n][y];
}

inline void set_c(int x, int y, bool value)
{
	assert(x + n < 50 && y < 25 && x + n >= 0);
	center[x + n][y] = value;
}

inline bool no_move(int x, int y)
{
	return (y == 0) || (get_c(x - 1, y - 1, false) && get_c(x + 1,y - 1, false));
}

inline void move(int & x, int & y, int pl)
{
	while(!no_move(x, y))
	{
		//if (center[x + pl][y - 1])
		x += pl;
		y--;
	}
}

void solve(int step, int max_y, double cur)
{
	if (step == n + 1)
	{
		if (get_c(X1, Y1, true))
			answer += cur;
			//p++;
		//total++;
		return;
	}
	if (step == 1)
	{
		set_c(0, 0, true);
		solve(step + 1, 0, cur);
		return;
	}
	int tt = 0;
	if (!get_c(1, max_y + 1, false))
		tt++;
	if (!get_c(-1, max_y + 1, false))
		tt++;
	for (int j = -1; j <= 1; j += 2)
	{
		if (!get_c(j, max_y + 1, false))
		{
			int new_x = 0;
			int new_y = max_y + 2;
			move(new_x, new_y, j);
			set_c(new_x, new_y, true);
			//int t_max = max_y;
			//if (new_x == 0)
			//	t_max = max(t_max, new_y);
			solve(step + 1, max_y, cur / (double)tt);
			set_c(new_x, new_y, false);
		}
	}
	if (get_c(1, max_y + 1, false) && get_c(-1, max_y + 1, false))
	{
		set_c(0, max_y + 2, true);
		solve(step + 1, max_y + 2, cur);
		set_c(0, max_y + 2, false);
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++)
	{
		memset(center, false, sizeof(center));
		scanf("%d%d%d", &n, &X1, &Y1);
		total = p = 0;
		answer = 0;
		solve(1, -2, 1.0);
		//double answer = (double)p / (double)total;
		//assert(total != 0);
		printf("Case #%d: %0.10lf\n", test, answer);
	}
}