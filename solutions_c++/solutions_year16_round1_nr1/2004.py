#include <iostream>
#include <string>
#include <vector>

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		std::string S,Sr;
		std::cin >> S;
		Sr += S[0];
		for (int i = 1; i < S.length(); i++) {
			if (Sr[0] > S[i]) Sr += S[i];
			else Sr = S[i] + Sr;
		}
		std::cout << Sr;
		std::cout << std::endl;
	}
	return 0;
}
