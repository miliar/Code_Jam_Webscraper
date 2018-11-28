#include <iostream>
#include <set>
#include <algorithm>
#include <vector>

int solve() {
	int n, X;
	std::cin >> n >> X;
	std::vector<int> file_sizes;
	for (int i = 0; i < n; ++i) {
		int s;
		std::cin >> s;
		file_sizes.push_back(s);
	}

	std::sort(file_sizes.begin(), file_sizes.end(), std::greater<int>());

	int ret = 0;
/*
	std::multiset<int> remaining_spaces;
	for (int i = 0; i < n; ++i) {
		int s = file_sizes[i];
		auto just_fit_it = remaining_spaces.lower_bound(s);
		if (just_fit_it == remaining_spaces.end()) {
			++ret;
			remaining_spaces.insert(X - s);
		}
		else
			remaining_spaces.erase(just_fit_it);
	}
*/
	for (int i = 0; i < n; ++i) {
		int s_i = file_sizes[i];
		if (s_i == 0)
			continue;
		++ret;
		file_sizes[i] = 0;
		for (int j = 0; j < n; ++j) {
			int s_j = file_sizes[j];
			if (s_j == 0)
				continue;
			if (s_i + s_j <= X) {
				file_sizes[j] = 0;
				break;
			}
		}
	}

	return ret;
}

int main() {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cout << "Case #" << i << ": "
			  << solve() << "\n";
	}
	return 0;
}
