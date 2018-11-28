#include <iostream>

void solve(int test) {
	int i, j, a;
	int counts[17] = {0};
	std::cin >> i;
	for(int y = 0; y < 4; ++y) {
		for(int x = 0; x < 4; ++x) {
			std::cin >> a;
			if(i-1 == y)
				counts[a]++;
		}
	}
	std::cin >> j;
	for(int y = 0; y < 4; ++y) {
		for(int x = 0; x < 4; ++x) {
			std::cin >> a;
			if(j-1 == y)
				counts[a]++;
		}
	}
	
	int n_answers = 0;
	int answer;
	for(int n = 1; n <= 16; ++n) {
		if(counts[n] == 2) {
			n_answers++;
			answer = n;
		}
	}

	if(n_answers == 1)
		std::cout << "Case #" << test << ": " << answer << std::endl;
	else if(n_answers > 1)
		std::cout << "Case #" << test << ": Bad magician!" << std::endl;
	else
		std::cout << "Case #" << test << ": Volunteer cheated!" << std::endl;
}

int main() {
	int t;
	std::cin >> t;
	for(int i = 1; i <= t; ++i) {
		solve(i);
	}
	return 0;
}
