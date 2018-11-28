#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <stack>
#include <deque>
#include <queue>

using namespace std;

int Y, X;
vector<vector<char> > a;

void input()
{
	cin >> Y >> X;
	a.clear();

	a.resize(X, vector<char>(Y));
	string s;
	for (int y = 0; y < Y; ++y)
	{
		cin >> s;
		for (int x = 0; x < X; ++x)
		{
			a[x][y] = s[x];
		}
	}

	vector<vector<char> > left(X, vector<char>(Y));
	vector<vector<char> > right(X, vector<char>(Y));
	vector<vector<char> > bottom(X, vector<char>(Y));
	vector<vector<char> > top(X, vector<char>(Y));

	for (int y = 0; y < Y; ++y)
	{
		bool have = false;
		for (int x = 0; x < X; ++x)
		{
			if (a[x][y] != '.')
			{
				left[x][y] = have;
				have = true;
			}
		}
		have = false;
		for (int x = X - 1; x >= 0; --x)
		{
			if (a[x][y] != '.')
			{
				right[x][y] = have;
				have = true;
			}
		}
	}
	for (int x = 0; x < X; ++x)
	{
		bool have = false;
		for (int y = 0; y < Y; ++y)
		{
			if (a[x][y] != '.')
			{
				top[x][y] = have;
				have = true;
			}
		}
		have = false;
		for (int y = Y - 1; y >= 0; --y)
		{
			if (a[x][y] != '.')
			{
				bottom[x][y] = have;
				have = true;
			}
		}
	}

	int result = 0;
	bool impossible = false;
	for (int y = 0; y < Y; ++y)
	{
		for (int x = 0; x < X; ++x)
		{
			if (a[x][y] == '^')
			{
				if (top[x][y])continue;
				else if (left[x][y] || right[x][y] || bottom[x][y])++result;
				else impossible = true;
			}
			else if (a[x][y] == '>')
			{
				if (right[x][y])continue;
				else if (left[x][y] || top[x][y] || bottom[x][y])++result;
				else impossible = true;
			}
			else if (a[x][y] == 'v')
			{
				if (bottom[x][y])continue;
				else if (left[x][y] || top[x][y] || right[x][y])++result;
				else impossible = true;
			}
			else if (a[x][y] == '<')
			{
				if (left[x][y])continue;
				else if (bottom[x][y] || top[x][y] || right[x][y])++result;
				else impossible = true;
			}
		}
	}
	
	if (impossible)
	{
		cout << "IMPOSSIBLE" << endl;
	}
	else
	{
		cout << result << endl;
	}

}

void solve()
{
	input();
}

int main()
{
	//ios_base::sync_with_stdio(false);
	//freopen("d:/A-small-attempt0.in", "rt", stdin);
	int T; std::cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}

	return 0;
}