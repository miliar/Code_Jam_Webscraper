#include <iostream>
#include <sstream>
#include <string>

#include <set>
#include <algorithm>
#include <iterator>

// Using boost libraries (1.55.0)
// https://sourceforge.net/projects/boost/files/boost/1.55.0/
#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/lexical_cast.hpp>

// get a line of input
template <typename T>
T gl() {
	std::string s;
	std::getline(std::cin, s);
	std::istringstream ss(s);
	T result;
	ss >> result;
	return result;
}

template <>
std::string gl<std::string>() {
	std::string s;
	std::getline(std::cin, s);
	return s;
}


#define LOG \
	std::cerr << boost::posix_time::microsec_clock::local_time() \
<< ": " << __FILE__ << ": " << __LINE__ << ": "

int solve_test_case() {
	int s_max;
	std::cin >> s_max;
	LOG << "Smax = " << s_max << std::endl;
	std::string s_digits;
	std::cin >> s_digits;
	LOG << "Sdigits = " << s_digits << std::endl;
	int running_total = 0;
	int total_added = 0;
	for (auto i = 0; i <= s_max; ++i) {
		if (running_total < i) {
			auto needed = i - running_total;
			LOG << "Inviting " << needed << std::endl;
			total_added += needed;
			running_total += needed;
		}
		running_total += boost::lexical_cast<int>(s_digits[i]);

	}
	return total_added;
}

int main (int argc, char ** argv) {
	auto N = gl<int>();
	LOG << "There are " << N << " test cases" << std::endl;
	for (auto i = 1; i <= N; ++i) {
		LOG << "Attempting case #" << i << std::endl;
		auto result = solve_test_case();
		LOG << "Case #" << i << ": " << result << std::endl;
		std::cout << "Case #" << i << ": " << result << std::endl;
	}
}
