#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main(void) {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		int N;
		std::cin >> N;
		std::vector<int> P(N);
		int s = 0;
		for (int i = 0; i < N; i++) {
			std::cin >> P[i];
			s += P[i];
		}
		for (int i = 0; i < s; i++) {
			int max = 0;
			for (int j = 0; j < N; j++)
				if (P[j] > max) max = P[j];
			int state = 0;
			if (max > 1)
			for (int j = 0; j < N; j++) {
				if (state <= 1 && P[j] == max) {
					P[j]--;
					if (state == 1) i++;
					state++;
					std::cout << char('A' + j);
				}
			}
			else {
				if (s-i == 2) {
					for (int j = 0; j < N; j++)
						if (P[j] == 1) std::cout << char('A' + j);
					i++;
				} else {
					for (int j = 0; j < N; j++) {
						if (P[j] == 1) {
							std::cout << char('A' + j);
							P[j]--;
							break;
						}
					}
				}
			}
			std::cout << " ";
		}
		std::cout << std::endl;
	}
	return 0;
}
