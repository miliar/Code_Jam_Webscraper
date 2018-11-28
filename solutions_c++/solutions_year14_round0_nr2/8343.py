#include <iostream>

int main() {

	int T;
	std::cin >> T;
	std::cout.precision(7);
	for (int t = 1; t <= T; t++) {
		double C, F, X;
		std::cin >> C >> F >> X;

		double t0 = X / 2, t1;
		double s = 0;
		for (int k = 1; ; k++) {
			s += C / (2 + (k - 1) * F);
			t1 = s + X / (2 + k * F);
			if (t1 > t0)
				break;
			else
				t0 = t1;
		}
		std::cout << "Case #" << t << ": " << std::fixed << t0 << std::endl;
	}

	return 0;
}