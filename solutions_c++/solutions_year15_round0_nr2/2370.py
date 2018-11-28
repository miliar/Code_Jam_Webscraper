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
int solve5()
{
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	int answer = MAX;
	for (int eatstart = 1; eatstart < 1002; ++eatstart)
	{
		int moves = 0;
		for (int i = 0; i < n; ++i)
		{
			int move = (a[i] - 1) / eatstart;
			moves += max(move, 0);
		}
		int ans = moves + eatstart;

		answer = min(answer, ans);
	}

	return answer;
}
int solve3(priority_queue<int> s)
{
	if (s.empty())
		return 0;
	int mx = s.top(); 
	if (mx < 3)
		return mx;
	priority_queue<int> q, q2 = s;
	s.pop();
	/*while (!q2.empty())
	{
		if (q2.top() > 1)
			q.push(q2.top() - 1);
		q2.pop();
	}*/
	q2.pop();
	int tot = mx;
	int k = (tot - mx / 2);
	s.push(k);
	s.push(mx / 2);
	q2.push(tot - mx / 3);
	q2.push(mx / 3);
	mx = min(mx, 1 + solve3(q2));
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
	//if (ans2 != ans)
	//	throw 34;
	return ans2;
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

bool solve4()
{
	bool fCan = false;
	int x, r, c;
	cin >> x >> r >> c;
	if (r > c) swap(r, c);
	if (x == 1)
		return true;
	if (x == 2)
	{
		if (c < 2)
			return false;
		return (r * c) % 2 == 0;
	}
	if (x == 3)
	{
		if (c < 3)
			return false;
		if (r == 1)
			return false;
		if (r == 2)
		{
			if (c == 3)
				return true;
			else
				return false;
		}
		if (r == 3)
		{
		return true;
		}
		return false;
	}
	if (x == 4)
	{
		return r > 2 && (r * c % 4 == 0);
	}
	return fCan;
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
		cout << solve5();
		cout << endl;
	}
	return 0;
}