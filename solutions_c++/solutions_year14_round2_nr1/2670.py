#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

std::vector<int> checkWord(const std::string& input, const std::vector<char>& letters) {
	auto iter = letters.begin();
	std::vector<int> counts;
	counts.push_back(0);
	for (char letter : input) {
		if (letter != *iter) {
			if (counts.back() == 0 || letter != *(++iter)){
				throw 1;
			} else
				counts.push_back(0);
		}
		++(counts.back());
	}
	if (++iter != letters.end())
		throw 1;
	return counts;
}

int main() {
	int tests;
	std::cin >> tests;

	for (int i = 1; i <= tests; ++i) {
		int words;
		std::cin >> words;
		std::vector<char> letters;
		std::vector<std::vector<int>> vCounts;

		std::string input;
		std::cin >> input;
		char currentLetter = 0;
		for (char letter : input) {
			if (letter != currentLetter) {
				currentLetter = letter;
				letters.push_back(letter);
			}
		}
		vCounts.push_back(checkWord(input, letters));
		try {
			for (int j = 0; j < (words-1); ++j) {
				std::cin >> input;
				vCounts.push_back(checkWord(input, letters));
			}

			int actions = 0;
			for (int j = 0; j < letters.size(); ++j) {
				std::vector<int> letterCounts;
				for (const auto& arr : vCounts) {
					letterCounts.push_back(arr[j]);
				}
				std::sort(letterCounts.begin(), letterCounts.end());
				int median = letterCounts[letterCounts.size()/2];
				for (const auto& arr : vCounts) {
					actions += std::abs(arr[j] - median);
				}
			}
			std::cout << "Case #" << i << ": " << actions << std::endl;
		} catch (int ex) {
			std::cout << "Case #" << i << ": Fegla Won" << std::endl;
		}
	}
}
