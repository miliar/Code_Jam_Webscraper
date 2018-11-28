#include <iostream>
#include <iomanip>

#define INIT_CPS 2

double solve(double c, double f, double x)
{
	double cps = INIT_CPS;
	double sec = 0;

	while (true) {
		double sec_not_wait = x / cps;
		double sec_wait = c / cps + x / (cps + f);

		if (sec_not_wait < sec_wait) {
			sec += sec_not_wait;
			break;
		}

		sec += c / cps;
		cps += f;
	}

	return sec;
}

int main()
{
	int cases;

	std::cin >> cases;

	for (int i = 1; i <= cases; i++) {
		double c, f, x;

		std::cin >> c >> f >> x;

		double sec = solve(c, f, x);

		std::cout << "Case #" << i << ": " << std::setprecision(7) << std::fixed << sec << std::endl;
	}

	return 0;
}
