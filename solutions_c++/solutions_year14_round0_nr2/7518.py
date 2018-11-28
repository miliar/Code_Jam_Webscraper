#include <iostream>
#include <vector>
#include <iomanip>

int T;
double C, F, X;
double t, rate;


void init() {
	t = 0.0;
	rate = 2.0;
}

bool shoudBuy() {
	double t1 = X / rate;
	double t2 = C / rate + X / (rate + F);
	return t1 > t2;
}

void solveCase() {
	init();
	std::cin >> C >> F >> X;
	while (shoudBuy()) {
		t += C / rate;
		rate += F;
	}

	t += X / rate;
	std::cout << std::setprecision(15) << t;
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	std::cin >> T;
	for (int i = 1; i < T + 1; ++i)
	{
		std::cout << "Case #" << i << ": ";
		solveCase();
		if (i < T)
			std::cout << std::endl;
	}
	return 0;
}