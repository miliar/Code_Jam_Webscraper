#include <cstdio>
#include <cstring>
#include <cstdlib>

double C, F, X;

void input() {
	scanf("%lf%lf%lf", &C, &F, &X);
}

void output() {
	double res = X/2;
	double number = 2;
	double time1 = 0;

	for(int i = 1;;i ++) {
		time1 += C/number;
		number += F;

		double tmp = time1 + X/number;
		if(tmp < res) res = tmp;
		else break;
	}

	printf("%.7lf\n", res);
}

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		output();
	}
	return 0;
}