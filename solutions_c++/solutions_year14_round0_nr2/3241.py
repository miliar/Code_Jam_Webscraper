#include <cstdio>
#include <cstdlib>

void solve(const int case_no) {
	double C, F, X;
	scanf("%lf %lf %lf", &C, &F, &X);
	double rate = 2.0f;
	double base_time = 0;
	double min = X / rate;
	while (true) {
		double time = base_time + (C / rate) + (X / (rate + F));
		if (min < time) {
			printf("Case #%d: %f\n", case_no, min);
			return;
		}
		base_time += C / rate;
		rate += F;
		min = time;
	}
}

int main(int, char**) {
	int case_no;
	scanf("%d", &case_no);
	for (int i=1; i <= case_no; i++) {
		solve(i);
	}
	return EXIT_SUCCESS;
}
