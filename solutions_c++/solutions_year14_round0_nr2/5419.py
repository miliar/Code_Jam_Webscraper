#include <bits/stdc++.h>
using namespace std;
void func() {
	double C, F, X;
	cin >> C >> F >> X;
	double R = 2;
	double T = 0;
	double r = 1e+300;
	for (;;) {
		double rr = T + X / R;
		if (rr > r) break;
		r = rr;
		T += C / R;
		R += F;
	}
	printf("%.7f\n", r);
}
int main() {
	int T;
	cin >> T;
	for (int tt = 1; tt <= T; ++ tt) {
		cout << "Case #" << tt << ": ";
		func();
	}
}
