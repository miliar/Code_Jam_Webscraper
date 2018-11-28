
#include <iostream>

int main() {
	unsigned N;
	std::cin >> N;
	std::cout.precision(10);
	for (unsigned c = 1; c <= N; ++c) {
		double C, F, X;
		std::cin >> C >> F >> X;
		double timeWithoutFarm = X / 2;
		double bestTime = timeWithoutFarm;
		for (unsigned farms = 1;; ++farms) {
			double time = 0;
			for (unsigned i = 0; i < farms; ++i)
				time += C / (2 + i * F);
			if (time >= timeWithoutFarm)
				break;
			time += X / (2 + farms * F);
			if (time < bestTime)
				bestTime = time;
			else
				break;
		}
		std::cout << "Case #" << c << ": " << bestTime << std::endl;
	}
	return 0;
}
