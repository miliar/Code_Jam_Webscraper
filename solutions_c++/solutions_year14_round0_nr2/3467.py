#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;



void solve()
{
	double c, f, x;
	cin >> c >> f >> x;
	double m = x / 2.0;
	double cur = 0;
	double p = 2.0;
	while (cur < m)
	{
		cur += c / p;
		p += f;
		m = min(m, cur + x / p);
	}
	cout.setf(cout.fixed);
	cout.precision(7);
	cout << m;
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