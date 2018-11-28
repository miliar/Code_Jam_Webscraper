#include <iostream>

int main() {
	int N, r, x, c[2][4], result, count;
	std::cin >> N;
	for (int i = 0; i < N; i++) {
		count = 0, result = 0;
		for (int j = 0; j < 2; j++) {
			std::cin >> r;
			for (int k = 1; k < 5; k++) {
				if (k == r)
					std::cin >> c[j][0] >> c[j][1] >> c[j][2] >> c[j][3];
				else
					std::cin >> x >> x >> x >> x;
			}
		}
		for (int j = 0; j < 4; j++) {
			for (int k = 0; k < 4; k++) {
				if (c[0][j] == c[1][k]) {
					result = c[0][j];
					count++;
				}
			}
		}
		switch (count) {
			case 0:
				std::cout << "Case #" << (i + 1) << ": Volunteer cheated!" << std::endl;
				break;
			case 1:
				std::cout << "Case #" << (i + 1) << ": " << result << std::endl;
				break;
			default:
				std::cout << "Case #" << (i + 1) << ": Bad magician!" << std::endl;
		}
	}
}
