#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void append(string& str, const char c) {
	int len = str.size();
	// find the first instance of a character that is not equivalent to c and compare it to c
	int idx = 0;
	while (idx < len) {
		char curchar = str[idx];
		if (curchar != c) {
			if (curchar > c) {
				// append to end
				str += c;
			} else {
				// append to front
				str = c + str;
			}
			return;
		}
		idx++;
	}
	// if code has reached here, means that either string is empty
	// or every character in string is equal to c, so just slot c in wherever
	str += c;
}

int main(int argc, char** argv) {
	int numCases;
	cin >> numCases;
	for (int i = 1; i <= numCases; i++) {
		string str;
		cin >> str;
		int len = (int) str.size();
		string cur = ""; // the current lowest-ordered string
		for (int ci = 0; ci < len; ci++) {
			char c = str[ci];
			append(cur, c);
		}
		cout << "Case #" << i << ": " << cur << endl;
	}
	return 0;
}
