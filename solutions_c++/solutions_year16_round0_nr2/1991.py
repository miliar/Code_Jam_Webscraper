#include <iostream>
#include <string>
#include <vector>

int num_flips(std::vector<bool> &pancake_stack) {
	while (!pancake_stack.empty() && pancake_stack.back()) {
		pancake_stack.pop_back();
	}

	if (pancake_stack.empty()) {
		return 0;
	} else {
		pancake_stack.pop_back();
		for (int i = 0; i < pancake_stack.size(); ++i) {
			pancake_stack[i] = !pancake_stack[i];
		}
		return 1 + num_flips(pancake_stack);
	}
}

int main() {
	int num_cases;
	std::cin >> num_cases;

	for (int i = 1; i <= num_cases; ++i) {
		std::string stack_str;
		std::cin >> stack_str;
		std::vector<bool> pancake_stack;

		for (char c : stack_str) {
			pancake_stack.push_back(c == '+');
		}

		std::cout << "Case #" << i << ": " << num_flips(pancake_stack) << '\n';
	}

	return 0;
}
