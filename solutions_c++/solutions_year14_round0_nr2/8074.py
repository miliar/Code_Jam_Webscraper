#include <iostream>
#include <iomanip>

int main() {
	int N;
	double C, F, X, total, speed, time;
	bool b;
	std::cin >> N;
	std::cout << std::setprecision(7) << std::fixed;
	for (int i = 1; i <= N; i++) {
		speed = 2.0;
		total = 0.0;
		b = true;
		std::cin >> C >> F >> X;
		while (b) {
			time = C / speed + X / (speed + F);
			if (time < X / speed) {
				total += C / speed;
				speed += F;
			} else {
				total += X / speed;
				b = false;
			}
		}
		std::cout << "Case #" << i << ": " << total << std::endl;
	}
}
