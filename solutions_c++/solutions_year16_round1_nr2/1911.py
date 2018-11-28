#include <iostream>

int main(void) {
	int T;
	std::cin >> T;

	int N;
	for (int i = 0; i < T; i++) {
		std::cin >> N;

		int height[2500] = { 0 };
		int num;
		for (int j = 0; j < N*(2*N-1); j++) {
			std::cin >> num;
			height[num - 1]++;
		}
		int count = 0;
		int result[50];
		for (int j = 0; j < 2500; j++) {
			if (height[j] % 2 == 1) {
				result[count] = j + 1;
				count++;
			}
			if (count >= N)break;
		}

		std::cout << "Case #" << i + 1 << ":";
		for (int j = 0; j < N; j++) {
			std::cout << ' ' << result[j];
		}
		std::cout << std::endl;
	}

	return 0;
}