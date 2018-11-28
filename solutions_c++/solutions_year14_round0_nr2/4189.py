#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		double c, f, x;
		cin >> c >> f >> x;

		double cookie_rate = 2.0;
		double time_needed = x / cookie_rate;
		double time_pasted = 0.0;
		while (1) {
			time_pasted += c / cookie_rate;
			cookie_rate += f;
			double tn = time_pasted + x / cookie_rate;
			if (tn >= time_needed) {
				break;
			}
			time_needed = tn;
		} 
		printf("Case #%d: %f\n", t, time_needed);
	}
	return 0;
}