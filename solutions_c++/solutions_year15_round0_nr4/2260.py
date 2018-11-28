#include <iostream>

bool g_win(int x, int r, int c) {
	switch (x) {
		case 1:
			return true;
		case 2:
			return r % 2 == 0 || c % 2 == 0;
		case 3:
			return (r % 3 == 0 || c % 3 == 0)
					&& r >= 2 && c >= 2;
		default:
			return (r == 4 || c == 4)
					&& r >= 3 && c >= 3;
	}
}

int main() {
	int cases, n = 1;
	std::cin >> cases;
	while (n <= cases) {
		int x, r, c;
		std::cin >> x >> r >> c;
		if (g_win(x, r, c)) {
			std::cout << "Case #" << n << ": GABRIEL" << std::endl;
		} else {
			std::cout << "Case #" << n << ": RICHARD" << std::endl;
		}
		++n;
	}
	return 0;
}