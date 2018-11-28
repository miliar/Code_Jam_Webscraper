#include <cassert>
#include <cmath>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <set>
#include <string>
#include <vector>

#include <experimental/optional>

namespace codejam {

template <class T>
std::string toString(const T& t) {
	std::ostringstream out;
	out << t;
	return out.str();
}

std::string toString(const bool value);

template <class T>
T fromString(std::string const & s) {
	std::istringstream in(s);
	T result;
	in >> result;
	return result;
}

template <typename IteratorT>
std::string join(
		IteratorT begin,
		IteratorT end,
		std::string delimiter) {
	std::ostringstream out;
	std::copy(begin, end, std::ostream_iterator<std::string>(out, delimiter.c_str()));
	std::string result = out.str();
	return result.empty() ? result : result.substr(0, result.size()-delimiter.size());
}

template <typename ContainerT>
std::string join(
		ContainerT const & container,
		std::string delimiter) {
	return join(container.begin(), container.end(), delimiter);
}

template <typename ElementT>
std::vector<ElementT> split(
		std::string const & splittee,
		std::string const & delimiters = " ") {
	std::vector<ElementT> result;
	if (splittee.empty()) {
		return result;
	}
	auto first = splittee.find_first_not_of(delimiters);
	auto second = splittee.find_first_of(delimiters);
	while (second != std::string::npos) {
		auto size = second - first;
		result.push_back(fromString<ElementT>(splittee.substr(first, size)));
		first = splittee.find_first_not_of(delimiters, second);
		second = splittee.find_first_of(delimiters, first);
	}
	if (first != std::string::npos) {
		result.push_back(fromString<ElementT>(splittee.substr(first)));
	}
	return result;
}

}


namespace codejam {

template <typename DerivedT>
class Solution {
public:
	void run(std::istream & input, std::ostream & output) {
		_in = &input;
		_out = &output;
		auto const numCases = read<unsigned>();
		for (unsigned caseIndex = 1; caseIndex <= numCases; ++caseIndex) {
			out() << "Case #" << caseIndex << ": ";
			derived().doRun();
			out() << std::endl;
		}
	}

protected:
	std::istream & in() {return *_in;}
	std::ostream & out() {return *_out;}

	template <typename T>
	T read() {
		T result;
		in() >> result;
		return result;
	}

	std::string readLine() {
		std::string line;
		while (line.empty()) {
			std::getline(in(), line);
		}
		return line;
	}

	template <typename T>
	std::vector<T> readVector() {
		std::string line;
		while (line.empty()) {
			std::getline(in(), line);
		}
		return split<T>(line);
	}

	template <typename T>
	std::vector<T> readVector(unsigned count) {
		T value;
		std::vector<T> result;
		for (unsigned i = 0; i < count; ++i) {
			in() >> value;
			result.push_back(value);
		}
		return result;
	}

private:
	DerivedT & derived() {return static_cast<DerivedT &>(*this);}

	std::istream * _in;
	std::ostream * _out;

}; // class Solution

}

using namespace codejam;
using namespace std;


class CoinJam : public Solution<CoinJam> {
public:
	using CoinType = std::string;
	using NumberType = uint64_t;
	void doRun() {
		auto const n = read<unsigned>();
		auto const j = read<unsigned>();
		CoinType coin = initialCoin(n);
		unsigned numFound = 0;
		while (numFound < j) {
			std::vector<NumberType> divisors = divisorsOf(coin);
			if (not divisors.empty()) {
				out() << std::endl;
				++numFound;
				out() << coin << " ";
				std::ostringstream o;
				std::copy(divisors.begin(), divisors.end(), std::ostream_iterator<NumberType>(o, " "));
				auto divisorString = o.str();
				out() << divisorString.substr(0, divisorString.size() - 1);
			}
			increment(coin);
		}
	}

	static std::vector<NumberType> divisorsOf(CoinType const & coin) {
		std::vector<NumberType> divisors;
		for (unsigned base = 2; base <= 10; ++base) {
			NumberType const number = toDecimal(coin, base);
			auto divisor = lowestDivisorOf(number);
			if (not divisor) {
				return std::vector<NumberType>();
			}
			else {
				divisors.push_back(*divisor);
			}
		}
		return divisors;
	}

	static std::string initialCoin(unsigned const n) {
		std::string result(n, '0');
		result.front() = '1';
		result.back() = '1';
		return result;
	}

	static bool increment(CoinType & coin) {
		for (int position = coin.size() - 2; position >= 1; --position) {
			auto & bit = coin[position];
			if (bit == '0') {
				bit = '1';
				return true;
			}
			bit = '0';
		}
		return false;
	}
	static NumberType toDecimal(CoinType const & coin, NumberType const base) {
		NumberType result = 0;
		NumberType multiplier = 1;
		for (int i = coin.size() - 1; i >= 0; --i) {
			if (coin[i] == '1') {
				result += multiplier;
			}
			multiplier *= base;
		}
		return result;
	}
	static std::experimental::optional<NumberType> lowestDivisorOf(NumberType const number) {
		NumberType const stop = std::sqrt(number);
		for (NumberType i = 3; i <= stop + 1; ++i) {
			if ((number % i) == 0) {
				return i;
			}
		}
		return {};
	}
};

int main(int argc, char** argv) {
	CoinJam solution;

	if (argc == 1) {
		solution.run(std::cin, std::cout);
	}
	else if (argc == 3) {
		ifstream in(argv[1]);
		ofstream out(argv[2]);
		solution.run(in, out);
	}

	return 0;
}
