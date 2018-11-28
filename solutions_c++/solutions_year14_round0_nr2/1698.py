#include<iostream>
#include<cstring>
#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;
double check(int t, double c, double x, double f)
{
	double ans = 0;
    double r = 2;
	for (int i = 0; i < t; i++)	{
        ans += c / r;
        r += f;
	}
	ans += x / r;
	return ans;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    double c, x, f;
    for (int cas = 1; cas <= T; cas++) {
        cin >> c >> f >> x;
        double t = (x - c - 2 * c / f) / c;
        double ans = check(int(ceil(t) + 1e-7), c, x, f);
        ans = min(ans, check(int(ceil(t) + 1e-7), c, x, f));
		printf("Case #%d: %.7f\n", cas, ans);
	}
	return 0;
}
