#include <iostream>
#include <list>
using namespace std;


void solve() {
	string s;
	string r;

	cin >> s;

	r += s.at(0);

	for (int i = 1; i < s.length(); i++) {
		char c = s.at(i);
		if (c >= r.at(0)) {
			r = c + r;
		} else {
			r = r + c;
		}
	}

	cout << r << endl;
}



int main() {
	int T;

	cin >> T;

	for (int i = 0; i < T; i++) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
	return 0;
}