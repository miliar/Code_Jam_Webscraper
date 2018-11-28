#include <iostream>
#include <cfloat>
#include <iomanip>

using namespace std;

int main() {
	int T;
	cin >> T;
	cout << setprecision(7) << fixed;
	for (int t = 1; t <= T; ++t) {
		double C, F, X;
		cin >> C >> F >> X;
		double answer = DBL_MAX;
		double time = 0;
		double rate = 2;
		while (time <= answer) {
			double time_to_win = X / rate;
			double time_to_farm = C / rate;
			answer = min(answer, time + time_to_win);
			time += time_to_farm;
			rate += F;
		}
		cout << "Case #" << t << ": " << answer << endl;
	}
}
