#include <iostream>
#include <string>
#include <vector>

int main() {
	std::string line;
	int c = 0;
	while (std::getline(std::cin, line)) {
		if (c == 0) {
			++c;
			continue;
		}
		int n = std::stoi(line);
		if (n == 0) {
			std::cout << "Case #" << c << ": INSOMNIA" << std::endl;
			++c;
			continue;
		}

		std::vector<int> v(10, 0);

		int sum = 0;

		int original_n = n;
		int count = 2;

		while (sum < 10) {
			sum = 0;
			int temp = n;
			while (n > 0) {
				int digit = n % 10;
				// if never see the digit before
				if (v[digit] < 1 ) {
					++v[digit];
				}
				n = n / 10;
			}
			for (int i = 0; i < v.size(); ++i) {
				sum += v[i];
			}
			if (sum == 10) {
				std::cout << "Case #" << c << ": " << temp << std::endl;
				++c;
				break;
			}
			else {
				n = original_n * count;
				++count;
				continue;
			}
		}
	}
    return 0;
}


