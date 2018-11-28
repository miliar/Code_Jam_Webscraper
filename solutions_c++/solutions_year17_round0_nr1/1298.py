#include <iostream>
#include <vector>
#include <string>

int main() {

	int t;
	std::cin >> t;

	for (auto i = 1; i <= t; i++) {
		std::string cakes;
		int flipper;
		std::cin >> cakes >> flipper;
		int ret = 0;
		for (auto j = 0; j <= cakes.size() - flipper; j++) {
			if (cakes[j] == '+') {
				continue;
			}
			else { // flip
				ret++;
				for (auto k = 0; k < flipper; k++) {
					cakes[k + j] = (cakes[k + j] == '+') ? '-' : '+';
				}
			}
		}

		bool allGood = true;
		for (auto j = 0; j < cakes.size(); j++) {
			if (cakes[j] == '-') {
				allGood = false;
				break;
			}
		}

		if (allGood) {
			std::cout << "Case #" << i << ": " << ret << "\n";
		}
		else {
			std::cout << "Case #" << i << ": IMPOSSIBLE\n";

		}

	}

	return 0;
}