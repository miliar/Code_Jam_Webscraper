#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;

double C, F, X;

int main() {
	freopen("B-large.in","r", stdin);
	freopen("B-large.out","w", stdout);
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti ++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		printf("Case #%d: ", ti);
		int n = (int)(X / C - 2 / F + 1);
		double best = X / 2.0;
		double sa = 0.0;
		for (int i = 1; i <= n + 5; i ++) {
			sa += C / (2 + (i-1) * F);
			double f = sa + X / (2 + i * F);
			if (f < best) best = f;
		}
		printf("%.7lf\n", best);
	}
	return 0;
}
