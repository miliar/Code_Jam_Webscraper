#include <cassert>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <iterator>
#include <sstream>
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



class RevengeOfThePancakes : public Solution<RevengeOfThePancakes> {
public:
	void doRun() {
		auto stack = readLine();
		auto const result = minNumFlips(stack);
		out() << result;
	}
	static unsigned minNumFlips(std::string stack) {
		unsigned numFlips = 0;
		while (not isFinished(stack)) {
			++numFlips;
			unsigned best = stack.size() + 1;
			std::vector<unsigned> bestIndices;
			for (unsigned i = 0; i < stack.size(); ++i) {
				auto const flippedStack = flippedAt(i, stack);
				unsigned const current = numChanges(flippedStack);
				if (current < best) {
					best = current;
					bestIndices.clear();
					bestIndices.push_back(i);
				}
				else if (current == best) {
					bestIndices.push_back(i);
				}
			}
//			if (bestIndices.size() > 1) {
//				std::cerr << stack << std::endl;
//				std::cerr << best << std::endl;
//				std::copy(bestIndices.begin(), bestIndices.end(), std::ostream_iterator<unsigned>(std::cerr, " "));
//				assert(false);
//			}
			stack = flippedAt(bestIndices.front(), stack);
//			if (bestIndices.size() == 1) {
//				stack = flippedAt(bestIndices[0], stack);
//			}
//			else {
//				unsigned winner = 0;
//				for (unsigned const index: bestIndices) {
//					unsigned const current = minNumFlips(flippedAt(index, stack));
//					winner = std::max(current, winner);
//				}
//				return winner;
//			}
		}
		return numFlips;
	}
	static unsigned numChanges(std::string const & stack) {
		unsigned count = 0;
		char lastChar = flipped(stack[0]);
		for (unsigned i = 0; i < stack.size(); ++i) {
			char const currentChar = stack[i];
			if (currentChar != lastChar) {
				++count;
			}
			lastChar = currentChar;
		}
		return count;
	}
	static unsigned longestRun(std::string const & stack) {
		unsigned bestRun = 0;
		unsigned currentRun = 1;
		char lastChar = flipped(stack[0]);
		for (unsigned i = 0; i < stack.size(); ++i) {
			char const currentChar = stack[i];
			if (currentChar == lastChar) {
				++currentRun;
				bestRun = std::max(bestRun, currentRun);
			}
			else {
				currentRun = 1;
			}
			lastChar = currentChar;
		}
		return bestRun;
	}
	static std::string flippedAt(unsigned const index, std::string const & stack) {
		std::string result{stack};
		for (unsigned i = 0; i <= index/2; ++i) {
			unsigned j = index - i;
			char const first = flipped(result[i]);
			char const last = flipped(result[j]);
			result[i] = last;
			result[j] = first;
		}
		return result;
	}
	static bool isFinished(std::string const & stack) {
		return stack.find_first_of('-') == std::string::npos;
	}
	static char flipped(char const c) {
		switch (c) {
			case '-': return '+';
			case '+': return '-';
			default: assert(false); return '0';
		}
	}
};

int main(int argc, char** argv) {
	RevengeOfThePancakes solution;

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
