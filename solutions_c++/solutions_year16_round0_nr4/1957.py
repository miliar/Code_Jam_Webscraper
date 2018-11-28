#include <iostream>

using namespace std;

typedef long long ll;

int main() {
	int nt; cin >> nt;
	for (int ct = 1; ct <= nt; ct++) {
		ll k, c, s;
		cin >> k >> c >> s;

		cout << "Case #" << ct << ":";
		bool hasAns = true;
		ll ans = 0;
		if (c == 1) {
			if (s < k) {
				hasAns = false;
			} else {
				for (int i = 0; i < k; i++) {
					cout << " " << i+1;
				}
				cout << endl;
			}
		} else {
			if (s < k) {
				hasAns = false;
			} else {
				ll blah = 1;
				for (int i = 0; i < c-1; i++) {
					blah *= k;
				}
				for (int i = 0; i < k; i++) {
					cout << " " << (blah * i) + 1;
				}
				cout << endl;
			}
		}

		if (!hasAns) {
			cout << " IMPOSSIBLE" << endl;
		}
	}
}
