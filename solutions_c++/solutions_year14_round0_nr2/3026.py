#include <iostream>
#include <cstdio>
using namespace std;
double C, F, X;
int T;

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++) {
		double time = 0.0;
		double rate = 2.0;
		cin >> C >> F >> X;
		if (C > X)
			time = X / rate;
		else {
			time += C / rate;
			while (X / (rate + F) < (X - C) / rate) {
				rate += F;
				time += C / rate;
			}
			time += (X - C) / rate;
		
		}

		printf("Case #%d: %.7f\n", i,time);	

	}
}
