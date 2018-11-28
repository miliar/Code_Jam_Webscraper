#include <iostream>
#include <numeric>
#include <vector>

void solve() {
	int n;
	std::vector<int> digits {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	std::cin >> n;
	if ( n == 0) {
		std::cout << "INSOMNIA" << std::endl;
		return;
	}
	int j = 0;
	do {
		j += n;
		// std::cerr << "j = " << j << std::endl;
		int np = j;
		do {
			digits[np % 10] = 1;
			np /= 10;
		} while (np > 0);
	} while (std::accumulate(digits.begin(), digits.end(), 0) < 10);
	std::cout << j << std::endl;
}

int main(int argc, char ** argv) {
	int t;
	std::cin >> t;
	for (int i = 1; i <= t; ++i) {
		std::cout << "Case #" << i << ": " ;
		solve();
	}
}