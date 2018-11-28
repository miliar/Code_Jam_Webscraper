#include <iostream>
#include <vector>
#include <list>
#include <numeric>

int main () {

	std::vector<uint64_t> numbers;
	uint64_t n;
	uint16_t T;
	std::cin >> T;
	for (int i = 0; i < T; ++i) {
		std::cin >> n;
		numbers.push_back(n);
	}

	for (int i = 0; i < numbers.size(); ++i) {
		std::list<uint16_t> digits(10);
		std::iota(digits.begin(), digits.end(), 0);

		if (numbers[i] == 0) {
			std::cout << "Case #" << i+1 << ": " << "INSOMNIA" << std::endl;
			continue;
		}

		uint64_t factor = 0;
		while (digits.size() > 0) {
			++factor;
			n = factor * numbers[i];
			while (n != 0) {
				uint16_t tmp = n % 10;
				digits.remove_if([&tmp] (uint16_t a) {return a == tmp;});
				n /= 10;
			}
		}


		


		uint64_t result = factor * numbers[i];
		std::cout << "Case #" << i+1 << ": " << result << std::endl;
	}
	return 0;
}