// -std=c++11

#include <iostream>
#include <string>
#include <list>

using namespace std;

string last_word(const string& initial) {
	list<char> board;
	for (char c : initial) {
		if (c >= board.front()) {
			board.push_front(c);
		} else {
			board.push_back(c);
		}
	}
	return string(board.begin(), board.end());
}

int main() {
	int count;
	cin >> count;
	for (int c = 1; c <= count; c++) {
		string initial;
		cin >> initial;
		cout << "Case #" << c << ": " << last_word(initial) << endl;
	}
	return 0;
}
