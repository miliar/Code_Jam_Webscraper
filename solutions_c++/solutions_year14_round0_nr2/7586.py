#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;


int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		double C, F, X;
		scanf("%lf %lf %lf", &C, &F, &X);

		double min_time = X / 2.0;
		
		double time = 0.0;
		for (double cps = 2.0; time < min_time; cps += F) {
			double t = X / cps;
			if (time + t < min_time) {
				min_time = time + t;
			}
			double u = C / cps;
			time += u;
		}

		printf("Case #%d: %.07f\n", Ti, min_time);
	}
	return 0;
}
