#include <cstdio>
const double eps = 1e-8;
double C, F, X;
double ans;
void solve()
{
	double speed = 2.0;
	ans = X/speed;
	double times = 0.0;
	while (1)
	{
		double producetimes = C/speed;
		if (producetimes + times > ans) break;
		speed += F;
		double tmpans = X/speed+producetimes+times;
		times += producetimes;
		if (tmpans < ans)
		{
			if (ans - tmpans < eps) break;
			ans = tmpans;
		}
	}
	printf("%.8lf\n", ans);
}
int main()
{
	freopen("E:\\My Code\\GCJ\\QR\\B-small-attempt0.in", "r", stdin);
	freopen("E:\\My Code\\GCJ\\QR\\B-small-attempt0.out", "w", stdout);
	int T;
	int Case = 1;
	scanf("%d", &T);
	while (T--)
	{
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ", Case++);
		solve();
	}
	return 0;
}