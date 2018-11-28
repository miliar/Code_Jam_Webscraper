#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <set>
#include <map>
#include <cassert>
#include <numeric>
#include <string>
#include <cstring>
using namespace std;

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) 42
#endif

typedef long long int int64;

const int N = 20;

const int dx[] = {1, 0, -1, 0};
const int dy[] = {0, 1, 0, -1};

int r, c;
int mx[N][N];

bool in(int x, int y)
{
	return x >= 0 && x < r && y >= 0 && y < c;
}

bool good()
{
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			if (mx[i][j] == -1)
				continue;

			int min_same_cnt = 0;
			int max_same_cnt = 0;

			for (int dir = 0; dir < 4; dir++)
			{
				int new_i = i + dx[dir];
				int new_j = j + dy[dir];
				new_j = (new_j + c) % c;
				if (!in(new_i, new_j))
					continue;
				if (mx[new_i][new_j] == mx[i][j])
				{
					min_same_cnt++;
					max_same_cnt++;
				}
				else if (mx[new_i][new_j] == -1)
					max_same_cnt++;
			}
			
			if (min_same_cnt > mx[i][j] || max_same_cnt < mx[i][j])
				return false;
		}
	}
	return true;
}

vector<int> get(int start)
{
	vector<int> res;
	for (int sh = 0; sh < c; sh++)
	{
		for (int i = 0; i < r; i++)
			res.push_back(mx[i][(start + sh) % c]);
	}
	return res;
}

vector<int> get_min()
{
	auto ans = get(0);
	for (int i = 1; i < c; i++)
		ans = min(ans, get(i));
	return ans;
}

set<vector<int> > s;

void rec(int x, int y)
{
	if (!good())
		return;

	if (y == c)
	{
		rec(x + 1, 0);
		return;
	}

	if (x == r)
	{
		if (!good())
			return;
		s.insert(get_min());
		return;
	}

	for (int i = 1; i <= 4; i++)
	{
		mx[x][y] = i;
		rec(x, y + 1);
	}
	mx[x][y] = -1;
}

void solve(int test)
{
	cin >> r >> c;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			mx[i][j] = -1;
	s.clear();
	rec(0, 0);
	printf("Case #%d: %d\n", test, (int)s.size());
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
#endif

	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
		solve(i + 1);

	return 0;
}
