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

typedef vector<double> vd;
typedef vector<vector<unsigned>> vvu;
typedef vector<unsigned> vu;
typedef list<unsigned> lu;
typedef priority_queue<unsigned> pu;
typedef vector<unsigned> su;




unsigned solve(vu& s, unsigned X)
{
	unsigned retval = 0;

	std::sort(s.begin(), s.end());

	for (retval = 0; !s.empty(); ++retval) {
		unsigned l = s.back();
		s.pop_back();

		auto iter = std::upper_bound(s.begin(), s.end(), X - l);

		if (iter != s.begin()) {
			s.erase(iter - 1);
		}

		DBGMSG << s.size() << endl;
	}

	return retval;
}




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

		unsigned num_testcases;
		input >> num_testcases;

		for (unsigned i = 1; i <= num_testcases; ++i) {
			/* The first line of the input gives the number of test cases, T. T test cases follow.
			 *
			 * Each test case begins with a line containing two integers: the number of files to be stored N,
			 * and the capacity of the discs to be used X (in MBs).
			 *
			 * The next line contains the N integers representing the sizes of the files Si (in MBs),
			 * separated by single spaces.
			 *
			 * Output
			 *
			 * For each test case, output one line containing "Case #x: y", where x is the case number
			 * (starting from 1) and y is the minimum number of discs needed to store the given files.
			 */
			unsigned N, X;
			input >> N >> X;

			vu s;

			for (unsigned i = 0; i < N; ++i) {
				unsigned s_i;
				input >> s_i;
				s.push_back(s_i);
			}

			int retval = solve(s, X);

			std::cout << "Case #" << i << ": ";
			if (retval < 0)
				std::cout << "Fegla Won" <<std::endl;
			else
				std::cout << retval << std::endl;
		}
	}
	return 0;
}
