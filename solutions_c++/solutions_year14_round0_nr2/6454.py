#include <cstdio>
#include <iostream>
using namespace std;

double C, F, X;

double solution(double P, double max) {
	double a, b;
	a = X / P;
	if (a > max) {
		return a;
	}
	b = C/P;
	b += solution(P+F, a-b);
	return a<b?a:b;
}

int main() {
	int T, cnt = 1;

//  freopen("B-large.in", "r", stdin);
//  freopen("output_large.out", "w", stdout);

	for (cin >> T; T--;) {
		cin >> C >> F >> X;
		printf("Case #%d: %.7lf\n", cnt++, solution(2, X));
	}

	return 0;
}
