#include <iostream>
#include <string>

int T;

int main() {
	std::cin >> T;
	for (int t = 0; t < T; ++t) {
		int e = 0;
		int s = 0;
		int S = 0;
		std::string x;
		std::cin >> S >> x;
		for (int i = 0; i <= S; ++i) {
			e += std::max(0, i - s);
			s += std::max(0, i - s);
			s += x[i] - '0';
		}
		std::cout << "Case #" << t + 1 << ": " << e << '\n';
	}
}