#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>
#include <string>
#include <map>
#include <set>
using namespace std;

const int N = 10001;
int d[N][N];

const int a[4][4] = {
	{ 1, 2, 3, 4 },
	{ 2, -1, 4, -3 },
	{ 3, -4, -1, 2 },
	{ 4, 3, -2, -1 }
};

int Parse(char c)
{
	if (c == 'i') return 2;
	if (c == 'j') return 3;
	if (c == 'k') return 4;
}

int  main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;
	for (int q = 1; q <= t; q++)
	{
		int l, x;
		cin >> l >> x;

		string s;
		string line;
		cin >> line;
		for (int i = 0; i < x; i++)
		{
			s += line;
		}
		for (int i = 0; i < s.length(); i++)
		{
			d[i][i] = Parse(s[i]);
			for (int j = i + 1; j < s.length(); j++)
			{
				d[i][j] = a[abs(d[i][j - 1]) - 1][Parse(s[j]) - 1];
				if (d[i][j - 1] < 0) d[i][j] *= -1;
			}
		}

		bool ans = false;
		for (int i = 1; i < s.length() - 1; i++)
		{

			if (d[0][i - 1] != 2) continue;
			for (int j = i; j < s.length() - 1; j++)
			{
				if (d[i][j] == 3 && d[j + 1][s.length() - 1] == 4)
				{
					ans = true;
					break;
				}

			}
			if (ans) break;
		}
		cout << "Case #" << q << ": ";
		if (ans) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}