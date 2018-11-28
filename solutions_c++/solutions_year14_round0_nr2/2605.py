#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		cout << "Case #" << test << ": ";
		double C, F, X; cin >> C >> F >> X;
		double res = 9876543210.0;
		double curGet = 2.0;
		double curTime = 0.0;
		for (int buy = 0; buy - 1e-4 < X; ++buy) {
			res = min(res, X / curGet + curTime);
			curTime += C / curGet;
			curGet += F;
		}
		printf("%.7lf\n", res);
	}
	return 0;
}