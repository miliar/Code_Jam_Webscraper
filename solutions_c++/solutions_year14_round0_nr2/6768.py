#include <cstdio>

int main() {
	//freopen("b.in", "r", stdin);
	//freopen("b.out", "w", stdout);
	int Q;
	scanf("%d", &Q);
	for (int kcase = 1; kcase <= Q; ++kcase) {
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double t = 0.0, res = x/2.0;
		int buy = 0;
		for (;; ++buy) {
			if (c/(buy*f + 2) + t + x/((buy+1)*f + 2) < res) {
				res = c/(buy*f + 2) + t + x/((buy+1)*f + 2);
				t += c/(buy*f + 2);
			} else {
				break;
			}
		}
		printf("Case #%d: %.7lf\n", kcase, res);
		//cout << "Case #" << kcase << ": " << setprecision(7) << res << endl;
	}
	return 0;
}
