#include <iostream>
#include <climits>

int main() {
	int t;
	std::cin >> t;
	unsigned long k, c, s, needed, tile;
	int counter;
	for (int i = 0; i < t; ++i) {
		std::cin >> k >> c >> s;
		
		std::cout << "Case #" << i + 1 << ":";
		
		needed = k/c;
		if (c*needed < k) {
			needed++;
		}
		if (needed > s) {
			std::cout << " IMPOSSIBLE";
		} else {
			tile = 0;
			counter = 0;
			for (unsigned long i = 0; i < k; ++i) {
				++counter;
				tile = tile*k + i;
				if (counter == c) {
					counter = 0;
					std::cout << " " << tile + 1;
					tile = 0;
				}
			}
			if (counter != 0) {
				std::cout << " " << tile + 1;
			}
		}
		std::cout << std::endl;
	}

	return 0;
}
