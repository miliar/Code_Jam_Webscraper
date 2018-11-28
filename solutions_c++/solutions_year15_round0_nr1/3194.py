#define _CRT_SECURE_NO_WARNINGS
#pragma comment(linker,"/STACK:64000000")
#include <iostream>
#include <cstdio>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <string>
#include <memory.h>
#include <limits.h>
#include <queue>

using namespace std;

void prepare(string s)
{
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#else
	if (s.size() != 0)
	{
		freopen((s + ".in").c_str(), "r", stdin);
		freopen((s + ".out").c_str(), "w", stdout);
	}
#endif
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
}

vector <int> s;

void solve()
{
	int count = 0,
		_friend = 0;

	for (int i = 0; i < s.size(); i++)
	{
		if (count >= i)
		{
			count += s[i];
		}
		else
		{
			_friend += i - count;
			count = i + s[i];
		}
	}
	cout << _friend << endl;
}

void getData()
{
	s.clear();

	int smax;
	cin >> smax;

	string line;
	cin >> line;

	for (int i = 0; i < line.size(); i++)
	{
		int si = line[i] - '0';
		s.push_back(si);
	}
}

int main()
{
	prepare("");
	
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
				cout << "Case #" << i + 1 << ": ";
		getData();
		solve();

	}
	return 0;
}
