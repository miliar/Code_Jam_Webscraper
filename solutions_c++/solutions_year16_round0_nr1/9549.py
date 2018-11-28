#include <iostream>
#include <stdio.h>
#include <map>
using namespace std;

map<int, int> m;

bool test() {
	for (int i = 0; i < 10; i++) {
		if (!m[i])
			return 0;
	}
	return 1;
}
bool addTomap(long int a) {
	while (a > 0) {
		m[a % 10]++;
		a /= 10;
	}
	return test();
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	long int n;
	long int c = 1;
	int z = t;
	while (t--) {
		m.clear();
		cin >> n;
		c = n;
		if (c == 0) {
			cout << "Case #" << z - t  << ": INSOMNIA" << endl;
			continue;
		}
		for (int i = 1;; i++) {
			if (addTomap(c * i)) {
				cout << "Case #" << z - t  << ": " << c * i << endl;
				break;
			}
		}

	}
	return 0;
}
