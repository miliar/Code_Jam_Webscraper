#include <iostream>
#include <string>
#include <sstream>
#include <vector>

int iterSearch(long long n) {
	if (n == 0) return -1;
	std::vector<bool> digits(10, false);
	int seen = 0;

	int i = 1;
	while (1) {
		long long x = n * i++;
		std::stringstream ss;
		ss << x;
		std::string text = ss.str();

		for (int j = 0; j < text.size(); ++j) {
			int digit;
			std::stringstream d;
			d << text.substr(j, 1);
			d >> digit;


			if (!digits[digit]) {
				digits[digit] = true;
				++seen;
			}

			if (seen == 10) return x;
		}
	}
}

int main() {
	int t;
	std::cin >> t;

	for (int i = 1; i <= t; ++i) {
		int num;
		std::cin >> num;

		int count = iterSearch(num);

		std::cout << "Case #" << i << ": ";
		if (count == -1)
			std::cout << "INSOMNIA";
		else
			std::cout << count;

		std::cout << std::endl;
	}
}
