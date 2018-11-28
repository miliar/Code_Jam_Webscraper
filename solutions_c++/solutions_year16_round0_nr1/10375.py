#include <iostream>
#include <array>
#include <algorithm>

#ifdef _DEBUG
#include <fstream>
std::ifstream in("input.in");
std::ofstream out("output.txt");
#elif
std::istream& in = std::cin;
std::ostream& out = std::cout;
#endif


int main() {
	int tCase, counter;
	long long num, tnum;
	std::array<bool, 10> seen;

	in >> tCase;
	for (int i = 0; i < tCase; i++) {
		in >> num;
		if (num == 0) {
			out << "Case #" << i+1 <<": INSOMNIA\n";
			continue;
		}
		std::fill(seen.begin(), seen.end(), false);
		counter = 1;
		while (std::any_of(seen.begin(), seen.end(), [](bool t) {
			return !t;
		})) {
			tnum = num * counter++;
			while (tnum / 10 != 0) {
				seen[tnum % 10] = true;
				tnum /= 10;
			}
			seen[tnum] = true;
		}
		out << "Case #" << i + 1 << ": " << num * (counter - 1) <<"\n";
	}
	return 0;
}