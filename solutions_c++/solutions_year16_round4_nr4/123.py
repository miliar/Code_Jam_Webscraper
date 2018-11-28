#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
#include <string>

#include <valarray>
#include <complex>
#include <functional>

using namespace std;

const int N = 100;
int table[N][N];
char str[N];

int n;

void read()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf(" %s", str);
		for (int s = 0; s < n; s++)
			table[i][s] = str[s] - '0';
	}
}

int perm[N];
int jobs[N];
int used[N];

bool check()
{
	for (int i = 0; i < n; i++)
		perm[i] = jobs[i] = i;
	do
	{
		do
		{
			fill(used, used + n, 0);
			for (int i = 0; i < n; i++)
			{
				int who = perm[i];
				int to = jobs[i];
				bool fail = true;
				if (table[who][to] == 0)
				{
					for (int a = 0; a < n; a++)
					{
						if (!used[a] && table[who][a])
							fail = false;
					}
					if (fail)
						return false;
				}
				else
					used[to] = 1;
			}
		} while (next_permutation(jobs, jobs + n));
	} while (next_permutation(perm, perm + n));
	return true;
}

bool brute(int x, int y, int t)
{
	if (t == 0)
		return check();
	if (x == n)
		return false;
	if (y == n)
		return brute(x + 1, 0, t);
	bool a = false;
	if (table[x][y] == 1)
		return brute(x, y + 1, t);

	if (rand() % 2 == 0)
	{
		a |= brute(x, y + 1, t);
		table[x][y] = 1;
		a |= brute(x, y + 1, t - 1);
		table[x][y] = 0;
	}
	else
	{
		table[x][y] = 1;
		a |= brute(x, y + 1, t - 1);
		table[x][y] = 0;
		a |= brute(x, y + 1, t);
	}
	return a;
}

void solve()
{
	int f = 0;
	for (int i = 0; i < n; i++)
		for (int s = 0; s < n; s++)
			f += (1 - table[i][s]);
	for (int i = 0; i <= f; i++)
	{
		if (brute(0, 0, i))
		{
			printf("%d\n", i);
			break;
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++)
	{
		printf("Case #%d: ", i + 1);
		read();
		solve();
	}
	return 0;
}
