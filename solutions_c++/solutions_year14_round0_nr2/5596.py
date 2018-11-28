#include <stdio.h>

#define COOKIE_RATE (2.0f)

double C, F, X;


float yolocookie(int depth = 0, double time = 0.0f) {
	double nextfarmtime = C / (COOKIE_RATE + depth*F) + time;
	double nextgoaltime = X / (COOKIE_RATE + (depth + 1)*F) + nextfarmtime;
	double goaltime = X / (COOKIE_RATE + depth*F) + time;
	if (goaltime <= nextgoaltime)
		return goaltime;
	return yolocookie(depth+1, nextfarmtime);
}

int main(int argc, char** argv) {
	int T;
	scanf("%d%*c", &T);
	for (int i = 0; i < T; ++i) {
		scanf("%lf %lf %lf", &C, &F, &X);
		printf("Case #%d: %.7lf\n", i + 1, yolocookie());
	}
	return 0;
}