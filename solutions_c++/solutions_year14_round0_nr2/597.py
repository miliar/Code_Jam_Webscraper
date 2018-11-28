#include <iostream>
#include <iomanip>

int main() {
	int T;
	std::cin >> T;
	for (int i=0; i<T; i++) {
		double C, F, X;
		std::cin >> C >> F >> X;
		double rate = 2, time = 0;
		while (C/rate + X/(rate+F) < X/rate) {
			time += C/rate;
			rate += F;
		}
		std::cout << std::fixed << std::setprecision(6) << time + X/rate << std::endl;
	}
	return 0;
}
