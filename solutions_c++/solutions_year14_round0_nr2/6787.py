#include <iostream>
using namespace std;

int main(void) {
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		const double amortization_time = C / F;

		double time = 0;
		int farms = 0;
		while(true) {
			const double waiting_time = C / (2. + F * farms);
			if(amortization_time + waiting_time < X / (2. + F * farms)) {
				time += waiting_time;
				farms++;
			} else {
				time += X / (2. + F * farms);
				break;
			}
		}

		cout << "Case #" << i << ": ";
		cout.precision(7);
		cout << fixed << time;
		cout << endl;
	}
	return 0;
}
