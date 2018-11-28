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

struct CodeJam {
	void conquer(std::istream &cin, std::ostream &cout) {
		std::string s;
		cin >> s;
		std::string res;
		for (char c : s) {
			std::string left = std::string(1, c) + res;
			if (left > res) {
				res = left;
			}
			else {
				res.push_back(c);
			}
		}
		cout << res;
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
