#include <cassert>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <queue>

using namespace std;

const int N = 1 << 12;

int n;
int a[N], b[N];

int t[N];
bool busy[N];

bool backtrack(const int p)
{
	if(p >= n)
	{
		bool ok = true;
		for(int i = 0; i < n; i++)
		{
			int bc = 1;
			for(int j = i + 1; j < n; j++)
				if(t[i] > t[j])
					bc = max(bc, b[j] + 1);

			if(bc != b[i])
			{
				ok = false;
				break;
			}
		}

		if(!ok)
			return false;

		for(int i = 0; i < n; i++)
			printf(" %i", t[i] + 1);
		return true;
	}

	for(int c = 0; c < n; c++)
	{
		if(busy[c])
			continue;

		{
			int ac = 1;
			for(int i = 0; i < p; i++)
				if(t[i] < c)
					ac = max(ac, a[i] + 1);

			if(ac != a[p])
				continue;
		}

		{
			bool ok = true;
			for(int i = 0; i < p; i++)
				if(t[i] > c && b[i] < b[p] + 1)
				{
					ok = false;
					break;
				}

			if(!ok)
				continue;
		}

		busy[c] = true; t[p] = c;

		if(backtrack(p + 1))
			return true;

		busy[c] = false;
	}

	return false;
}

void solve()
{
	std::memset(busy, 0, sizeof(busy));
	if(!backtrack(0))
		assert(false);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%i\n", &t);

	for(int ti = 1; ti <= t; ti++)
	{
		scanf("%i", &n);
		for(int i = 0; i < n; i++)
			scanf("%i", &a[i]);

		for(int i = 0; i < n; i++)
			scanf("%i", &b[i]);

		cout << "Case #" << ti << ": ";
		solve();
		cout << "\n";
		cerr << ti << "\n";
	}

	return 0;
}
