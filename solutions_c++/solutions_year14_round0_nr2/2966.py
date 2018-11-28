#include <cstdio>
using namespace std;

int T;
double C, F, X, produce, times;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.in", "w", stdout);

	scanf("%d", &T);
	for (int no = 1; no <= T; no++) {
		scanf("%lf%lf%lf", &C, &F, &X);
		times = 0.0;
		produce = 2.0;
		while (true) {
			double a = X / produce, // время до X без фермы
				b = C / produce + X / (produce + F); // приобретем ферму
			if (a > b) {
				times += C / produce;
				produce += F;
			} else {
				times += a;
				break;
			}
		}
		printf("Case #%d: %.7lf\n", no, times);
	}
	return 0;
}