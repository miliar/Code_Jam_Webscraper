#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

bool isValid(string s) {
	int n = s.size();
	for (int i = 0; i < n; i++) {
		if (s[i] == '-') {
			return false;
		}
	}
	return true;
}

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		int k;
		cin >> s >> k;

		int ret = 0;
		int n = s.size();
		for (int i = 0; i <= n - k; i++) {
			if (s[i] == '-') {
				for (int j = 0; j < k; j++) {
					if (s[i + j] == '-') {
						s[i + j] = '+';
					} else {
						s[i + j] = '-';
					}
				}
				ret++;
			}
		}

		if (isValid(s)) {
			cout << "Case #" << t << ": " << ret << endl;
		} else {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
		}
	}
}

