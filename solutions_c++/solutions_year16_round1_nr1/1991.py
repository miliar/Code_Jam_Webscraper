#include <iostream>
#include <string>

using namespace std;

string sort_char(string str) {
	string result = "";
	char max_char = 0;
	for (int i = 0; i < str.size(); i++) {
		char item = str[i];
		if (item >= max_char) {
			result = str[i] + result;
			max_char = str[i];
		}
		else {
			result.push_back(str[i]);
		}
	}
	return result;
}

int main() {
	int t;
	cin >> t;
	string s;
	getline(cin, s);
	for (int i = 1; i <= t; i++) {
		string s;
		getline(cin, s);
		string res = sort_char(s);
		cout << "Case #" << i << ": " << res << endl;
	}
	return 0;
}