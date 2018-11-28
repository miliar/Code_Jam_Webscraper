#include <iostream>

using namespace std;

#define EPSILON 0.000001

int main() {
	int T;
	cin >> T;
	cout.precision (7);
	for (int i = 0; i < T; ++i) {
		double C, F, X;
		cin >> C >> F >> X;
		double rate = 2;
		double current = 0;
		double time;
		double proposed;
		while ((time = X / rate) + current > (current + (proposed = (C / rate + (X / (rate + F)))))) {
			current += C / rate;
			rate += F;
		}
		current += time;
		cout << "Case #" << i + 1 << ": " << fixed << current << endl;
	}
	return 0;
}