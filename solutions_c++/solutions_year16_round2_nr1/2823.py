#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <sstream>

using namespace std;

typedef map<char, int> map_t;

bool present(map_t& chars, string const& digit) {
	map_t dig;
	for(int i = 0 ; i< digit.size(); i++) {
		dig[digit[i]]++;
	}
	for (auto it = dig.begin(); it != dig.end(); ++it) {
		if (chars[it->first] < dig[it->first]) {
			return false;
		}
	}
	return true;
}

void remove(map_t& chars, string const& digit) {
	for (int i = 0; i < digit.size(); i++) {
		chars[digit[i]]--;
	}
}

int main() {
	string digits[] = {
		"ZERO",
		"ONE",
		"TWO",
		"TRHEE",
		"FOUR",
		"FIVE",
		"SIX",
		"SEVEN",
		"EIGHT",
		"NINE"
	};

	int T;
	cin >> T;
	string str;
	getline(cin, str);
	for (int t = 1; t <= T; t++) {
		getline(cin, str);
		vector<int> result;
		map_t chars;
		for (int i = 0; i < str.size(); i++) {
			chars[str[i]]++;
		}
		while (true) {
			if (chars['Z'] > 0) {
				result.push_back(0);
				remove(chars, digits[0]);
				continue;
			} else if (chars['W'] > 0) {
				result.push_back(2);
				remove(chars, digits[2]);
				continue;
			} else if (chars['G'] > 0) {
				result.push_back(8);
				remove(chars, digits[8]);
				continue;
			} else if (chars['U'] > 0) {
				result.push_back(4);
				remove(chars, digits[4]);
				continue;
			}
			break;
		}

		int curDigit = 0;
		while (!chars.empty() && curDigit < 10) {
			if (present(chars, digits[curDigit])) {
				remove(chars, digits[curDigit]);
				result.push_back(curDigit); 
			} else {
				curDigit++;
			}
		}
		sort(result.begin(), result.end(), std::less<int>());
		cout << "Case #" << t << ": ";
		for (int i = 0; i < result.size(); i++) cout << result[i];
		cout << endl;
	}

	return 0;
}