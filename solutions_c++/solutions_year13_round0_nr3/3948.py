#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <array>
#include <string>
#include <memory>
#include <cmath>
#include <cstdlib>

template<class T>
struct FileStream {
	T stream;
	FileStream(const std::string& filename) : stream(filename.c_str()) {
	}

	~FileStream() {
		stream.close();
	}
};

bool is_fair(int number) {
	static std::string view("");
	view = std::to_string(number);
	std::string feflected_view(view.rbegin(), view.rend());
	return view == feflected_view;
}

const std::vector<int>& fairs_in_range(int left, int right) {
	static std::vector<int> result;
	result.clear();
	for (int number = left; number <= right; ++number) {
		if (is_fair(number)) {
			result.push_back(number);
		}
	}
	return result;
}

void QualificationRound2013C(const std::string& filename) {
	FileStream<std::ifstream> input(filename);
	FileStream<std::ofstream> output(filename + ".out");
	std::string current_line("");
	std::getline(input.stream, current_line);
	const int cases = atoi(current_line.c_str());
	for (int current_case = 0; current_case < cases; ++current_case) {
		int result = 0;
		int left_bound;
		int right_bound;
		input.stream >> left_bound >> right_bound;
		int real_left_bound = ceil(sqrt(left_bound));
		int real_right_bound = sqrt(right_bound);
		const std::vector<int>& current_sqrts = fairs_in_range(real_left_bound, real_right_bound);
		for (int number : current_sqrts) {
			int sqr = powl(number, 2);
			if (is_fair(sqr)) {
				++result;
			}
		}
		output.stream << "Case #" << current_case + 1 << ": " << result << std::endl;
	}
}

void main(int argc, char* argv[]) {
	std::string filename("C-small-attempt0.in");
	QualificationRound2013C(filename);
}