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

double time(double V, double C,
	double v1, double C1,
	double v2, double C2)
{
	double a1 = v1, b1 = v2, c1 = V;
	double a2 = (C - C1) * v1, b2 = (C - C2) * v2, c2 = 0;
	double cc = a1 / a2;
	b2 *= cc;
	b2 -= b1; c2 = -c1;
	double y = c2 / b2;
	double x = (c1 - b1 * y) / a1;
	if ((x < 0) || (y < 0)) return -1;
	return x + y;
}

void solve()
{
	int N;
	double V, X;
	double r1, r2, r3;
	double c1, c2, c3;
	cin >> N >> V >> X;
	if (N == 1)
	{
		cin >> r1 >> c1;
		if (X == c1)
		{
			printf("%.9f\n", V / r1);
			return;
		}
		else
		{
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	else if (N == 2)
	{
		cin >> r1 >> c1 >> r2 >> c2;

		if (c1 == c2)
		{
			r1 += r2;
			if (X == c1)
			{
				printf("%.9f\n", V / r1);
				return;
			}
			else
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}

		if (c1 == X)
		{
			printf("%.9f\n", V / r1);
			return;
		}
		
		if (c2 == X)
		{
			printf("%.9f\n", V / r2);
			return;
		}

		r3 = r1 + r2;
		c3 = (c1 * r1 + c2 * r2) / (r1 + r2);
		double t = -1;
		double a1 = time(V, X, r1, c1, r3, c3);
		double a2 = time(V, X, r2, c2, r3, c3);
		if (a1 > 0)
		{
			t = a1;
		}
		if (a2 > 0)
		{
			if ((t == -1) || (t > a2))
				t = a2;
		}
		if (t != -1)
		{
			printf("%.9f\n", t);
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}
	}
}

int main()
{
	//ios_base::sync_with_stdio(false);
	//freopen("d:/input.txt", "rt", stdin);
	int T; std::cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}

	return 0;
}