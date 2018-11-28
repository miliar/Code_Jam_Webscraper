#include <iostream>
#include <vector>
#include <set>

int main(int argc, char **argv) {
	long long num;
	std::vector<long long> numbers;
	std::cin >> num;
	for(long long cnt(num); cnt > 0; --cnt) {
		long long num;
		std::cin >> num;
		numbers.push_back(num);
	}

	size_t caseCounter(1);
	for(const auto& number : numbers) {
		std::set<size_t> digits;
		for(size_t i = 1; i < 100; ++i) {
			long long numToCompare = i * number;
			long long numToCompareCopy = numToCompare;
			while (numToCompare) {
			    unsigned digit = numToCompare % 10;
			    digits.insert(digit);
			    if(digits.size() == 10) {
			    	std::cout << "Case #" << caseCounter << ": " << numToCompareCopy << "\n";
			    	break;
			    }
			    numToCompare /= 10;
			}
			if(digits.size() == 10) { break; }
		}
		if(digits.size() < 10) {
			std::cout << "Case #" << caseCounter << ": " << "INSOMNIA" << "\n";
		}
		digits.clear();
		++caseCounter;
	}

}
