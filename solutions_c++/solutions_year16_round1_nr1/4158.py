// TheLastWord.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>

std::string getLastWord(const std::string& input)
{
	std::string lastWord = std::string(1, input.front());

	if(input.length() > 1) {	
		for (size_t i = 1; i < input.length(); i++) {
			auto c = std::string(1, input[i]);

			auto s1 = lastWord + c;
			auto s2 = c + lastWord;
			lastWord = std::max(s1, s2);
		}
	}

	return lastWord;
}

int main()
{
	int caseCount;
	std::cin >> caseCount;

	std::vector<std::string> startingStrings;
	std::copy_n(std::istream_iterator<std::string>(std::cin), caseCount, std::back_inserter(startingStrings));

	std::vector<std::string> lastWords;
	lastWords.reserve(caseCount);

	std::transform(startingStrings.begin(), startingStrings.end(), std::back_inserter(lastWords), &getLastWord);

	for (int i = 0; i < caseCount; i++) {
		std::cout << "Case #" << i+1 << ": " << lastWords[i] << "\n";
	}

    return 0;
}

