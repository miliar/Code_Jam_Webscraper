#include <iostream>

void input_answer(int *answer, int table[][4]) {
	std::cin >> *answer;
	*answer = *answer - 1;
	for (int row = 0; row < 4; ++row) {
		for (int column = 0; column < 4; ++column) {
			std::cin >> table[row][column];
		}
	}
}

int main() {
	int case_count;
	int first_answer;
	int second_answer;
	int first_table[4][4];
	int second_table[4][4];
	
	std::cin >> case_count;
	for (int case_num = 1; case_num <= case_count; ++case_num) {
		input_answer(&first_answer, first_table);
		input_answer(&second_answer, second_table);

		int equal_count = 0;
		int equal_value = -1;
		for (int col1 = 0; col1 < 4; ++col1) {
			for (int col2 = 0; col2 < 4; ++col2) {
				if (first_table[first_answer][col1] == second_table[second_answer][col2]) {
					equal_count++;
					equal_value = first_table[first_answer][col1];
				}
			}
		}
		std::cout << "Case #" << case_num << ": ";
		if (equal_count == 1) {
			std::cout << equal_value << std::endl;
		} else if (equal_count == 0) {
			std::cout << "Volunteer cheated!" << std::endl;
		} else {
			std::cout << "Bad magician!" << std::endl;
		}
	}
	return 0;
}
