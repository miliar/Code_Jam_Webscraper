#include <iostream>

int main() {
	int TC;
	std::cin >> TC;
	for (int i = 0; i < TC; i++) {
		int smax;
		std::cin >> smax;
		int mincount = 0;
		int scur = 0;
		for (int j = 0; j <= smax; j++) {
			char c;
			std::cin >> c;
			int cv = c - 48;
			if (cv == 0) continue;
			if (scur < j) {
				mincount += j - scur;
				scur = j;
			}
			scur += cv;
		}
		std::cout << "Case #" << (i+1) << ": " << mincount << std::endl;
	}
}