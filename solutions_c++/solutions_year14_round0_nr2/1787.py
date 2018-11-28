#include <iostream>
#include <vector>
using namespace std;

#define INF 0x7fffffff

int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);

	int T, cs;
	scanf("%d", &T);
	for (cs = 1; cs <= T; ++cs)
	{
		double c, f, x;
		int i;
		double ans = INF, t = 0.0;
		scanf("%lf%lf%lf", &c, &f, &x);
		for (i = 0; i < x; ++i)
		{
			ans = min(ans, t + x / (2 + i * f));
			t += c / (2 + i * f);
		}
		printf("Case #%d: ", cs);
		printf("%.8lf\n", ans);
	}
}