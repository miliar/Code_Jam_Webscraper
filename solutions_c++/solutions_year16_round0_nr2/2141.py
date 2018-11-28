#include <iostream>
#include <string>

int main() {
	int t;
	std::cin >> t;
	
	std::string s;
	
	char last;
	int y;
	for (int i = 0; i < t; ++i) {
		std::cin >> s;
		char last = '+';
		y = 0;
		for (int index = s.length() - 1; index >= 0; --index) {
			if (last != s[index]) {
				last = s[index];
				++y;
			}
		}
		std::cout << "Case #" << i + 1 << ": " << y << std::endl;
	}

	return 0;
}
