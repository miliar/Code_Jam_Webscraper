#include <algorithm>
#include <fstream>
#include <iostream>

using namespace std;

uint64_t solve(uint64_t number)
{
	static const unsigned dest = 0x3ff;

	auto			mask = 0u;
	auto			val = number;
	const uint64_t	limit = std::numeric_limits<uint64_t>::max() - number;

	while (val <= limit) {
		for (auto j = val; j;) {
			mask |= 1 << (j % 10);
			j /= 10;
		}

		if (mask == dest)
			break;

		val += number;
	}

	return val;
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
			uint32_t N;

			input >> N;

			if (N > 0) {
				auto retval = solve(N);

				std::cout << "Case #" << i << ": " << retval << std::endl;
			}
			else {
				std::cout << "Case #" << i << ": " << "INSOMNIA" << std::endl;
			}
		}
	}
	return 0;
}
