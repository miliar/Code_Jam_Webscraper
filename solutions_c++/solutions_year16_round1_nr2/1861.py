#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>
#include <functional>
#include <iterator>
#include <cstdint>

struct CodeJam {

	void conquer(std::istream &cin, std::ostream &cout) {
		int N;
		cin >> N;
		std::map<int, int> frec;
		for (int j = 0, jn = N*(2 * N - 1); j < jn; ++j) {
			int h;
			cin >> h;
			++frec[h];
		}

		std::vector<int> heights;
		for (std::pair<int, int> p : frec) {
			if (p.second % 2) {
				heights.push_back(p.first);
			}
		}

		std::sort(heights.begin(), heights.end());
		std::copy(heights.begin(), heights.end(), std::ostream_iterator<int>(cout, " "));
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
