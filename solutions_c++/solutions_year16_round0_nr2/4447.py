// pancakes.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <string>
#include <stdexcept>

//! Checks if all pancakes are happy side up
bool isStackHappy(const std::vector<bool>& stack)
{
	return (std::find(stack.begin(), stack.end(), false) == stack.end());
}

//! Converts + or - to true or false respectively
bool signToBool(const char& sign) {
	switch (sign) {
		case '+': return true;
		case '-': return false;
	}
	throw std::invalid_argument("Only supports + and - as input.");
}

//! Converts a string of +/- to a vec<bool> pancake stack
std::vector<bool> stringToStack(const std::string& string)
{
	std::vector<bool> stack;
	std::transform(string.begin(), string.end(), std::back_inserter(stack), &signToBool);

	return stack;
}

// Caluclates the minimum number of required flips to get a happy stack
int minimalFlipsForHappyStack(const std::vector<bool>& stack)
{
	if (isStackHappy(stack)) {
		return 0;
	} else {
		int flipCounter = 0;
		// Count the times of side changes (changes between true/false or happy/other side)
		for (int i = 0; i < stack.size()-1; i++) {
			if (stack.at(i) != stack.at(i+1)) flipCounter++;
		}

		// Increase count if last pancake is other side up
		if (stack.back() == false) flipCounter++;

		return flipCounter;
	}
}

int main()
{
	// std::cout << "Happy Pancakes" << "\n";
	// std::cout << "--------------" << "\n";

	// Get number of test cases
	int caseCount;
	std::cin >> caseCount;

	// std::cout << "Received " << caseCount << " test cases." << "\n";

	// Read stack input strings from std in
	std::vector<std::string> stackStrings;
	stackStrings.reserve(caseCount);
	std::copy_n(std::istream_iterator<std::string>(std::cin), caseCount, std::back_inserter(stackStrings));

	// std::cout << "Read " << stackStrings.size() << " values into vector." << "\n";

	// Convert input strings to bool vectors
	std::vector<std::vector<bool>> stacks;
	stacks.reserve(caseCount);
	std::transform(stackStrings.begin(), stackStrings.end(), std::back_inserter(stacks), &stringToStack);

	// Calculate number of minimal flips per stack
	std::vector<int> output;
	output.reserve(caseCount);
	std::transform(stacks.begin(), stacks.end(), std::back_inserter(output), &minimalFlipsForHappyStack);

	// Print results
	for (int i = 0; i < caseCount; i++) {
		std::cout << "Case #" << i+1 << ": " << output.at(i) << "\n";
	}

    return 0;
}

