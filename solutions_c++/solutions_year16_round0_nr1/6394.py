#include <iostream>
#include <algorithm>

int main(void)
{
	int T;
	uint64_t N;

	std::cin >> T;

	for (int i = 0; i < T; i++) {
		std::cin >> N;

		if (N != 0) {
			bool check[10];
			for (int j = 0; j < 10; j++) {
				check[j] = false;
			}

			bool loop = true;
			uint64_t x = 0;
			do {
				x++;
				uint64_t t = N * x;
				while (t > 0) {
					check[t % 10] = true;
					t /= 10;
				}

				loop = false;
				for (int j = 0; j < 10; j++) {
					if (check[j] == false) {
						loop = true;
					}
				}
			}while(loop);

			std::cout << "Case #" << i + 1 << ": " << N * x << std::endl;
		}
		else {
			std::cout << "Case #" << i + 1 << ": INSOMNIA" << std::endl;
		}

	}

	return 0;
}

