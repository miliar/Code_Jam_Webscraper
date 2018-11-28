#include <cstdio>

using namespace std;

int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t ++){
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double need = 0, speed = 2, ans = x / 2;
		for (int i = 0; i < x; i ++){
			double cur = need + x / speed;
			if (cur < ans)
				ans = cur;
			need += c / speed;
			speed += f;
		}
		printf("Case #%d: %.8lf\n", t+1, ans);
	}
	return 0;
}
