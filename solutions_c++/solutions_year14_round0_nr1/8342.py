#include <iostream>
#include <vector>
#include <set>
#include <iterator>
#include <algorithm>

int main() {

	int T, t;
	std::cin >> T;
	
	for (t = 1; t <= T; t++) {
		std::vector<int> a, b;
		int i, j;
		std::set<int> f, g;

		std::cin >> i;
		std::copy_n(std::istream_iterator<int>(std::cin), 16, std::back_inserter(a));
		std::copy_n(std::begin(a) + 4 * (i - 1), 4, std::inserter(f, std::begin(f)));

		std::cin >> j;
		std::copy_n(std::istream_iterator<int>(std::cin), 16, std::back_inserter(b));
		std::copy_n(std::begin(b) + 4 * (j - 1), 4, std::inserter(g, std::begin(g)));

		std::vector<int> common;
		std::set_intersection(std::begin(f), std::end(f), std::begin(g), std::end(g), std::back_inserter(common));
		
		std::cout << "Case #" << t << ": ";
		switch (common.size()) {
			case 0:
				std::cout << "Volunteer cheated!";
				break;
			case 1:
				std::cout << common.front();
				break;
			default:
				std::cout << "Bad magician!";
		}
		std::cout << std::endl;
	}

	return 0;
}