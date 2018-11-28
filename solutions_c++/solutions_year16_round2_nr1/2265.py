#include <iostream>
#include <string>

int main() {
	int t;
	std::cin >> t;
	
	std::string s;
	const int NO_LETTERS = 'Z'-'A' + 1;
	int letters[NO_LETTERS];

	const int NO_DIGITS = 10;
	int digits[NO_DIGITS];
	
	for (int i = 0; i < t; ++i) {
		
		// init:
		for (int i = 0; i < NO_LETTERS; ++i) {
			letters[i] = 0;
		}
		
		std::cin >> s;
		for (char c : s) {
			letters[c - 'A']++;
		}
		
		digits[6] = letters['X' - 'A'];
		letters['S' - 'A'] -= digits[6];
		letters['I' - 'A'] -= digits[6];
		letters['X' - 'A'] -= digits[6];
		
		digits[8] = letters['G' - 'A'];
		letters['E' - 'A'] -= digits[8];
		letters['I' - 'A'] -= digits[8];
		letters['G' - 'A'] -= digits[8];
		letters['H' - 'A'] -= digits[8];
		letters['T' - 'A'] -= digits[8];
		
		digits[0] = letters['Z' - 'A'];
		letters['Z' - 'A'] -= digits[0];
		letters['E' - 'A'] -= digits[0];
		letters['R' - 'A'] -= digits[0];
		letters['O' - 'A'] -= digits[0];
		
		digits[2] = letters['W' - 'A'];
		letters['T' - 'A'] -= digits[2];
		letters['W' - 'A'] -= digits[2];
		letters['O' - 'A'] -= digits[2];
		
		digits[3] = letters['H' - 'A'];
		letters['T' - 'A'] -= digits[3];
		letters['H' - 'A'] -= digits[3];
		letters['R' - 'A'] -= digits[3];
		letters['E' - 'A'] -= 2*digits[3];
		
		digits[7] = letters['S' - 'A'];
		letters['S' - 'A'] -= digits[7];
		letters['E' - 'A'] -= 2*digits[7];
		letters['V' - 'A'] -= digits[7];
		letters['N' - 'A'] -= digits[7];
		
		digits[5] = letters['V' - 'A'];
		letters['F' - 'A'] -= digits[5];
		letters['I' - 'A'] -= digits[5];
		letters['V' - 'A'] -= digits[5];
		letters['E' - 'A'] -= digits[5];
		
		digits[9] = letters['I' - 'A'];
		letters['N' - 'A'] -= 2*digits[9];
		letters['I' - 'A'] -= digits[9];
		letters['E' - 'A'] -= digits[9];
		
		digits[4] = letters['F' - 'A'];
		letters['F' - 'A'] -= digits[4];
		letters['O' - 'A'] -= digits[4];
		letters['U' - 'A'] -= digits[4];
		letters['R' - 'A'] -= digits[4];
		
		digits[1] = letters['O' - 'A'];
		// checkup, unneceserry:
		letters['O' - 'A'] -= digits[1];
		letters['N' - 'A'] -= digits[1];
		letters['E' - 'A'] -= digits[1];
		
		std::cout << "Case #" << i + 1 << ": ";
		for (int digit = 0; digit < NO_DIGITS; ++digit) {
			while(digits[digit]) {
				std::cout << digit;
				--digits[digit];
			}
		}
		
		std::cout << std::endl;
	}

	return 0;
}
