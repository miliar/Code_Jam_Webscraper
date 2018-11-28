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
typedef priority_queue<unsigned, std::vector<unsigned>, std::greater<unsigned> > rpu;
typedef set<unsigned> su;


template <typename T>
void DBG_QUEUE(T copy)
{
#ifdef DEBUG
	DBGMSG << "p: [";

	while (!copy.empty()) {
		DBGMSG << copy.top() << ", ";
		copy.pop();
	}

	DBGMSG << "]" << endl;
#endif
}


unsigned solve2(pu& p)
{
	DBG_QUEUE(p);

	if (p.top() <= 3)
		return p.top();

	size_t retval = p.top();

	unsigned max_smaller_pow2 = 1;
	for (unsigned i = 1; i < p.top(); i <<= 1)
		max_smaller_pow2 = i;

	auto v = p.top();

	vu tmp;

	while (!p.empty() && p.top() == v) {
		p.pop();
		tmp.push_back(v);
	}

	for (unsigned v_1 = (v >> 1); v_1 <= max_smaller_pow2; v_1++) {
		auto p_copy = p;
		for (size_t c = 0; c < tmp.size(); ++c) {
			p_copy.push(v_1);
			p_copy.push(v - v_1);
		}

		auto result = solve2(p_copy) + tmp.size();
		retval = std::min(retval, result);
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

		unsigned T;
		input >> T;

		for (unsigned t = 1; t <= T; ++t) {
			/*
			 *
			 */
			unsigned D;
			input >> D;

			pu p;

			for (unsigned i = 0; i < D; ++i) {
				unsigned p_i;
				input >> p_i;
				p.push(p_i);
			}

			unsigned retval = solve2(p);

			std::cout << "Case #" << t << ": " << retval << std::endl;
		}
	}
	return 0;
}
