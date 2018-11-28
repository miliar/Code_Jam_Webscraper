#include <cstdio>
#include <iostream>
using namespace std;

int main(int argc, char** argv) {
	int T;
	FILE *in, *out;
	in = fopen("input", "r");
	out = fopen("output", "w");

	fscanf (in, "%d", &T);
	for (int i = 1; i <= T; i++) {
		double C, F, X, PR = 2.0, timeToX = 0.0;
		fscanf(in, "%lf %lf %lf", &C, &F, &X);
		double lazyTime = 0.0, timeToFarm = 0.0;
		do {
			timeToX += timeToFarm;
			lazyTime = X/PR;
			timeToFarm = C/PR;
			PR = PR+F;
		} while (timeToFarm + X/PR < lazyTime);
		timeToX += lazyTime;
		fprintf(out ,"Case #%d: %.7lf\n", i, timeToX);
	}
	fclose (in);
	fclose (out);
	return 0;
}
