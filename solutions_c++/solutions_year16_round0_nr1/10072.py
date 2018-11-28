#include <cassert>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <utility>
#include <iterator>
#include <numeric>
#include <string>
#include <limits>
#include <cmath>
#include <algorithm>
#include <exception>
#include <set>

using namespace std;

// use for ALL floating point comparisons 
template <typename T, typename = enable_if<is_floating_point<T>::value>>
constexpr inline bool fequal(T lhs, T rhs,
	T epsilon = numeric_limits<T>::epsilon())
{
	return fabs(lhs - rhs) < epsilon;
}


inline void FillSet(set<char>&s, const std::string& str) {
	for (const auto& c : str) {
		if (isdigit(c)) s.insert(c);
	}
}


int main()
{
	ofstream ofile("A-S-OUT.out");
	ifstream ifile("A-S-IN.in");

	if (!ofile || !ifile) throw std::runtime_error("error opening files"); // quick check

	size_t T = 15;
	ifile >> T;

	for (size_t test_case = 1; test_case <= T; ++test_case) {

		unsigned int N;
		ifile >> N;

		if (N == 0) { // special case 
			ofile << "Case #" << test_case << ": " << "INSOMNIA" << '\n';
			continue;
		}

		set<char>results;

		uint64_t answer = N;
		uint64_t count = 1;

		for (uint64_t count = 1; results.size() != 10; ++count) {
			answer = N * count;
			FillSet(results, to_string(answer));
		}

		ofile << "Case #" << test_case << ": " << answer << '\n';
	}

	system("pause");
	return 0;
}