#include <iostream>
#include <sstream>
#include <set>

using namespace std;

void solve() {
	int n;
	cin >> n;
	if (n == 0) {
		cout << " " << "INSOMNIA" << endl;
	} else {
		set<char> st;
		for (long long i = n;; i += n) {
			stringstream sout;
			sout << i;
			for (char c : sout.str()) {
				st.insert(c);
			}
			if (st.size() == 10) {
				cout << " " << i << endl;
				break;
			}
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ":";
		solve();
	}
}
