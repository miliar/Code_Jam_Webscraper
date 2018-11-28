#include <iostream>
#include <set>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int ct = 1; ct <= T; ct++) {
		set<int> s;
		int n;
		cin >> n;

		for (int i = 0; i < n * (2 * n - 1); i++) {
			int x;
			cin >> x;
			set<int>::iterator it = s.find(x);
			if (it == s.end()) {
				s.insert(x);
			} else {
				s.erase(x);
			}
		}

		cout << "Case #" << ct << ":";
		set<int>::iterator it = s.begin();
		while (it != s.end()) {
			cout << " " << *it;
			it++;
		}
		cout << endl;
	}

	return 0;
}