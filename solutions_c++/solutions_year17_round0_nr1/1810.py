#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		string s;
		int k;
		cin >> s;
		cin >> k;
		bool flag = true;
		int sum = 0;
		for (int i = 0; i < (int)s.size(); i++) {
			if (s[i] == '-' && (int)s.size() - i >= k) {
				sum++;
				for (int j = i; j < i + k; j++) {
					if (s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
			}
			if (s[i] == '-')
				flag = false;
		}
		cout << "Case #" << q + 1 << ": ";
		if (flag)
			cout << sum << '\n';
		else
			cout << "IMPOSSIBLE\n";
	}

	return 0;
}