#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

double c, f, x;
double ans, rate, cur;

void solve()
{
	cin >> c >> f >> x;
	ans = 1e10, rate = 2;
	cur = 0;
	for (int i = 0; i < x + 2; ++i)
	{
		double tmp = x / rate;
		if (ans > tmp + cur)
			ans = tmp + cur;
		cur += c / rate;
		rate += f;
	}
	printf("%.7lf\n", ans);
}

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int i = 1; i <= times; ++i)
	{
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
