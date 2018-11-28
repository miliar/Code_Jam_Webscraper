#include <stdio.h>
#include <stdlib.h>

int process(int caseNum) {
	double c, f, x, time;
	double farm = 0.0;
	double min = NULL;
	double base = 2.0;

	scanf("%lf %lf %lf", &c, &f, &x);

	while(1) {
		time = x/base;
		time += farm;
		if(min == NULL || min > time) {
			min = time;
		}
		else {
			break;
		}
		farm += c/base;
		base += f;
	}

	printf("Case #%d: %.7lf\n", caseNum, min);

	return 0;
}

int main() {
	int i, t;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		process(i);
	}
	return 0;
}