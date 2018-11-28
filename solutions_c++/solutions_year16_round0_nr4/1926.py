#include <iostream>

int main() {
	int num_cases;
	std::cin >> num_cases;

	for (int i = 1; i <= num_cases; ++i) {
		int K, C, S;
		std::cin >> K >> C >> S;
		std::cout << "Case #" << i << ": ";

		// It is always sufficient to look at the first K tiles
		for (int j = 1; j <= K; ++j) {
			std::cout << j << ' ';
		}

		std::cout << '\n';
	}

	return 0;
}
