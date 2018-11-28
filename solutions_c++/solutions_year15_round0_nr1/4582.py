#include <iostream>

int main() {
	int cases, i = 1;
	std::cin >> cases;
	while (i <= cases) {
		int sz;
		std::cin >> sz;
		int j = 0, total = 0, res = 0;
		while (j <= sz) {
			char c;
			std::cin >> c;
			int guest_num = c-'0';
			if (guest_num > 0 && j > total) {
				res += (j-total);
				total = j + guest_num;
			} else {
				total += guest_num;
			}
			++j;
		}
		std::cout << "Case #" << i << ": " << res << std::endl;
		++i;
	}
	return 0;
}