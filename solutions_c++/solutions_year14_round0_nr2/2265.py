#include <cstdio>
#include <iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int i = 0; i < T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double rate = 2.0, secs = 0.0;		
		while (C/rate + (X/(rate+F)) < X/rate) {		
			secs += C/rate;
			rate += F;
		}
		secs += X/rate;
		printf("Case #%d: %.7f\n", i+1, secs);
	}
	return 0;
}

