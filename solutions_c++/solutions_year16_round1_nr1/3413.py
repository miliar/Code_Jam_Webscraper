#include <iostream>
#include <string>

std::string lastWord(const std::string &word) 
{
	std::string result; result.push_back(word[0]);
	for (int i = 1; i < word.length(); i++) {
		if (word[i] >= result[0]) {
			result.insert(0, 1, word[i]);
		} else {
			result.push_back(word[i]);
		}
	}
	return result;
}

int main()
{
	int NumTests = 0;
	std::cin >> NumTests;
	for (int i = 1; i <= NumTests; i++) {
		std::string word; std::cin >> word;
		std::cout << "Case #" << i << ": " << lastWord(word) << std::endl;
	}
	return 0;
}