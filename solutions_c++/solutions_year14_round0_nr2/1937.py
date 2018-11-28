#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
int t;
double c, f, x;

int main()
{
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		double ans = 0;
		int k = 1;
		while (x / (2 + k * f - f) > c / (2 + k * f - f) + x / (2 + k * f))
		{
			ans += c / (2 + k * f - f);
			k++;
		}
		ans += x / (2 + k * f - f);
		printf("Case #%d: %.8lf\n", tt, ans);
	}
	return 0;
}
