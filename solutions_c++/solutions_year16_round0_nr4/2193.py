#define _CRT_SECURE_NO_WARNINGS

#include <iostream>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, c, k, s; 
	cin >> t;
	for (int g = 1; g <= t; ++g) {
		cin >> k >> c >> s;
		cout << "Case #" << g << ": ";
		if (s < k) {
			cout << "IMPOSSIBLE\n";
			continue;
		}
		else {
			for (int i = 1; i <= s; ++i)
				cout << i << ' ';
			cout << '\n';
		}
	}
	return 0;
}