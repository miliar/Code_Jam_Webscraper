#include <iostream>
#include <algorithm>
#include <vector>

int signs_to_ints(const char& sign) {
	if (sign == '+') {
		return 1;
	}
	return 0;
}

void solve() {
	std::string s;
	while (s.empty()) {
		std::getline(std::cin, s);		
	}
	std::vector<int> pancakes;
	std::transform(s.begin(), s.end(), std::back_inserter(pancakes), signs_to_ints);
	int flip_count = 0;
	for (;;) {
		unsigned int score = std::accumulate(pancakes.begin(), pancakes.end(), 0U);
		if (score == pancakes.size()) {
			break;
		}
		unsigned int i;
		for (i = 1; i < pancakes.size(); ++i) {
			if (pancakes[i] != pancakes[i - 1]) {
				break;
			}
		}
		for (unsigned int i2 = 0; i2 < i; ++i2) {
			switch (pancakes[i2]) {
				case 0:
					pancakes[i2] = 1;
					break;
				case 1:
					pancakes[i2] = 0;
					break;
			}
		}
		++flip_count;
	}
	std::cout << flip_count << std::endl;
}

int main(int argc, char ** argv) {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cout << "Case #" << i << ": " ;
		solve();
	}
}