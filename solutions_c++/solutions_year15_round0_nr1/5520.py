#include <algorithm>
#include <cassert>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>

#ifdef DEBUG
#define DBGMSG	std::cerr
#else
#define DBGMSG	if (0) std::cerr
#endif

using namespace std;

int main(int argc, char** argv)
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

		for (unsigned t = 1; t <= T; ++t) {
			unsigned s_max;
			std::string s_str;
			input >> s_max >> s_str;

			unsigned audience = 0;
			unsigned friends = 0;

			assert(s_str.size() == s_max + 1);

			for (unsigned i = 0; i <= s_max; ++i) {
				int s_i = s_str[i] - '0';

				assert(s_i >= 0);
				assert(s_i <= 9);

				if (s_i > 0) {
					unsigned required = i;
					if (audience < required)
						friends = std::max(friends, required - audience);

					audience += s_i;
				}
			}

			std::cout << "Case #" << t << ": " << friends << std::endl;
		}
	}

	return 0;
}
