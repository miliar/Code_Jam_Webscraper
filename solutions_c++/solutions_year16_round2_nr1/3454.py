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
	for (T v : container) {
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

/*
Z -> zero
W -> two
X -> six
G -> eight
*/

void remove(std::string& S, std::string chars) {
	if (chars.size() == 0) {
		return;
	}
	for (auto it = S.begin(); it != S.end(); it++) {
		if (*it == chars[0]) {
			S.erase(it);
			chars.erase(chars.begin());
			remove(S, chars);
			break;
		}
	}
}

std::string parse(std::string S, std::vector<int> blacklist){
	std::string original = S;
	std::unordered_map<std::string, int> numbers = {
		{"ZERO", 0},
		{"ONE", 1},
		{"TWO", 2},
		{"THREE", 3},
		{"FOUR", 4},
		{"FIVE", 5},
		{"SIX", 6},
		{"SEVEN", 7},
		{"EIGHT", 8},
		{"NINE", 9}
	};
	std::vector<int> digits;
	while (S.size() > 0) {
		for (char c : S) {
			if (c == 'Z') {
				digits.push_back(0);
				remove(S, "ZERO");
				break;
			}
			if (c == 'W') {
				digits.push_back(2);
				remove(S, "TWO");
				break;
			}
			if (c == 'X') {
				digits.push_back(6);
				remove(S, "SIX");
				break;
			}
			if (c == 'G') {
				digits.push_back(8);
				remove(S, "EIGHT");
				break;
			}

			bool shouldBreak = false;
			for (auto pair : numbers) {
				bool found = true;
				for (char c : pair.first) {
					if (S.find(c) == std::string::npos) {
						found = false;
						break;
					}
				}

				if (found) {
					if (contains(blacklist, pair.second)) {
						continue;
					}
					// std::cout << "found: " << pair.second << std::endl;
					digits.push_back(pair.second);
					remove(S, pair.first);
					// std::cout << "result: " << S << std::endl;
					shouldBreak = true;
					break;
				}
			}

			if (!shouldBreak) {
				blacklist.push_back(digits.back());
				digits.pop_back();
				return parse(original, blacklist);
			}

			if (shouldBreak) {
				break;
			}
		}
	}

	sort(digits);
	std::string result;
	for (int d : digits) {
		result += std::to_string(d);
	}
	return result;
}

std::string parse(std::string S) {
	return parse(S, std::vector<int>());
}



int main(){
	unsigned T, i = 0;
	std::string S;

	std::cin >> T;
	for (unsigned i = 0; i < T; i++) {
		std::cin >> S;
		auto r = parse(S);
		std::cout << "Case #" << (i+1) << ": " << r << std::endl;
	}
}
