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
int a[MAX];

int solve3(priority_queue<int> s)
{
	if (s.empty())
		return 0;
	int mx = s.top(); 
	if (mx < 2)
		return mx;
	priority_queue<int> q, q2 = s;
	s.pop();
	while (!q2.empty())
	{
		if (q2.top() > 1)
			q.push(q2.top() - 1);
		q2.pop();
	}
	int tot = mx;
	int k = (tot - mx / 2);
	s.push(k);
	s.push(mx / 2);
	
	mx = min(mx, 1 + solve3(q));
	return min(mx, 1 + solve3(s));
}


int solve2()
{
	int n; cin >> n;
	priority_queue<int> s;
	for (int i = 0; i < n; ++i)
	{
		int r;
		cin >> r;
		s.push(r);
	}

	return solve3(s);
}

int solve()
{
	int n;
	cin >> n;
	priority_queue<int> s;
	for (int i = 0; i < n; ++i)
	{
	
		cin >> a[i];
		s.push(a[i]);
	}

	int ans = 2000;
	int attmp = 0;
	while (attmp++ < 1001)
	{
		int mx = 0;
		for (int i = 0; i < n; ++i)
			if (a[i] > a[mx])
				mx = i;

		int lans = a[mx] + attmp - 1;
		ans = min(ans, lans);
		int tot = a[mx];
		a[mx] = a[mx] / 2;
		a[n++] = tot - a[mx];
	}
	int ans2 = solve3(s);
	if (ans2 != ans)
		throw 34;
	return ans;
}

int solve_1()
{
	int n;
	cin >> n;
	char c;
	int standing = 0; int add = 0;
	for (int i = 0; i <= n; ++i)
	{
		cin >> c;
		int added = 0;
		int cc = c - '0';
		if (standing < i && cc)
		{
			added = i - standing;
		}
		standing += cc + added;
		add += added;
	}
	return add;
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
		cout << solve_1();
		cout << endl;
	}
	return 0;
}