#include <iostream>
#include <vector>
#include <string>

void flip(std::string stack, int n) {
	int flipCount = 0;
	// Reverse iterate string
	for (int i = stack.size() - 1; i >= 0; i--) {
		if (stack[i] == '+') {
			// If there is a +, we don't want to flip it
			continue;
		} else {
			if (stack[0] == '+') {
				// Special case, flipping first two will not go anywhere
				flipCount++;
				int l = 0;
				while (stack[l] == '+') l++;

				for (int k = 0; k < l / 2; k++) {
					char temp = stack[k];
					stack[k] = stack[l - k - 1];
					stack[l - k - 1] = temp;
				}

				for (int k = 0; k < l; k++) {
					stack[k] = stack[k] == '+' ? '-' : '+';
				}
			}
			
			flipCount++;

			int l = i + 1;

			for (int k = 0; k < l / 2; k++) {
				char temp = stack[k];
				stack[k] = stack[l - k - 1];
				stack[l - k - 1] = temp;
			}

			for (int k = 0; k <= i; k++) {
				stack[k] = stack[k] == '+' ? '-' : '+';
			}
		}
	}

	std::cout << "Case #" << n << ": " << flipCount << std::endl;
}

int main() {
	std::size_t T;
	std::cin >> T;
	std::vector<std::string> cases;
	std::string input;
	for (std::size_t i = 0; i < T; i++) {
		std::cin >> input;
		cases.push_back(input);
	}

	for (std::size_t i = 0; i < cases.size(); i++) {
		flip(cases[i], i + 1);
	}
	return 0;
}
