#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		double C, F, X, rate = 2, time = 0; 
		cin >> C >> F >> X;
		while (X/rate > C/rate + X/(rate + F)) {
			time += C/rate;
			rate += F;
		}
		time += X/rate;
		cout << "Case #" << i << ": ";
	       	printf("%.7lf\n", time);	
	}
}
