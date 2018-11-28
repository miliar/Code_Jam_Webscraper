#include <iostream>
#include <set>
#include <cmath>

int main() { int cases; std::cin >> cases; std::cin.get(); // skip endline
	for (int n = 1; n <= cases; ++n) { std::cout << "Case #" << n << ":";
		int K, C, S; std::cin >> K >> C >> S;
		std::set<uint64_t> positions;
		// std::cout << "\n";

		uint64_t k = 0;
		do {
			uint64_t pos = k;
			for (int i = 0; i < C - 1; ++i) {
				// std::cout << "STEP : " << i << " " << k << " " << pos << std::endl;
				pos = pos * K;
				if (k < K - 1) {
					++k;
					pos = pos + k;
					// std::cout << "STEP2: " << i << " " << k << " " << pos << std::endl;
				}
			}
			++k;
			// std::cout << "NEW POS : " << pos << std::endl;
			positions.insert(pos);
		} while (k < K);

		if (S >= positions.size()) {
			for (auto i : positions)
				std::cout << " " << i + 1;
		} else std::cout << " IMPOSSIBLE";
		std::cout << std::endl;
	}
}
