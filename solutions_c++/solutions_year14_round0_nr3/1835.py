#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
vector <bool> mineField;
int r, c, k;

vector <vector <int> > goodField;
pair<int, int> gp;

void isFieldGood()
{
	vector <vector <int> > f(r, vector <int> (c, 1));
	for (int i = 0; i < r * c; ++i)
	{
		if (mineField[i])
			f[i / c][i % c] = 0;
	}
	int not = r * c - k;

	for (int x = 0; x < r; ++x)
	{
		for (int y = 0; y < c; ++y)
		{
			if (f[x][y])
			{
				queue<pair<int, int> > q;
				q.push(make_pair(x, y));
				vector <vector <bool> > used(r, vector <bool> (c, 0));
				int now = 0;
				while (q.size())
				{
					auto cur = q.front();
					if (f[cur.first][cur.second] && !used[cur.first][cur.second])
						++now;
					used[cur.first][cur.second] = 1;

					q.pop();
					bool bad = 0;
					if (cur.first)
					{
						if (cur.second)
							if (!f[cur.first - 1][cur.second - 1])
								bad = true;
						if (!f[cur.first - 1][cur.second])
							bad = true;
						if (cur.second + 1 < c)
							if (!f[cur.first - 1][cur.second + 1])
								bad = true;
					}
					if (true)
					{
						if (cur.second)
							if (!f[cur.first][cur.second - 1])
								bad = true;
						if (!f[cur.first][cur.second])
							bad = true;
						if (cur.second + 1 < c)
							if (!f[cur.first][cur.second + 1])
								bad = true;
					}
					if (cur.first + 1 < r)
					{
						if (cur.second)
							if (!f[cur.first + 1][cur.second - 1])
								bad = true;
						if (!f[cur.first + 1][cur.second])
							bad = true;
						if (cur.second + 1 < c)
							if (!f[cur.first + 1][cur.second + 1])
								bad = true;
					}
					if (!bad)
					{
						if (cur.first)
						{
							if (cur.second)
								if (!used[cur.first - 1][cur.second - 1])
									q.push(make_pair(cur.first - 1, cur.second - 1));
							if (!used[cur.first - 1][cur.second])
								q.push(make_pair(cur.first - 1, cur.second));
							if (cur.second + 1 < c)
								if (!used[cur.first - 1][cur.second + 1])
									q.push(make_pair(cur.first - 1, cur.second + 1));
						}
						if (true)
						{
							if (cur.second)
								if (!used[cur.first][cur.second - 1])
									q.push(make_pair(cur.first, cur.second - 1));
							if (!used[cur.first][cur.second])
								q.push(make_pair(cur.first, cur.second));
							if (cur.second + 1 < c)
								if (!used[cur.first][cur.second + 1])
									q.push(make_pair(cur.first, cur.second + 1));
						}
						if (cur.first + 1 < r)
						{
							if (cur.second)
								if (!used[cur.first + 1][cur.second - 1])
									q.push(make_pair(cur.first + 1, cur.second - 1));
							if (!used[cur.first + 1][cur.second])
								q.push(make_pair(cur.first + 1, cur.second));
							if (cur.second + 1 < c)
								if (!used[cur.first + 1][cur.second + 1])
									q.push(make_pair(cur.first + 1, cur.second + 1));
						}
					}
				}
				if (now == not)
				{
					goodField = f;
					gp = make_pair(x, y);
					return;
				}
			}
		}
	}
}



void gen(int n, int i, int left)
{
	if (gp != make_pair(-1, -1))
			return;
	if (i == n)
	{
		isFieldGood();
		if (gp != make_pair(-1, -1))
			return;
	}
	else
	{
		if (left)
		{
			mineField[i] = 1;
			gen(n, i + 1, left - 1);
		}
		if (left != n - i)
		{
			mineField[i] = 0;
			gen(n, i + 1, left);
		}
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int z = 1; z <= T; ++z)
	{
		printf("Case #%d:\n", z);
		gp = make_pair(-1, -1);
		scanf("%d %d %d", &r, &c, &k);
		mineField.resize(r * c);
		gen(r * c, 0, k);
		if (gp == make_pair(-1, -1))
		{
			printf("Impossible\n");
			continue;
		}
		
		goodField[gp.first][gp.second] = 2;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (goodField[i][j] == 0)
					printf("*");
				else if (goodField[i][j] == 1)
					printf(".");
				else
					printf("c");
			}
			printf("\n");
		}
	}
	return 0;
}