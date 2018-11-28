#include <algorithm>
#include <climits>
#include <cmath>
#include <iostream>
#include <list>
#include <queue>
#include <sstream>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>

// ----------- Utilities ----------- \\

template<typename Iterable, typename T>
bool contains(const Iterable& container, const T& value) {
	for (T& v : container) {
		if (v == value) {
			return true;
		}
	}
	return false;
}

template<typename Iterable>
void sort(Iterable& container) {
	std::sort(container.begin(), container.end());
}


// ----------- Problem ----------- \\

std::string parse(std::string C, std::string J){
	unsigned size = C.size();
	if (C == std::string(size, '?')) {
		std::string buffer;
		if (C == J) {
			buffer = std::string(size, '0');
		} else {
			for (unsigned i = 0; i < size; i++) {
				buffer += (J[i] == '?') ?'0' : J[i];
			}
		}
		return buffer + " " + buffer;
	}

	std::unordered_map<unsigned, std::vector<unsigned>> unknowns;
	unknowns.insert(std::make_pair(0, std::vector<unsigned>()));
	unknowns.insert(std::make_pair(1, std::vector<unsigned>()));
	unsigned counter = 0;
	for (unsigned i = 0; i < size; i++) {
		if (C[i] == '?') {
			counter++;
			unknowns[0].push_back(i);
		}
		if (J[i] == '?') {
			counter++;
			unknowns[1].push_back(i);
		}
	}

	unsigned lenC = unknowns[0].size();
	std::string origC = C;
	std::string origJ = J;
	std::pair<unsigned, unsigned> min = {0, pow(10, size)};
	for (unsigned attempt = 0; attempt < pow(10, counter); attempt++) {
		auto str = std::to_string(attempt);
		while (str.length() < counter) {
			str = '0' + str;
		}
		unsigned i = 0;
		for (char c : str) {
			if (i < lenC) {
				C[unknowns[0][i]] = c;
			} else {				
				J[unknowns[1][i - lenC]] = c;
			}
			i++;
		}

		unsigned delta = abs(stoi(C) - stoi(J));
		if (delta < min.second) {
			min.first = attempt;
			min.second = delta;
		}
		C = origC;
		J = origJ;
	}

	auto str = std::to_string(min.first);
	while (str.length() < counter) {
		str = '0' + str;
	}
	unsigned i = 0;
	for (char c : str) {
		if (i < lenC) {
			C[unknowns[0][i]] = c;
		} else {				
			J[unknowns[1][i - lenC]] = c;
		}
		i++;
	}
	// return C + " " + J + " (" + std::to_string(min.first) + ", " + std::to_string(min.second) + ")";
	return C + " " + J;
}

int main(){
	unsigned T, i = 0;
	std::string C, J;

	std::cin >> T;
	for (unsigned i = 0; i < T; i++) {
		std::cin >> C >> J;
		auto r = parse(C, J);
		std::cout << "Case #" << (i+1) << ": " << r << std::endl;
	}
}
