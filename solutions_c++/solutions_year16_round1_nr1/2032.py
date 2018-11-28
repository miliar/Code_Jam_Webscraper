#include <iostream>
#include <vector>
using namespace std;

string lastword(string s) {
	if (s.empty()) return "";
	//int m[26] = {0};
	string result = "";
	result += s[0];
	for (int i = 1; i < s.size(); i++) {
		if (s[i] >= result[0]) {
			result = s[i] + result;
		} else {
			result = result + s[i];
		}
	}

	return result;
}

int main() {
	int t;
	string n;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n and then m.
		cout << "Case #" << i << ": " << lastword(n) << endl;
	}
}