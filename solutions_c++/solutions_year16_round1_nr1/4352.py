// The Last Word

#include <fstream>
#include <string>

int main(int argc, char **argv) {
	std::ifstream input;
	std::ofstream output;

	input.open("input.txt");
	output.open("output.txt");

	int t;

	input >> t;

	for (int iT = 1; iT <= t; ++iT) {
		std::string str;
		std::string lastWord;

		input >> str;

		lastWord += str[0];

		for (int i = 1; i < str.length(); ++i) {
			char nextLetter = str[i];
			char firstLetter = lastWord[0];

			if (firstLetter <= nextLetter) {
				lastWord = nextLetter + lastWord;
			} else {
				lastWord += nextLetter;
			}
		}

		output << "Case #" << iT << ": " << lastWord << std::endl;
	}

	input.close();
	output.close();
}

