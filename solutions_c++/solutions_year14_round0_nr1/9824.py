#include <iostream>

int main() {
	int c = 0;
	int total_cases = 0;

	std::cin >> total_cases;

	std::cout << "Total Cases: " << total_cases << std::endl;

	int possibles [4] = {0, 0, 0, 0};
	
	for(c = 0; c < total_cases; c++) {
		int first_row = 0;
		std::cin >> first_row;
		int number = 0;
		int total_match = 0;
		
		for(int row = 1; row <= 4; row++) {
			for(int col = 0; col < 4; col++) {
				int input_digit = 0;
				std::cin >> input_digit;
				
				if(first_row == row) {
					possibles[col] = input_digit;
				}				
			}
		}
		
		int second_row = 0;
		std::cin >> second_row;
		
		for(int row = 1; row <= 4; row++) {
			for(int col = 0; col < 4; col++) {
				int input_digit = 0;
				std::cin >> input_digit;
				
				if(second_row == row) {
					for(int pos = 0; pos < 4; pos++) {
						if(possibles[pos] == input_digit) {
							number = input_digit;
							total_match++;
						}
					}
				}
			}
		}
		
		std::cout << "Case #" << (c + 1) << ": ";
		if(total_match == 0) {
			std::cout << "Volunteer cheated!";
		}
		else if(total_match > 1) {
			std::cout << "Bad magician!";
		}
		else {
			std::cout << number;
		}
		std::cout << std::endl;
	}
}