#include <cstdio>
#include <iostream>
#include <string>

std::string input;

void solve(void) {
	std::cin >> input;

	std::string output;
	for (int i = 0, j; i < (int)input.length(); i = j) {
		for (j = i; j < (int)input.length() && input[j] == input[i]; ++j);
		output += input[i];
	}

	std::cout << (int)output.length() - (output.back() == '+') << std::endl;
}

int main(void) {
	int tests;
	std::cin >> tests;
	for (int i = 1; i <= tests; ++i) {
		std::cout << "Case #" << i << ": ";
		solve();
	}
}