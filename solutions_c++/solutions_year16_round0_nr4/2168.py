#include <iostream>

int main() {
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i ++) {
		int k, c, s;
		std::cin >> k >> c >> s;
		std::cout << "Case #" << i << ":";
		for (int j = 1; j <= s; j ++)
			std::cout << " " << j;
		std::cout << std::endl;
	}
	return 0;
}

