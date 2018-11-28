#include <iostream>

using namespace std;

int test() {
	int m;
	int c, d;
	char ch;
	cin >> m;

	int standing = 0;
	int ans = 0;

	cin >> ch;
	standing = ch - '0';
	for(int i = 1; i <= m; i++) {
		cin >> ch;
		d = ch - '0';
		if(d && i > standing) {
			ans += i - standing;
			standing += i - standing;
		}
		standing += d;
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
		cout << "Case #" << i << ": " << test() << "\n";
	return 0;
}