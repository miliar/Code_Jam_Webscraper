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

vector<int> p;

void solve()
{
	int MAX = 0;

	for (int i = 0; i < p.size(); i++)
	{
		MAX = max(MAX, p[i]);
	}

	int ans = INT_MAX;


	for (int i = 1; i <= MAX; i++)
	{
		int cnt = 0;

		for (int j = 0; j < p.size(); j++)
		{
			cnt += (p[j] - 1) / i;
		}
		ans = min(ans, i + cnt);
	}

	cout << ans << endl;
}

void getData()
{
	p.clear();

	int d;
	cin >> d;

	for (int i = 0; i < d; i++)
	{
		int el;
		cin >> el;
		p.push_back(el);
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
