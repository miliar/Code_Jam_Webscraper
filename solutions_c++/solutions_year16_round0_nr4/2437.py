#include <iostream>



int main () {
	uint32_t T;
	std::cin >> T;
	for (uint32_t i = 0; i < T; ++i) {
		uint32_t K,C,S;
		std::cin >> K >> C >> S;


		std::cout << "Case #" << i+1 << ":";
		for (int j = 1; j <= K; ++j) {
			std::cout << " " << j;
		}
		std::cout << std::endl;
	}
	return 0;
}