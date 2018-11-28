#include <iostream>
#include <string>
#include <set>
#include <cstdlib>

using namespace std;

void updateSet(const string &str, set<int> &set_digit) {
	for (int i = 0; i < str.length(); i ++) {
		set_digit.insert(str[i] - '0');
	}
}

bool checkIncludeAll(const set<int> &set_digit) {
	for (int i = 0; i <= 9; i ++) {
		if (set_digit.find(i) == set_digit.end()) {
			return false;
		}
	}
	return true;
}

string getLastSheepCount(int N) {
	if (N <= 0) {
		return "INSOMNIA";
	}

	int n = 0;
	bool bl_all_include = false;
	set<int> set_digit;

	while (!bl_all_include) {
		n += N;
		string str_num = std::to_string(n);
		updateSet(str_num, set_digit);
		bl_all_include = checkIncludeAll(set_digit);
	}
	return std::to_string(n);
}

int main() {
	int t, T, N;
	cin >> T;

	t = 0;
	while (T-- > 0) {
		cout << "Case #" << ++t << ": ";
		cin >> N;
		cout << getLastSheepCount(N) << endl;
	}
	return 0;
}
