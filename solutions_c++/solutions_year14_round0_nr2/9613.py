#include <iostream>
#include <iomanip>

using namespace std;
double C, F, X;
double best;

void rec(double cookies, double freq, double time) {
	if (time > best) {
		return;
	}
	if (cookies >= X) {
		best = min(best, time);
		return;
	}
	double diff = X - cookies;
	best = min(best, time + (diff/freq));
	diff = C - cookies;
	rec(0, freq + F, time + (diff/freq));
}

int main() {
	cout << setprecision(12);
	int k;
	cin >> k;
	for (int i = 0; i < k; i++) {
		cout << "Case #" << (i + 1) << ": ";
		cin >> C >> F >> X;
		best = 100000;
		rec(0, 2, 0);
		cout << best << endl;
	}

}
