#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t=1 ; t<=T ; t++) {
		double C, F, X;
		cin >> C >> F >> X;
		double temp, acum=0.0, rate=2.0, best=X/2.0;
		while (acum<best) {
			acum += C/rate;
			rate += F;
			temp = acum + X/rate;
			if (temp < best)
				best = temp;
		}
		printf("Case #%d: %.7lf\n",t,best);
	}
	return 0;
}