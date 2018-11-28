#include <iostream>
#include <cstdio>
#include <map>

using namespace std;

int main() {
	int T;
	double C, F, X, N, tAll, t1, t2;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> C >> F >> X;
		tAll = 0;
		N = 2;
		while (1) {
			t1 = X/N;
			t2 = C/N + X/(N+F);
			if (t1 > t2) {
				tAll += C/N;
				N += F;
			} else {
				break;
			}
		}
		tAll += t1;

		printf("Case #%d: %.7f\n", i, tAll);
	}
}