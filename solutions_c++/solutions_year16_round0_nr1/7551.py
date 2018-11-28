#include <iostream>
#include <vector>
#include <string>

void count(unsigned long long input, int n) {
	// Trivial case
	if (input == 0) {
		std::cout << "Case #" << n << ": INSOMNIA" << std::endl;
		return;
	}

	std::vector<char> digits_left = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
	unsigned long long count = 0;
	while (digits_left.size() > 0) {
		// Increment the string
		count++;
		std::string input_string = std::to_string(input * count);
		for (std::size_t j = 0; j < digits_left.size(); j++) {
			std::size_t pos = input_string.find(digits_left[j]);
			if (pos != std::string::npos) {
				digits_left.erase(digits_left.begin() + j--);
			}
		}
	}
	std::cout << "Case #" << n << ": " << input * count << std::endl;
}

int main() {
	std::size_t T;
	std::cin >> T;
	std::vector<unsigned long long> cases;
	unsigned long long num;
	for (std::size_t i = 0; i < T; i++) {
		std::cin >> num;
		cases.push_back(num);
	}

	for (std::size_t i = 0; i < cases.size(); i++) {
		count(cases[i], i + 1);
	}
	return 0;
}
