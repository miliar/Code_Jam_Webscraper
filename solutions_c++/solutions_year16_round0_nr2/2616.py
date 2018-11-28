#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

unsigned long solve(std::string S)
{
	unsigned long retval = 0;

	char ref = '+';

	for (auto iter = S.rbegin(); iter != S.rend(); ++iter) {
		const char c = *iter;
		if (c != ref) {
			++retval;
			if (ref == '+')
				ref = '-';
			else
				ref = '+';
		}
	}

	return retval;
}

int main(int argc, char *argv[])
{
	if (argc < 2) {
		std::cerr << "Need an input file" << std::endl;
	}
	else {
		std::fstream input;
		input.open(argv[1], std::fstream::in);

		if (!input.is_open())
			return -1;

		unsigned T;
		input >> T;

		for (unsigned i = 1; i <= T; ++i) {
			std::string S;

			input >> S;

			auto retval = solve(S);

			std::cout << "Case #" << i << ": " << retval << std::endl;
		}
	}
	return 0;
}
