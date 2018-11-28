/*
ID: eoart2
PROG: transform
LANG: C++
*/
//#define MYDEBUG
#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker, "/STACK:134217728")
#include <cstdio>
#include <iostream>
#include <iomanip> 
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <string>
#include <functional>
#include <cassert>
#include <random>

const long long MOD = 1000000007;
const int INF = 2000000000;
const int MAXN = 200000;
const double EPS = 1e-9;
const int HASH_POW = 7;
const double PI = acos(-1.0);

using namespace std;

void my_return(int code)
{
#ifdef MYDEBUG
	cout << "\nTime = " << fixed << setprecision(3) << double(clock()) / CLOCKS_PER_SEC << endl;
#endif
	exit(code);
}

int main()
{
	//cin.sync_with_stdio(0);
	mt19937 mt_rand(time(NULL));
	#ifdef MYDEBUG
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	#else
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	#endif

	int CASE;
	cin >> CASE;
	for (int T = 1; T <= CASE; ++T)
	{
		int r, c;
		cin >> r >> c;
		char p[110][110];
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
				cin >> p[i][j];
		}
		bool haveans = true;
		int ans = 0;
		for (int i = 0; i < r; ++i)
		{
			for (int j = 0; j < c; ++j)
			{
				if (p[i][j] == '.')
					continue;

				int dx = 0, dy = 0;
				if (p[i][j] == '^')
					dx = -1;
				else if (p[i][j] == '<')
					dy = -1;
				else if (p[i][j] == '>')
					dy = 1;
				else
					dx = 1;

				int x = i, y = j;
				x += dx, y += dy;
				while (x >= 0 && x < r && y >= 0 && y < c && p[x][y] == '.')
					x += dx, y += dy;
				if (x >= 0 && x < r && y >= 0 && y < c)
					continue;

				int cnt = 0;
				for (int j = 0; j < c; ++j)
					if (p[i][j] != '.')
						++cnt;
				for (int i = 0; i < r; ++i)
					if (p[i][j] != '.')
						++cnt;
				if (cnt == 2)
				{
					haveans = false;
					break;
				}
				else
					++ans;
			}
			if (!haveans)
				break;
		}
		cout << "Case #" << T << ": ";
		if (haveans)
			cout << ans << "\n";
		else
			cout << "IMPOSSIBLE\n";
	}

	my_return(0);
}