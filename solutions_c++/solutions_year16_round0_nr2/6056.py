#include <iostream>
#include <cstdio>
#include <streambuf>
#include <array>
#include <cstdio>
#include <string>
#include <bitset>
#include <vector>

//template<int N>
int string_to_bitset(const std::string& line, std::vector<bool>& bitset) {
	int n = 0;

	bitset.clear();

	for (auto i : line) {
		switch (i)
		{
		case '+':
			bitset.push_back(1);
			break;
		case '-':
			bitset.push_back(0);
			break;
		default:
			return bitset.size();
		}
		n++;
	}
	return bitset.size();
}


void problemB() {
	unsigned flips;
	unsigned num_tests;
	std::string line;
	
	std::getline(std::cin, line);
	num_tests = std::stoi(line);

	//std::bitset<100> bits;
	unsigned lenght;
	std::vector<bool> bits;
	bits.reserve(100);


	for (int i = 1; i <= num_tests; i++) {
		std::getline(std::cin, line);
		lenght = string_to_bitset(line, bits);

		int flips = 0;
		char last = 'x';

		for (auto i : line) {
			if (i == '+' || i == '-') {
				if (i != last) {
					last = i;
					flips++;
				}
			}
		}

		if (last == '+') {
			flips--;
		}

		std::cout << "Case #" << i << ": " << flips << "\n";
	}
}

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	problemB();
}