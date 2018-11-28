#include <vector>
#include <string>
#include <iostream>
#include <algorithm>

void flip(std::vector<bool>& cakes, int index) {
	for (int i = 0; i <= index; ++i) {
		cakes[i] = !cakes[i];
	}
}

int main() {
	int t;
	std::cin >> t;

	for (int i = 1; i <= t; ++i) {
		std::string series;
		std::cin >> series;
		std::vector<bool> cakes(series.size(), false);

		for (int j = 0; j < series.size(); ++j) {
			if (series.at(j) == '+') {
				cakes[j] = true;
			}

		}

		int count = 0;
		while (std::find(cakes.begin(), cakes.end(), false) != cakes.end()) {
			bool first = cakes[0];

			int index = 0;
			for (int j = 1; j < cakes.size(); ++j) {
				if (cakes[j] != first) break;
				++index;
			}

			flip(cakes, index);
			++count;
		}

		std::cout << "Case #" << i << ": " << count << std::endl;
	}

	return 0;
}
