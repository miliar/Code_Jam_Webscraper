#include<iostream>
#include<cstdio>
#include<string>
#include<set>
#include<algorithm>
#include<vector>
#include<map>
#include<cmath>
#include<queue>
using namespace std;

long long f[200], t[200];
long long V, T;

const double EPS = 1e-8;

bool ls(double a, double b)
{
	return a < b && abs(a - b) > EPS;
}

long long scand()
{
	int a, b;
	scanf("%d.%d", &a, &b);
	return a * 10000 + b;
}

void solve()
{
	int n;
	cin >> n;
	V = scand();
	T = scand();
	for (int i = 0; i < n; i++)
	{
		f[i] = scand();
		t[i] = scand();
	}

	if (n == 1)
	{
		f[n] = 0;
		t[n] = t[0];
		n++;
	}

	long long x = t[0], y = t[1];
	
	if (x == y)
	{
		f[0] += f[1];
		if (x != T)
		{
			printf("IMPOSSIBLE");
			return;
		}
		printf("%.10lf", 1.0 * V / f[0]);
		return;
	}

	if (max(x, y) < T || min(x, y) > T)
	{
		printf("IMPOSSIBLE");
		return;
	}

	double u = 1.0 * (T * V - V * y) / (x - y);
	double v = V - u;
	double rest = (u * x + v * y) / (v + u);
	
	double res = max(u / f[0], v / f[1]);
	printf("%.10lf", res);
}

int main()
{
#ifdef LOCAL
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
#endif

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		solve();
		printf("\n");
	}
}