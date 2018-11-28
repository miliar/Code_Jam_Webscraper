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

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string s;
		cin >> s;
		int n = s.size();
		bool isHappy[n];
		for (int i = 0; i < n; i++) {
			isHappy[i] = s[i] == '+';
		}
		int ret = 0;
		bool ended = false;
		for (int i = 0; i < n; i++) {
			for (int j = 1; j < n; j++) {
				if (isHappy[j] != isHappy[j - 1]) {
					ret++;
					for (int k = 0; k < j; k++) {
						isHappy[k] = !isHappy[k];
					}
					break;
				}
				if (j == n - 1) {
					ended = true;
				}
			}
			if (ended) {
				break;
			}
		}
		if (!isHappy[n - 1]) {
			ret++;
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
}

