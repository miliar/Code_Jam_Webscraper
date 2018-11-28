#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>

using namespace std;

double time_to_finish(double cookies, int farms, double C, double F, double X) {
	return max((X-cookies)/(2 + (double)farms*F), 0.0);
}

double time_to_next_farm(double cookies, int farms, double C, double F, double X) {
	return max((C-cookies)/(2 + (double)farms*F), 0.0);
}

bool should_buy(double cookies, int farms, double C, double F, double X) {
	double tfarm = time_to_next_farm(cookies, farms, C, F, X);
	double tfin = time_to_finish(cookies, farms, C, F, X);

	if (tfarm + time_to_finish(cookies-C+2*tfarm+(double)farms*F*tfarm, farms+1, C, F, X) < tfin)
		return true;
	else
		return false;
}

int main() {
	int T;
	cout << fixed << setprecision(7);
	cin >> T;
	for (int i = 1; i <= T; i++) {
		double C, F, X;
		cin >> C >> F >> X;
		double t = 0.0, cookies = 0.0;
		int farms = 0;
		while (should_buy(cookies, farms, C, F, X)) {
			double time =  time_to_next_farm(cookies, farms, C, F, X);
			t += time;
			cookies += 2*time + farms*F*time - C;
			farms++;
		}
		t += time_to_finish(cookies, farms, C, F, X);
		cout << "Case #" << i << ": " << t << endl;
	}
	return 0;
}
