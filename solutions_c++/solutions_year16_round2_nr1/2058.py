#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iterator>
#include <cstdint>
#include <cassert>

char *words[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
struct CodeJam {
	void conquer(std::istream &cin, std::ostream &cout) {
		std::string s;
		cin >> s;
		std::vector<int> chars(26);
		int *p = &chars[0] - 'A';
		for (char c : s) {
			p[c]++;
		}

		std::vector<int> nums(10);
		nums[0] = p['Z'];
		nums[6] = p['X'];
		nums[4] = p['U'];
		nums[2] = p['W'];
		nums[8] = p['G'];
		nums[3] = p['H'] - nums[8];
		nums[5] = p['F'] - nums[4];
		nums[7] = p['V'] - nums[5];
		nums[9] = p['I'] - nums[5] - nums[6] - nums[8];
		nums[1] = p['N'] - nums[7] - nums[9] - nums[9];

		for (int j = 0; j < 10; ++j) {
			for (int k = 0; k < nums[j]; ++k) {
				cout << j;
			}
		}
		
	}
private:

};

int main(int argc, char **argv) {
	std::ifstream ifstream;
	std::ofstream ofstream;
	if (argc > 1) {
		ifstream.open(argv[1]);
		std::string out(argv[1]);
		out.append(".out");
		ofstream.open(out.c_str());
		if (argc > 2) {
			ofstream.open(argv[2]);
		}
	}

	std::istream &cin(argc > 1 ? ifstream : std::cin);
	std::ostream &cout(argc > 1 ? ofstream : std::cout);

	int T;
	cin >> T;

	std::string line;
	std::getline(cin, line);

	for (int t = 1; t <= T; ++t) {
		cout << "Case #" << t << ": ";
		CodeJam jam;
		jam.conquer(cin, cout);
		cout << std::endl;
	}
}
