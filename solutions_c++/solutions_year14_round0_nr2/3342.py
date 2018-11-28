#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>

using namespace std;

typedef long double ld;

const ld EPS = 1e-15;

double solve()
{
	ld c, f, x;
	cin >> c >> f >> x;
	if (x <= c)
		return x / 2;
	ld step = 2,
		cookie_count = 0,
		time = 0;
	while (x / step > (c / step + x / (step + f)) + EPS)
	{
		time += c / step;
		step += f;
	}
	return time + x/step;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	cin >> t;
	cout.precision(10);
	for (int i = 1; i <= t; ++i)
	{
		ld ans = solve();
		cout << "Case #" << i << ": " << ans << endl;
	}
}