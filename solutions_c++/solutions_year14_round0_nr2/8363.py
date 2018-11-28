#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;

	for(int tc = 1; tc <= t; tc++) {
		double c, f, x, r = 2.0;
		cin >> c >> f >> x;

		double cur_time = 0, cur_comp_time = x/r;
		while(true) {
			double cb_time = c/r;
			double new_time = cur_time + cb_time + (x/(r + f));

			if(new_time < cur_comp_time) {
				cur_time += cb_time;
				cur_comp_time = new_time;
				r += f;
			
			} else break;
		}

		printf("Case #%d: %.7f\n", tc, cur_comp_time);
	}

	return 0;
}
