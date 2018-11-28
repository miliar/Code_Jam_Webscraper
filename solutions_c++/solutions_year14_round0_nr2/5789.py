#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>

using namespace std;

int T;
double C, F, X;

int main(void) {
	scanf("%d", &T);
	for(int t = 1; t <= T; t++) {
		scanf("%lf%lf%lf", &C, &F, &X);

		double gain = 2.0;
		double time = X / gain;
		double past = 0.0;
		for(int i = 1; ; i++) {
			double newTime = past + C / gain + X / (gain + F);
			if(newTime > time) {
				break;
			}
			time = newTime;
			past += C / gain;
			gain += F;
		}

		printf("Case #%d: %.8f\n", t, time);
	}
	return 0;
}
