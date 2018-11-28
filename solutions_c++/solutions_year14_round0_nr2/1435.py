#include <cstdio>
#include <iostream>
using namespace std;

int nTest;
double c, f, x;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &nTest);
	for(int test = 1; test <= nTest; test++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		double a = 2;
		double result = x/a, total = 0;		
		for(int i = 1; i <= 4000000; i++) {
			result = min(result, total + x/a);
			total += c/a;
			a += f;
		}
		printf("Case #%d: %.10lf\n", test, result);
	}

	return 0;
}