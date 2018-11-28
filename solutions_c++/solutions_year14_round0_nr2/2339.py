#include <iomanip>
#include <iostream>
#include <limits>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	cout << fixed << setprecision(7);
	for(int test = 1; test <= tests; ++test) {
		double cost, delta, goal, rate = 2.0, time = 0.0, best = numeric_limits<double>::max();
		cin >> cost >> delta >> goal;
		while(time + goal / rate <= best) {
			best = time + goal / rate;
			time += cost / rate;
			rate += delta;
		}
		cout << "Case #" << test << ": " << best << '\n';
	}
	return 0;
}
