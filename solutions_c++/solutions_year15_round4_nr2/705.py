#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

const double EPS = 1e-9;
bool EQ(double a, double b) { return abs(a - b) < EPS; }

struct Water {
	double v, x;
	bool operator < (const Water &a) const {
		if(!EQ(x, a.x)) return x < a.x;
		return false;
	}
} w[2];

int main(void) {
	int T;
	scanf("%d", &T);
	for(int kase = 1; kase <= T; kase++) {
		printf("Case #%d: ", kase);

		int n;
		double V, X;

		scanf("%d %lf %lf", &n, &V, &X);
		for(int i = 0; i < n; i++) scanf("%lf %lf", &w[i].v, &w[i].x);

		bool allLess = true, allMore = true;
		for(int i = 0; i < n; i++) {
			if(EQ(w[i].x, X) or w[i].x > X) allLess = false;
			if(EQ(w[i].x, X) or w[i].x < X) allMore = false;
		}

		if(allLess or allMore) {
			printf("IMPOSSIBLE\n");
			continue;
		}

		double mixX = 0, base = 0;
		for(int i = 0; i < n; i++) {
			mixX += w[i].v * w[i].x;
			base += w[i].v;
		}
		mixX /= base;

		if(n == 1) {
			printf("%.10lf\n", V / w[0].v);
			continue;
		}
		if(EQ(X, mixX)) {
			printf("%.10lf\n", V / (w[0].v + w[1].v));
			continue;
		}

		sort(w, w + n);
		if(!EQ(mixX, X) and mixX > X) swap(w[0], w[1]);

		double v0 = w[0].v, x0 = w[0].x, v1 = w[1].v, x1 = w[1].x;

		double a = (v0 * x0 + v1 * x1);
		double b = (v0 + v1);
		double t1 = (a * V - b * V * X) / (a * v1 - b * x1 * v1);
		double t0 = (V - v1 * t1) / b;

		printf("%.10lf\n", t0 + t1);
	}

	return 0;
}
