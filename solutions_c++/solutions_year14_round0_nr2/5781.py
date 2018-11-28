#include <iostream>
#include <cstdio>

using namespace std;

int main() {

	int T;
	double farm_cost;
	double farm_extra;
	double target;

	cin >> T;

	for (int t = 1; t <= T; t++) {
		// input
		cin >> farm_cost;
		cin >> farm_extra;
		cin >> target;

		// try to buy farm
		int buy_num = 0;
		double best_time = 9999999;
		while (true) {
			double cookie_p_sec = 2;
			double acc_time = 0;
			for (int b = 0; b < buy_num; b++) {
				double time_to_buy_farm = farm_cost / cookie_p_sec;
				cookie_p_sec += farm_extra;
				acc_time += time_to_buy_farm;
			}

			double newtime = (target / cookie_p_sec) + acc_time;
			if (newtime < best_time)
				best_time = newtime;
			else
				break;

			buy_num++;
		}

		// output
		printf("Case #%d: %.7lf\n", t, best_time);
	}

	return 0;
}

