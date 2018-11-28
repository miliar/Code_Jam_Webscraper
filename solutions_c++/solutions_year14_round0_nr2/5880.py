#include <cstdio>
using namespace std;

int T;

int main() {
	freopen("cookieclicker.in", "r", stdin);
	freopen("cookieclicker.out", "w", stdout);

	scanf("%d", &T);

	for(int i = 0; i < T; i++) {
		double c, f, x;

		scanf("%lf%lf%lf", &c, &f, &x);

		double r = 2.0f;
		double t = x/r;
		double cu = c/r;

		for(;;) {
			r += f;
			double temp = x/r + cu;
			if(temp < t) t = temp;
			else break;
			cu += c/r;
		}

		printf("Case #%d: %7f\n", i+1, t);
	}
}
