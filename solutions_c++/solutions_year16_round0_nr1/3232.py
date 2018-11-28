/*/**/

#include <bits/stdc++.h>

using namespace std;

set < int > s;

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; tt++) {
		int num;
		cin >> num;
		int foo = 0;
		s.clear();
		if(not num) {
			cout << "Case #" << tt << ": INSOMNIA" << endl;
			continue;
		}
		while(s.size() != 10) {
			foo += num;
			int bar = foo;
			while(bar) {
				s.insert(bar % 10);
				bar /= 10;
			}
		}
		cout << "Case #" << tt << ": " << foo << endl;
	}
	return 0;
}

