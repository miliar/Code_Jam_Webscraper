#include <iostream>
#include <deque>

using namespace std;


int main() {

	int T;
	cin >> T;
	
	for (int t = 1; t <= T; t++) {
		string s;
		deque<char> d;
		cin >> s;
		for (int i = 0; i < s.size(); i++) {
			if (d.empty()) {
				d.push_back(s[i]);
				continue;
			}
			if (d.front() > s[i]) {
				d.push_back(s[i]);
			}else d.push_front(s[i]);
		}
		cout << "Case #" << t << ": ";
		while (!d.empty()) {
			cout << d.front();
			d.pop_front();
		}
		cout << endl;
	}

}
