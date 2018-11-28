#include <iostream>
#include <sstream>
#include <string>

#include <deque>
#include <set>
#include <algorithm>
#include <functional>

// Using boost libraries (1.53.0)
// https://sourceforge.net/projects/boost/files/boost/1.53.0/
#include <boost/date_time/posix_time/posix_time.hpp>
#include <boost/format.hpp>
#include <boost/foreach.hpp>

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

int play_deceitful_war(std::set<double> naomi, std::set<double> ken) {
	int points = 0;
	LOG << "Playing Deceitful War" << std::endl;
	size_t N = naomi.size();
	for (size_t i = 0; i < N; ++i) {
		std::set<double>::iterator n = std::min_element(naomi.begin(), naomi.end());
		LOG << "Naomi plays " << *n << std::endl;
		std::set<double>::iterator min_k = std::min_element(ken.begin(), ken.end());
		std::set<double>::iterator max_k = std::max_element(ken.begin(), ken.end());
		std::set<double>::iterator k;
		if (*n < *min_k) {
			LOG << "She says it is just less than " << *max_k << std::endl;
			k = max_k;
		} else {
			LOG << "She says it is greater than " << *max_k << std::endl;
			k = min_k;
		}
		LOG << "Ken plays " << *k << std::endl;
		if (*n < *k) {
			LOG << "Ken wins the point" << std::endl;
		} else {
			LOG << "Naomi wins the point" << std::endl;
			++points;
		}
		naomi.erase(n);
		ken.erase(k);
	}
	LOG << "Naomi won " << points << " playing Deceitful War" << std::endl;
	return points;
}

int play_war(std::set<double> naomi, std::set<double> ken) {
	int points = 0;
	LOG << "Playing War" << std::endl;
	BOOST_FOREACH(const double& nb, naomi) {
		LOG << "Naomi chooses " << nb << std::endl;
		std::set<double>::iterator kb_iter = ken.upper_bound(nb);
		if (kb_iter == ken.end()) {
			kb_iter = ken.begin();
		}
		double kb = *kb_iter;
		LOG << "Ken chooses " << kb << std::endl;
		if (nb > kb) {
			LOG << "Naomi wins the point" << std::endl;
			++points;
		} else {
			LOG << "Ken wins the point" << std::endl;
		}
		ken.erase(kb_iter);
	}
	LOG << "Naomi won " << points << " playing War" << std::endl;
	return points;
}

std::string solve_test_case() {
	int N;
	std::cin >> N;

	LOG << "Each person has " << N << " blocks" << std::endl;
	std::set<double> naomi;
	for (auto i = 0; i < N; ++i) {
		double b;
		std::cin >> b;
		LOG << "Naomi has " << b << std::endl;
		naomi.insert(b);
	}

	std::set<double> ken;
	for (auto i = 0; i < N; ++i) {
		double b;
		std::cin >> b;
		LOG << "Ken has " << b << std::endl;
		ken.insert(b);
	}

	return boost::str(boost::format("%d %d") % play_deceitful_war(naomi, ken) % play_war(naomi, ken));
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
