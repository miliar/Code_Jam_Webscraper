#include<iostream>
using namespace std;

double C,F,X;

double get_cookie_per_sec(int factories_exist) {
	return 2.0 + factories_exist * F;
}

double get_time_to_fulfill(int factories_exist, double target) {
	return target/get_cookie_per_sec(factories_exist);
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		cin >> C >> F >> X;
		int crnt_factories = 0;
		double elapsed_time = 0.00;
		do {
			double old_total_time = get_time_to_fulfill(crnt_factories, X);
			double extra_time = get_time_to_fulfill(crnt_factories, C);
			double new_total_time = extra_time + get_time_to_fulfill(crnt_factories + 1, X);
			if (new_total_time < old_total_time)  {
				crnt_factories++;
				elapsed_time += extra_time;
			}
			else break;
		} while(true);
		double ans = elapsed_time + get_time_to_fulfill(crnt_factories, X);
		printf("Case #%d: %.7lf\n", tc, ans);
	}	
}
