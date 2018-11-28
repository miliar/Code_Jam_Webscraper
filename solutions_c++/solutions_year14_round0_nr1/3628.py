#include<iostream>
#include<vector>
#include<algorithm>

int main(void) {
	int cases;

	std::cin >> cases;
	int current = 1;
	while (cases--) {
		std::vector<int> row_1;

		std::vector<int> row_2;

		int ans1, ans2;

		std::cin >> ans1;
		int inp;
		for (int waste = 0; waste < (ans1 - 1) * 4; ++waste)
			std::cin >> inp;
		for (int i = 0; i < 4; ++i) {
			std::cin >> inp;
			row_1.push_back(inp);
		}

		int left = 16 - ans1 * 4;
		
		while (left--)
			std::cin >> inp;

		std::cin >> ans2;
		for (int waste = 0; waste < (ans2 - 1) * 4; ++waste)
			std::cin >> inp;
		for (int i = 0; i < 4; ++i) {
			std::cin >> inp;
			row_2.push_back(inp);
		}

		left = 16 - ans2 * 4;

		while (left--)
			std::cin >> inp;

		std::sort(row_1.begin(), row_1.end());
		std::sort(row_2.begin(), row_2.end());

		int matches = 0, value;
		for (auto it1 = row_1.begin(), it2 = row_2.begin(); it1 != row_1.end() && it2 != row_2.end();) {
			if (*it1 == *it2) {
				matches++;
				value = *it1;
				++it1;
				++it2;
			}
			else if (*it1 < *it2)
				it1++;
			else
				it2++;
		}
		std::cout << "Case #" << current << ": ";
		current++;
		if (matches == 0)
			std::cout << "Volunteer cheated!" << std::endl;
		else if (matches == 1)
			std::cout << value << std::endl;
		else
			std::cout << "Bad magician!" << std::endl;
	}
}