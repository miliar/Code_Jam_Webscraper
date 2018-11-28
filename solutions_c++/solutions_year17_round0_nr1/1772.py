#include <algorithm>
#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

void sol() {
	string s; int k;
	cin >> s >> k;
	int n = s.size();
	int cnt = 0;
	for (int i = 0; i < n + 1 - k; i++) {
		if (s[i] == '-') {
			for (int j = 0; j < k; j++) {
				if (s[i + j] == '-') {
					s[i + j] = '+';
				} else {
					s[i + j] = '-';
				}
			}
			cnt++;
		}
	}
	if (count(s.begin(), s.end(), '+') == n) {
		cout << cnt << endl;
	} else {
		cout << "IMPOSSIBLE\n";
	}
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		printf("Case #%d: ", i + 1);
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}