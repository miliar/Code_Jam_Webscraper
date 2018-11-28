#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>

typedef long long int ll;

int main(int argc, char *argv[])
{
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout << std::setprecision(9);

	int ncases;
	std::cin >> ncases;

	for (int i = 1; i <= ncases; i++) {
		int n;
		double v, x;
		std::vector<double> rate;
		std::vector<double> temperture;
		std::cin >> n >> v >> x;

		rate.resize(n);
		temperture.resize(n);

		for (int j = 0; j < n; j++) {
			std::cin >> rate[j] >> temperture[j];
		}

		std::cout << "Case #" << i << ": ";
		if (n == 1) {
			double t = v / rate[0];
			if (std::abs(temperture[0] - x) < 10e-6) {
				std::cout << t << std::endl;
			} else {
				std::cout << "IMPOSSIBLE" << std::endl;
			}

		} else if (n == 2) {
			double t0, t1;
			if (std::abs(temperture[0] - temperture[1]) < 10e-6) {
				if (std::abs(temperture[0] - x) > 10e-6) {
					std::cout << "IMPOSSIBLE" << std::endl;
				} else {
					std::cout << v / (rate[0] + rate[1]) << std::endl;
				}
			} else {
				t0 = v * (x - temperture[1]) / (temperture[0] - temperture[1]) / rate[0];
				t1 = v * (temperture[0] - x) / (temperture[0] - temperture[1]) / rate[1];
				if (t0 >= 0 && t1 >= 0) {
					std::cout << std::max(t0, t1) << std::endl;
				} else {
					std::cout << "IMPOSSIBLE" << std::endl;
				}
			}
		}
	}
	
	return 0;
}