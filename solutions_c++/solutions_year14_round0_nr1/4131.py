#include <iostream>

#define CARDS 16
#define SIDE 4

#define BAD_MAGIC 0
#define FOUND 1
#define CHEAT 2

int main()
{
	int cases;
	int row1, row2;
	int arrange1[SIDE][SIDE], arrange2[SIDE][SIDE];

	std::cin >> cases;

	for (int i = 1; i <= cases; i++) {
		std::cin >> row1;

		for (int j = 0; j < SIDE; j++) {
			for (int k = 0; k < SIDE; k++) {
				std::cin >> arrange1[j][k];
			}
		}

		std::cin >> row2;

		for (int j = 0; j < SIDE; j++) {
			for (int k = 0; k < SIDE; k++) {
				std::cin >> arrange2[j][k];
			}
		}

		int count[CARDS] = {0};

		for (int j = 0; j < SIDE; j++) {
			int num1 = arrange1[row1 - 1][j];
			int num2 = arrange2[row2 - 1][j];

			count[num1 - 1]++;
			count[num2 - 1]++;
		}

		int state = CHEAT;
		int num;

		for (int j = 0; j < CARDS; j++) {
			if (count[j] > 1) {
				if (state == CHEAT) {
					state = FOUND;
					num = j + 1;
				} else if (state == FOUND) {
					state = BAD_MAGIC;
					break;
				}
			}
		}

		if (state == BAD_MAGIC) {
			std::cout << "Case #" << i << ": Bad magician!" << std::endl;
		} else if (state == FOUND) {
			std::cout << "Case #" << i << ": " << num << std::endl;
		} else {
			std::cout << "Case #" << i << ": Volunteer cheated!" << std::endl;
		}
	}

	return 0;
}
