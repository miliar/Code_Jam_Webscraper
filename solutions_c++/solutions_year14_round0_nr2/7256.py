#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <iostream>

using namespace std;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("res.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 0; k < t; k++) {
		double farm_cost;
		cin >> farm_cost;
		double farm_profit;
		cin >> farm_profit;
		double X;
		cin >> X;
		double time = 0;
		double rate = 2;
		while (true) {
			double time_farm = farm_cost / rate + X / (rate + farm_profit);
			double time_finish = X / rate;
			if (time_finish < time_farm) {
				time += time_finish;
				break;
			}
			else {
				time += farm_cost / rate;
				rate += farm_profit;
			}
		}
		printf("Case #%d: %.7f\n", k + 1, time);
	}
	return 0;
}