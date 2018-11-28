#include <cstdio>
#include <algorithm>

using namespace std;

int T;
double C, F, X;

int main(void){
	int t;

	scanf("%d", &T);

	for (t = 1; t <= T; t++){
		double curr = 0, rate = 2, acc = 0, best;
		scanf("%lf %lf %lf", &C, &F, &X);

		best = X / rate;

		for (; acc < best; acc += C/rate, rate += F)
			best = min(best, acc + X / rate);

		printf("Case #%d: %lf\n", t, best);
	}

	return 0;
}
