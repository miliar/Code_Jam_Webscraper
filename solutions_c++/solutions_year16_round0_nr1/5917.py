#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <set>
#include <string>
#include <vector>

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


class CountingSheep: public Solution<CountingSheep> {
public:
	using DigitType = uint8_t;
	using NumberType = uint64_t;
	void doRun() {
		auto const multiple = read<NumberType>();
		if (multiple == 0) {
			out() << "INSOMNIA";
			return;
		}
		NumberType sum = 0;
		std::set<DigitType> digits;
		while (digits.size() < 10) {
			sum += multiple;
			includeDigitsFrom(sum, digits);
		}
		out() << sum;
	}
	void includeDigitsFrom(NumberType number, std::set<DigitType> & digits) {
		while (number > 0) {
			digits.insert(number % 10);
			number /= 10;
		}
	}

};

int main(int argc, char** argv) {
	CountingSheep solution;

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
