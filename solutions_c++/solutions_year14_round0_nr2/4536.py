#include <cstdio>
#include <cstring>
#define EPS (1e-10)
using namespace std;

double farmCost, farmRate, target;

inline void solve() {
	double fromFarms = 0.0;
	double oldans = 0.0;
	double rate = 2.0;
	double ans = target / rate;

	do {
		oldans = ans;
		fromFarms += farmCost / rate;
		rate += farmRate;
		ans = fromFarms + target / rate;
	} while (oldans+EPS > ans);

	printf("%.8lf\n", oldans);
}

inline void read() {
	scanf("%lf %lf %lf", &farmCost, &farmRate, &target);
}

int main() {
	int brt;
	scanf("%d", &brt);

	for (int test=0; test < brt; ++test) {
		printf("Case #%d: ", test+1);
		fprintf(stderr, "Case #%d ...\n", test+1);
		read();
		solve();
	}
	return 0;
}