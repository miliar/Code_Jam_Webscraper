
#include <iostream>
#include <vector>

#define TIMEOUT 10000

bool allNums(std::vector<int> digs) {
	for (int i = 0; i < (int)digs.size(); i++) {
		if (digs[i] == 0) {
			return false;
		}
	}

	return true;
}

int main() {

	int T;
	std::cin >> T;

	for (int t = 0; t < T; t++) {
		int N;
		std::cin >> N;

		std::vector<int> digs;
		digs.resize(10,0);

		int i = 0;

		while (!allNums(digs)) {
			if (i == TIMEOUT) {
				std::cout << "Case #" << t+1 << ": INSOMNIA" << std::endl;
				break;
			}

			long unsigned n = N*++i;

			do {
			    long unsigned digit = n % 10;
			    digs[digit]++;
			    n /= 10;
			} while (n > 0);
		}

		if (allNums(digs)) {
			std::cout << "Case #" << t+1 << ": " << N*i << std::endl;
		}

	}


	return 0;
}
