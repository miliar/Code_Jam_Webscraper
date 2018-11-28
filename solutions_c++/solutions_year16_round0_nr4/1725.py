#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		int K,C,S;
		std::cin >> K >> C >> S;
		if (K == S) {
			for (int i = 1; i <= K; i++)
				std::cout << i << " ";
		}

		std::cout << std::endl;
	}
	return 0;
}
