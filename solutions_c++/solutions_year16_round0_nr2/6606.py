#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <string>

using namespace std;



int calc(std::string& str) {
	int pos = -1;
	char ch = str[0];
	for (int i = 0; i < str.size(); i++) {
		if (str[i] != ch) {
			pos = i;
			break;
		}
	}
	if (pos == -1) {
		return ch == '+'? 0: 1;
	}
	for (int i = 0; i < pos; i++) {
		if (str[i] == '+') str[i] = '-'; else str[i] = '+';
	}
	return 1 + calc(str);
}

int main() {

	int T;
	cin >> T;
	string str;
	getline(cin, str);
	for (int t = 1; t <= T; t++) {
		getline(cin, str);
		int val = calc(str);
		cout << "Case #" << t << ": " << val << endl;
	}

	return 0;
}