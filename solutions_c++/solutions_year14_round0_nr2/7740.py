#include <iomanip>
#include <iostream>

double solve(double c, double f, double x) {
	double factories = 0.0;
	double last = x + 100.0;
	for (int k = 0; true; ++k) {
		if (k > 0) {
			factories += c / (2.0 + f * (k - 1));
		}
		double res = factories + x / (2.0 + f * k);
		if (res > last) {
			return last;
		} else {
			last = res;
		}
	}
}

int main() {
	std::cout << std::setprecision(15);
	int cases;
	std::cin >> cases;
	for (int case_num = 1; case_num <= cases; ++case_num) {
		double c, f, x;
		std::cin >> c >> f >> x;
		std::cout << "Case #" << case_num << ": " << solve(c, f, x) << std::endl;
	}

	return 0;
}
