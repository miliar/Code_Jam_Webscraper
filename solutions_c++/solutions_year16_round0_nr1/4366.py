// counting_sheep.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>
#include <tuple>
#include <utility>
#include <set>

#include <math.h>

std::vector<int> getDigits(int in)
{
	int n = in;
	std::vector<int> digits;
	n = std::abs(n);
	do {
		digits.push_back(n % 10);
		n /= 10;
	} while (n > 0);

	return digits;
}

std::tuple<int,bool> countSheep(int startingNumber) 
{
	const auto insomnia = std::make_tuple(0,false);
	if (startingNumber == 0) return insomnia;

	std::set<int> usedDigits;
	int currentFactor = 0;
	int currentNumber = 0;

	do {
		currentFactor++;
		currentNumber = currentFactor*startingNumber;

		auto digits = getDigits(currentNumber);
		std::copy(digits.begin(), digits.end(), std::inserter(usedDigits, usedDigits.begin()));
	} while (usedDigits.size() < 10);

	return {currentNumber,true};
}

void generateTestCases(int nMax)
{
	const int max = nMax;
	std::cout << max + 1 << "\n";
	for (int i = 0; i < max + 1; i++) {
		std::cout << i << "\n";
	}
}

void runTestCases()
{
	// std::cout << "Counting sheep" << "\n";
	// std::cout << "--------------" << "\n";

	int caseCount;
	std::cin >> caseCount;

	// std::cout << "Received " << caseCount << " test cases." << "\n";

	std::vector<int> startingNumbers;
	startingNumbers.reserve(caseCount);
	std::copy_n(std::istream_iterator<int>(std::cin), caseCount, std::back_inserter(startingNumbers));

	// std::cout << "Read " << startingNumbers.size() << " values into vector." << "\n";
	// std::cout << "Counting sheep..." << "\n";

	for (int i = 0; i < startingNumbers.size(); i++) {
		int lastNumber = 0;
		bool fallsAsleep = false;
		std::tie(lastNumber, fallsAsleep) = countSheep(startingNumbers.at(i));

		if (!fallsAsleep) {
			std::cout << "Case #" << i + 1 << ": " << "INSOMNIA" << "\n";
		}
		else {
			std::cout << "Case #" << i + 1 << ": " << lastNumber << "\n";
		}
	}
}

int main()
{
	runTestCases();
	return 0;
}
