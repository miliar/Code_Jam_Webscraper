#include <cassert>
#include <cstring>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>

using namespace std;

const int N = 37;

long long st[N];
long long b;

double solve()
{
	std::sort(st, st + N);
	long long minS = st[0];

	double res = 0;

	for(int block = 1; block <= N; block++)
	{
		for(long long h = minS + 1; ; h++)
		{
			long long win = 0.0;
			long long penalty = 0.0;
			int cnt = 0;

			for(int i = 0; i < N; i++)
				if(st[i] <= h)
				{
					cnt++;

					if(i < block)
					{
						win += h - st[i];
						penalty += h - st[i];
					}
					else
						penalty += h - st[i] + 1;
				}

			if(cnt < block)
				continue;

			if(penalty > b)
				break;

			double cur = 36.0 * (double)win / (double)block - (double)penalty;
			res = max(res, cur);
		}
	}

	return res;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%i\n", &t);

	for(int ti = 1; ti <= t; ti++)
	{
		for(int i = 0; i < N; i++)
			st[i] = 0;
		int n;
		cin >> b >> n;
		for(int i = 0; i < n; i++)
			cin >> st[i];

		cout << "Case #" << ti << ": ";
		printf("%0.20lf", solve());
		cout << "\n";
	}

	return 0;
}
