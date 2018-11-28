#include <stdio.h>
#include <string.h>
#include <math.h>
#include <algorithm>

using namespace std;

double c, f, x;

double count (int n) {
	double ans = 0;
	for (int i = 0; i < n; i++)
		ans += c/(2 + i*f);
	ans += x/(2 + n*f);
	return ans;
}

int main () {
	int cas;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; i++) {
		scanf("%lf%lf%lf\n", &c, &f, &x);
		int n = floor((f*x - 2*c) / (f*c));
		n = max(n, 0);
		double ansN = count(n);
		double ansM = count(n+1);
		printf("Case #%d: %.7lf\n", i, min(ansN, ansM));
	}
	return 0;
}
