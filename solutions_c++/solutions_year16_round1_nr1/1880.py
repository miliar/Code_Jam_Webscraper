#include <iostream>
#include <list>
#include <string>

using namespace std;

int main() {
	int T;
	list<char> op;
	string s;

	cin >> T;

	for (int i = 1; i <= T; ++i) {
		cin >> s;

		op.clear();
		op.push_back(s[0]);
		for (int j = 1; j < s.size(); ++j) {
			if (s[j] >= (*(op.begin()))) {
				op.push_front(s[j]);
			}
			else {
				op.push_back(s[j]);
			}
		}

		cout << "Case #" << i << ": ";
		for (auto x : op) {
			cout << x;
		}
		cout << "\n";

	}
	
	return 0;
}