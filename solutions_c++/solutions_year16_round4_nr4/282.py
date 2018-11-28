#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <map>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cassert>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> tll;

// globals starts here

const int MAX_N = 4;
int work[MAX_N][MAX_N];
int w[MAX_N][MAX_N];
int n;

int ones(int mask)
{
	int x = 0;
	while (mask > 0)
	{
		if (mask & 1)
		{
			++x;
		}
		mask >>= 1;
	}
	return x;
}

vector<int> perm;
bool go(int num, vector<bool>& used)
{
	if (num >= n)
	{
		return true;
	}

	int worker = perm[num];
	bool have = false;
	for (int i = 0; i < n; ++i)
	{
		if (w[worker][i] && !used[i])
		{
			have = true;
			used[i] = true;
			bool res = go(num + 1, used);
			if (!res)
			{
				return false;
			}
			used[i] = false;
		}
	}

	return have;
}

bool check()
{
	perm.clear();
	vector<bool> used;
	for (int i = 0; i < n; ++i)
	{
		perm.push_back(i);
		used.push_back(false);

	}

	do
	{
		if (!go(0, used))
		{
			return false;
		}
	} while (next_permutation(perm.begin(), perm.end()));

	return true;
}

int solve()
{
	int best = n*n;

	for (int m = 0; m < (1 << (n*n)); ++m)
	{
		for (int i = 0; i < n*n; ++i)
		{
			w[i / n][i%n] = work[i / n][i%n] | ((m >> i) & 1);
		}

		if (check())
		{
			int nones = ones(m);
			best = min(best, nones);
		}
	}

	return best;
}

int main()
{
#ifdef XXX
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int tests;
	cin >> tests;

	for (int tc = 1; tc <= tests; ++tc)
	{
		cin >> n;
		for (int i = 0; i < n; ++i) 
		{
			string line;
			cin >> line;
			for (int j = 0; j < n; ++j)
			{
				work[i][j] = line[j] - '0';
			}
		}

		int ans = solve();

		printf("Case #%d: %d\n", tc, ans);
	}

	return 0;
}