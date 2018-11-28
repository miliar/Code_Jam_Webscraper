#include <iostream>
#include <set>
#include <cstdio>

using namespace std;

int f(int n) {
	set<char> s = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};

	for (int i = 1; i * n <= 1000000000; ++i) {
		// cerr << "i=" << i << endl;
		char t[10];
		sprintf(t, "%d", i*n);
		for (char* p = t; *p != '\0'; ++p) s.erase(*p);

		if (s.empty()) return (i * n);
	}

	return -1;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		cin >> n;

		if (n == 0) cout << "Case #" << i << ": INSOMNIA" << endl;
		else cout << "Case #" << i << ": " << f(n) << endl;
	}

	return 0;
}
