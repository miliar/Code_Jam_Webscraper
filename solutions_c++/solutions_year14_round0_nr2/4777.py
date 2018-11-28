#include <stdio.h>

int t, cases;
double c, f, x, res, temp;

void rec(double rate, double time) {
	if(time < res) {
		temp = x / rate;
		if(temp + time < res) {
			res = time + temp;
		}
		rec(rate + f, (time + (c/rate)));
	}	
}

int main() {
	cases = 1;
	scanf("%d", &t);
	while(t--) {
		scanf("%lf %lf %lf", &c, &f, &x);
		res = 1000000000.0;
		rec(2.0, 0.0);
		printf("Case #%d: %.7lf\n", cases++, res);
	}
	return 0;
}