#include	<iostream>
#include	<ostream>
#include	<set>
using namespace std;

int main(void) {
	int T; cin >> T;

	cout.precision(7);
	cout.setf(ios::fixed);
	for (int t = 1; t <= T; ++t) {
		double	C, F, X;
		cin >> C >> F >> X;

		double	rate = 2.0, total_time = 0;
		while (1) {
			double	time_to_win = X / rate;
			double	time_till_farm = C / rate;
			double	time_to_win_with_farm = time_till_farm + X / (rate + F);

			if (time_to_win > time_to_win_with_farm) {
				total_time += time_till_farm;
				rate += F;
			} else {
				total_time += time_to_win;
				break;
			}
		}

		cout << "Case #" << t << ": " << total_time << endl;
	}

	return 0;
}