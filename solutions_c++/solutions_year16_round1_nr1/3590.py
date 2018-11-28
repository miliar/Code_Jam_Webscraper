#include <iostream>
#include <string>

using namespace std;

string getLastWord(string s) {
	string output;
	for (const auto& c : s) {
		if (c < output[0]) {
			output += c;
		} else {
			output = c + output;
		}
	}
	return output;
}

int main() {
	int n;
	cin >> n;
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		cout << "Case #" << i+1 << ": " << getLastWord(s) << "\n";
	}
	return 0;
}