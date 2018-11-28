#include <iostream>
#include <cstdlib>
#include <unordered_set>
#include <string>
#include <algorithm>
#include <cassert>


std::string solveProblem(std::string N) {
	if (N == "0") {
		return "INSOMNIA";		
	}
	int valueToAdd = std::stoi(N);

	std::unordered_set<char> seenDigits;

	for_each(N.begin(), N.end(), [&seenDigits](char c) {
		seenDigits.insert(c);
	});
	assert(seenDigits.size() <= 10);
	if (seenDigits.size() == 10) {
		return N;
	}

	while (seenDigits.size() < 10) {
		N = std::to_string(std::stoi(N) + valueToAdd);
		for_each(N.begin(), N.end(), [&seenDigits](char c) {
			seenDigits.insert(c);
		});
		assert(seenDigits.size() <= 10);
	}

	return N;
}

int main () {
    int T;
    std::cin >> T;

    for (int test = 1; test <= T; ++test) {
        std::string N;
        std::cin >> N;


        std::cout << "Case #" << test << ": " << solveProblem(N) << std::endl;

    }

    return EXIT_SUCCESS;
}
