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
		int k, c, s;
		cin >> k >> c >> s;

		if ((c == 1 && s < k) || s < (k + 1) / 2) {
			cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		vector<long long> ret;
		if (c == 1) {
			for (int i = 0; i < k; i++) {
				ret.push_back(i + 1);
			}
		} else {
			for (int i = 0; i < k; i += 2) {
				long long last = k;
				long long pos  = i + 1;
				for (int j = 0; j < c - 1; j++) {
					pos = last * i + pos;
					last *= k;
				}
				if (i < k - 1) {
					pos++;
				}
				ret.push_back(pos);
			}
		}

		cout << "Case #" << t << ": ";
		for (int i = 0, len = ret.size(); i < len; i++) {
			cout << ret[i];
			if (i < len - 1) {
				cout << " ";
			}
		}
		cout << endl;
	}
}

