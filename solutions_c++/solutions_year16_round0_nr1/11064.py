#include <iostream>
#include <string>
using namespace std;

bool t(bool a[10]) {
	for (int i = 0; i < 10; i++) {
		if (!a[i]) {
			return false;
		}
	}
	return true;
}

int main() {
	bool counted[10];
	int cases;
	cin >> cases;
	long long n, m;
	string M;
	long long k;
	long long c;
	for (int i = 0; i < cases; i++) {
		cin >> n;
		if (n == 0) {
			cout <<"Case #" << i+1 << ": INSOMNIA\n";
		} else {
			for (int i = 0; i < 10; i++) {
				counted[i] = false;
			}
			c = 0;
			while (!t(counted)) {
				c++;
				m = n*c;
				M = to_string(m);
				for (int j = 0; j < M.length(); j++) {
					k = M.at(j) - 48;
					counted[k] = true;
				}
			}
			cout << "Case #" << i + 1 << ": "<<m<<"\n";
		}
	}
}