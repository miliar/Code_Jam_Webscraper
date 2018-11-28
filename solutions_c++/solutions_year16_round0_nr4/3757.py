#include <iostream>

int main() {
	int T;
	std::cin >> T;
	
	for (int i=1; i<=T; i++) {
		int K, C, S;
		std::cin >> K >> C >> S;

		std::cout << "Case #" << i << ":";
		for (int i=1; i<=K; i++)
			std::cout << " " << i;
		std::cout << std::endl;
	}
}
