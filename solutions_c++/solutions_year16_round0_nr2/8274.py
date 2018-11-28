// Revenge of the Pancakes

#include <fstream>
#include <cstdlib>
#include <string>

int solve(std::string pancakes) {
	int moves = 0;
	char last = pancakes[0];

	for (int i = 1; i < pancakes.length(); ++i) {
		char cur = pancakes[i];

		if (cur != last) {
			++moves;
		}

		last = cur;
	}

	if (last == '-') {
		++moves;
	}

	return moves;
}

int main(int argc, char **argv) {
	std::ifstream input;
	std::ofstream output;

	input.open("input.txt");
	output.open("output.txt");

	int t;

	input >> t;

	for (int iT = 1; iT <= t; ++iT) {
		std::string pancakes;

		input >> pancakes;

		int answer = solve(pancakes);

		output << "Case #" << iT << ": " << answer << std::endl;
	}

	input.close();
	output.close();
}
