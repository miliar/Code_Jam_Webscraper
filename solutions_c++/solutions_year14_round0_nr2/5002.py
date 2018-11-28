#include <cstdio>
#include <cstdlib>
using namespace std;
double c, f, x, pro, ans, ans1, now;
int T, w;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	while (T--)
	{
		scanf("%lf%lf%lf", &c, &f, &x);
		pro = 2.;
		ans = x / pro;
		now = 0.;
		while (1)
		{
			now += c / pro;
			pro += f;
			ans1 = now + x / pro;
			if (ans < ans1) break;
			ans = ans1;
		}
		printf("Case #%d: ", ++w);
		printf("%.7lf\n", ans);
	}
	return 0;
}
