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
#include <sstream>
#include <map>
#include <iterator>

template<class T>
struct FileStream {
	T stream;
	FileStream(const std::string& filename) : stream(filename.c_str()) {
	}

	~FileStream() {
		stream.close();
	}
};

void QualificationRound2013B(const std::string& filename) {
	FileStream<std::ifstream> input(filename);
	FileStream<std::ofstream> output(filename + ".out");
	std::string current_line("");
	std::getline(input.stream, current_line);
	const unsigned cases = atoi(current_line.c_str());
	for (unsigned current_case = 0; current_case < cases; ++current_case) {
		int n, m;
		input.stream >> n >> m;
		std::vector<std::vector<unsigned>> lawn(n, std::vector<unsigned>(m, 0));
		for (auto i = 0; i < n; ++i)
			for (short j = 0; j < m; ++j)
				input.stream >> lawn[i][j];
		bool realizable_pattern = true;
		for (auto i = 0; i < n && realizable_pattern; ++i)
			for (auto j = 0; j < m && realizable_pattern; ++j) {
				bool fine_L = true;
				bool fine_M = true;
			for (unsigned l = 0; l < n && fine_L; ++l)
				fine_L = lawn[l][j] <= lawn[i][j];
			for (unsigned k = 0; k < m && fine_M; ++k)
				fine_M = lawn[i][k] <= lawn[i][j];
			realizable_pattern = fine_L || fine_M;
		}
		output.stream << "Case #" << current_case + 1 << ": " << (realizable_pattern ? "YES" : "NO") << std::endl;
	}
}

void main(int argc, char* argv[]) {
	std::string filename("B-large.in");
	QualificationRound2013B(filename);
}