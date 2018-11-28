#define _CRT_SECURE_NO_WARNINGS
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <stdio.h>
#include <string.h>
using namespace std;
const int MAX = 10000;
string a[MAX];

void solve()
{
	int n, m;

	cin >> n >> m;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	int need = 0;
	for (int i = 0; i < n && need >= 0; ++i)
		for (int j = 0; j < m && need >= 0; ++j)
		{
			bool canLeft = false;
			bool canRight = false;
			bool canUp = false;
			bool canDown = false;

			for (int k = 0; k < j; ++k)
				canLeft = canLeft || a[i][k] != '.';

			for (int k = j+1; k < m; ++k)
				canRight = canRight || a[i][k] != '.';

			for (int k = 0; k < i; ++k)
				canUp = canUp || a[k][j] != '.';

			for (int k = i + 1; k < n; ++k)
				canDown = canDown || a[k][j] != '.';

			if (a[i][j] != '.')
			{
				if (a[i][j] == '>' && canRight)
					continue;
				if (a[i][j] == '<' && canLeft)
					continue;
				if (a[i][j] == '^' && canUp)
					continue;
				if (a[i][j] == 'v' && canDown)
					continue;

				if (canLeft || canRight || canUp || canDown)
					need++;
				else
				{
					need = -1;
					break;
				}
			}

		}

	if (need == -1)
		cout << "IMPOSSIBLE";
	else
		cout << need;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}