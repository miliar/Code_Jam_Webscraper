#include <iostream>
#include <set>

int main() {
	size_t nCases;
	std::cin >> nCases;
	for (size_t i = 0; i < nCases; ++i) {
		std::cout << "Case #" << i + 1 << ": ";
		long long baseNumber;
		std::cin >> baseNumber;
		if (baseNumber != 0) {
			std::set<int> digitsSeen;
			long long currentNumber = baseNumber;
			while(1) {
				for (auto x = currentNumber; x > 0; x = x / 10)
					digitsSeen.insert(x % 10);
				if (digitsSeen.size() == 10)
					break;
				currentNumber += baseNumber;
			}
			std::cout << currentNumber << std::endl;
		} else std::cout << "INSOMNIA" << std::endl;
	}
}
