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

double eps = 1e-7;
bool eq(double d1, double d2)
{
	return fabs(d1 - d2) < eps;
}

double solve(int n, double v, double x, double r1, double r2, double c1, double c2)
{
	if (r1 == 0)
		return -1;
	
	double timeRight = v / r1;
	
	if (c1 < x && c2 < x)
		return -1;
	if (c1 > x && c2 > x)
		return -1;

	double timeLeft = 0;
	double v2 = 0, cc = -1, time = 0;
	while (timeRight - timeLeft > 1e-15)
	{
		time = (timeRight + timeLeft) / 2;
		if (time == timeRight || time == timeLeft)
			break;
		double v1 = time * r1;

		double t = (v - v1) / (r1 + r2);

		v1 += r1 * t;
		v2 = r2 * t;

		cc = (v1 * c1 + v2 * c2) / (v1 + v2);
		
		if (c2 <= x)
		{
			if (cc >= x)
				timeRight = time;
			else
				timeLeft = time;
		}
		else
		{
			if (cc <= x)
				timeRight = time;
			else
				timeLeft = time;
		}

	}
	
	double v1 = v - v2;
	if (eq(cc, x))
		return v1 / r1;

	return -1;
}

void solve()
{
	int n;
	double v, x, r1 = 0, r2 = 0, c1 = 0, c2 = 0;
	cin >> n >> v >> x;

	cin >> r1 >> c1;
	if (n == 2)
		cin >> r2 >> c2;


	double res1 = solve(n, v, x, r1, r2, c1, c2);
	double res2 = solve(n, v, x, r2, r1, c2, c1);
	cout.setf(6);
	if (res1 > 0)
	{
		if (res2 > 0)
			printf("%.7lf" , min(res1, res2));
		else
			printf("%.7lf", res1);
	}
	else
		if (res2 > 0)
			printf("%.7lf", res2);
		else
			cout << "IMPOSSIBLE";
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
		solve();
		cout << endl;
	}
	return 0;
}