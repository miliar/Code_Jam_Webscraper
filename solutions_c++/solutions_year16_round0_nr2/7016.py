#include <fstream>
#include <iostream>
#include <string>

int main(int argc, char** argv)
{
	int T;
	std::ifstream ifs(argv[1]);
	std::ofstream ofs(argv[2]);
	ifs >> T;
	for (int i = 1; i <= T; ++i) {
		int min_flips = 0;
		std::string pancakes;
		ifs >> pancakes;
		while (pancakes.find('-') != std::string::npos) {
			++min_flips;
			const size_t last_minus = pancakes.rfind('-');
			for (size_t j = 0; j <= last_minus; ++j) {
				if (pancakes[j] == '+')
					pancakes[j] = '-';
				else
					pancakes[j] = '+';
			}
		}
		ofs << "Case #" << i << ": " << min_flips << std::endl;
	}
}
