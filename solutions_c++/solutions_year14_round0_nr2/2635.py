#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	cout.precision(10);

	int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
		double C, F, X; cin >> C >> F >> X;

		double time = 0;
		double S = 2;
		while ((X-C) * (S+F) > X * S) {
			time += C/S;
			S += F;
		}

		time += X/S;

		cout << "Case #" << t << ": " << time << endl;
	}

	return 0;
}