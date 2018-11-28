#include <iostream>
#include <string>

int cnt(std::string s) {
	char c = 0;
	int count = 0;
	for (int i = 0; i < s.length(); i ++) 
		if (s[i] != c) c = s[i], count ++;
	if (*s.rbegin() == '+') count --;
	return count;
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 1; i <= T; i ++) {
		std::string input;
		std::cin >> input;
		std::cout << "Case #" << i << ": " << cnt(input) << std::endl;
	}
	return 0;
}
