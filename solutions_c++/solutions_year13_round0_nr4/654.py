#ifndef CANT_USE_TEMPLATE
#define  _CRT_SECURE_NO_WARNINGS
#include <functional>
#include <algorithm>
#include <memory.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <bitset>
#include <string>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <set>
#include <map>
using namespace std;

#define MP make_pair
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int)v.size()
#define sqr(x) ((x)*(x))
#endif

#define  TASK ""

const int N = 300;
const int M = 1 << 20;

int startK, n;
int keys[N];
int type[N];
vector < int > in[N];
int dp[M];

void solve(int mask)
{
	for (int i = 0; i < n; i++)
		if (((1 << i) & mask) == 0 && keys[type[i] - 1] > 0 && dp[mask | (1 << i)] == -1)
		{
			keys[type[i] - 1]--;
			for (int j = 0; j < SZ(in[i]); j++)
				keys[in[i][j] - 1]++;

			dp[mask | (1 << i)] = mask;
			solve(mask | (1 << i));

			for (int j = 0; j < SZ(in[i]); j++)
				keys[in[i][j] - 1]--;
			keys[type[i] - 1]++;
		}
}

int main()
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	//freopen(TASK ".in", "r", stdin);
	//freopen(TASK ".out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int p = 0; p < t; p++)
	{
		cin >> startK >> n;
		memset(keys, 0, sizeof(keys));

		for (int i = 0; i < startK; i++)
		{
			int x;	cin >> x;
			keys[x - 1]++;
		}
		for (int i = 0; i < n; i++)
		{
			int x;
			cin >> type[i] >> x;
			in[i].resize(x);
			for (int j = 0; j < x; j++)
				cin >> in[i][j];
		}
		memset(dp, -1, sizeof(dp));
		solve(0);
		cout << "Case #" << p + 1 << ": ";
		if (dp[(1 << n) - 1] == -1)
			cout << "IMPOSSIBLE\n";
		else
		{
			int mask = (1 << n) - 1;
			stack < int > st;
			while (mask != 0)
			{
				int x = mask ^ dp[mask];
				for (int j = 0;;j++)
					if ((1 << j) == x)
					{
						st.push(j + 1);
						break;
					}
				mask = dp[mask];
			}
			while (!st.empty())
			{
				cout << st.top() << " ";
				st.pop();
			}
			cout << "\n";
		}
	}
	return 0;
}