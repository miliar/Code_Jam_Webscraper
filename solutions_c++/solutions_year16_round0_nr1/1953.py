#include <iostream>
#include <vector>

bool all_true(std::vector<bool> &v) {
	for (bool b : v) {
		if (!b) return false;
	}
	return true;
}

unsigned long long last_number(int num) {
	unsigned long long result = num;
	std::vector<bool> found_digits(10, false);

	do {
		unsigned long long temp = result;
		while (temp) {
			int digit = temp % 10;
			found_digits[digit] = true;
			temp /= 10;
		}
		result += num;
	} while (!all_true(found_digits));

	return result - num;
}

int main() {
	int num_cases;
	std::cin >> num_cases;

	for (int i = 1; i <= num_cases; ++i) {
		std::cout << "Case #" << i << ": ";

		int num;
		std::cin >> num;
		if (num == 0) {
			std::cout << "INSOMNIA";
		} else {
			std::cout << last_number(num);
		}

		std::cout << '\n';
	}

	return 0;
}
