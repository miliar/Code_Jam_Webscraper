#include <iostream>
#include <string>

int solve(int maxshyness, std::string str) {
	int additional = 0;
	int up = 0;
	for (int i = 0; i <= maxshyness; ++i) {
		int num = str[i] - '0';
		if (i > up) {
			additional += i - up;
			up = i;
		}
		up += num;
	}
	return additional;
}

int main() {
	int cases;
	std::cin >> cases;
	for (int i = 0; i < cases; i++) {
		int maxshyness;
		std::string str;
		std::cin >> maxshyness >> str;
		std::cout << "Case #" << i+1 << ": " << solve(maxshyness, str) << std::endl;
	}
	return 0;
}
