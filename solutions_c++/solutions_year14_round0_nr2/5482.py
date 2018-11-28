# include <cstdio>
# include <cmath>

double C;
double F;
double X;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("outb.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; ++i) {
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ", i);
		int k = ceil( (X*F-2*C)/(C*F) - 1 );
		if (k <= 0) k = 0;
		double ans = 0;
		for (int j = 0; j < k; ++j) {
			ans += C/(j*F+2);
		}
		ans += X/(k*F+2);
		printf("%.7lf\n", ans);
	}

	return 0;
}

