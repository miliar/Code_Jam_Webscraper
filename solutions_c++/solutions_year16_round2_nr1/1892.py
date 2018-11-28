#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main() {
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; t++) {
		std::cout << "Case #" << t << ": ";
		std::string s;
		std::cin >> s;
		int letters[26] = {0};
		for (auto c : s) letters[c-'A']++;
		int numbers[10] = {0};

		numbers[0] = letters['Z'-'A'];
		letters['E'-'A'] -= numbers[0];
		letters['R'-'A'] -= numbers[0];
		letters['O'-'A'] -= numbers[0];
		
		numbers[2] = letters['W'-'A'];
		letters['T'-'A'] -= numbers[2];
		letters['O'-'A'] -= numbers[2];

		numbers[4] = letters['U'-'A'];
		letters['F'-'A'] -= numbers[4];
		letters['O'-'A'] -= numbers[4];
		letters['R'-'A'] -= numbers[4];

		numbers[5] = letters['F'-'A'];
		letters['I'-'A'] -= numbers[5];
		letters['V'-'A'] -= numbers[5];
		letters['E'-'A'] -= numbers[5];

		numbers[6] = letters['X'-'A'];
		letters['S'-'A'] -= numbers[5];
		letters['I'-'A'] -= numbers[5];
		
		numbers[7] = letters['V'-'A'];
		letters['S'-'A'] -= numbers[7];
		letters['E'-'A'] -= numbers[7];
		letters['E'-'A'] -= numbers[7];
		letters['N'-'A'] -= numbers[7];

		numbers[1] = letters['O'-'A'];
		letters['N'-'A'] -= numbers[1];
		letters['E'-'A'] -= numbers[1];

		numbers[3] = letters['R'-'A'];
		numbers[8] = letters['G'-'A'];
		numbers[9] = letters['N'-'A'] / 2;

		for (int i = 0; i < 10; i++)
			while(numbers[i] != 0)
				{std::cout << i; numbers[i]--;}
		std::cout << std::endl;
	}
	return 0;
}
