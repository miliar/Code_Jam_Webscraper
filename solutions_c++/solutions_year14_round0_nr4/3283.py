#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;



void solve()
{
	int n;
	cin >> n;
	vector<double> a(n), b(n);
	for (int i = 0; i < n; ++i)
		cin >> a[i];
	for (int i = 0; i < n; ++i)
		cin >> b[i];
	sort(a.begin(), a.end());
	reverse(a.begin(), a.end());
	sort(b.begin(), b.end());
	reverse(b.begin(), b.end());
	int fa = 0;
	int i = 0;
	int j = 0;
	for (; i < n; ++i)
	{
		if (a[i] > b[j])
			++fa;
		else
			++j;
	}
	int sa = 0;
	reverse(a.begin(), a.end());
	reverse(b.begin(), b.end());
	i = 0;
	j = 0;
	for (; i < n; ++i)
	{
		if (a[i] > b[j])
		{
			++sa;
			++j;
		}
	}
	cout << sa << " " << fa;
}

void main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
}