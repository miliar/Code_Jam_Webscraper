#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int T; cin >> T;
	for (int t = 0; t < T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		double mintime = X / 2.0f;
		if (X > C) {
			for (int t = 1;; ++t){
				double elapsedtime = 0.0f;
				for (int i = 0; i < t; ++i) {
					elapsedtime += C / (2.0f + i*F);
				}
				elapsedtime += X / (2.0f + t*F);
				if (mintime > elapsedtime) mintime = elapsedtime;
				else break;
			}
		}
		printf("Case #%d: %.7f\n", t + 1, mintime);
	}
}