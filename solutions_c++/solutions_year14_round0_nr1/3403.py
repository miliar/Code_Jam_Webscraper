#include <iostream>
#include <set>

using namespace std;

int main() {
	int T, la, m, n, p, q;
	cin >> T;
	for (int i = 1; i <= T; ++i) {
		cin >> la;
		set<int> saved;
		for (int j=1; j<=4; j++) {
			cin >> m >> n >> p >> q;
			if (j == la) {
				saved.insert(m);
				saved.insert(n);
				saved.insert(p);
				saved.insert(q);
			}
		}
		cin >> la;
		int len = 0, v;
		for (int j=1; j<=4; j++) {
			cin >> m >> n >> p >> q;
			if (j == la) {
				if (saved.find(m) != saved.end()) {
					len++;
					v = m;
				}
				if (saved.find(n) != saved.end()) {
					len++;
					v = n;
				}
				if (saved.find(p) != saved.end()) {
					len++;
					v = p;
				}
				if (saved.find(q) != saved.end()) {
					len++;
					v = q;
				}
			}
		}

		if (len == 1)
			cout << "Case #" << i << ": " << v << '\n';
		else if (len == 0)
			cout << "Case #" << i << ": Volunteer cheated!\n";
		else
			cout << "Case #" << i << ": Bad magician!\n";
	}

	return 0;
}