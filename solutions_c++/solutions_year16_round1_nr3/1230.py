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

int ok(vector<int> b, int i, int j) {
	return b[i] == j;
}
int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		int n;
		vector<int> b;
		cin >> n;
		for (int i = 0; i < n; i++) {
			int tmp;
			cin >> tmp;
			b.push_back(tmp - 1);
		}
		int ret = 0;
		int maxbits = 1 << n;
		vector< vector<int> > elms;
		for (int i = 0; i < maxbits; i++) {
			int bits = i;
			vector<int> tmp;
			for (int j = 0; j < n && bits > 0; j++) {
				if (bits % 2) {
					tmp.push_back(j);
				}
				bits /= 2;
			}
			elms.push_back(tmp);
		}
		for (int i = 0; i < maxbits; i++) {
			for (int j = i + 1; j < maxbits; j++) {
				if (elms[i].size() < elms[j].size()) {
					vector<int> work = elms[i];
					elms[i] = elms[j];
					elms[j] = work;
				}
			}
		}
		bool found = false;
		for (int i = 0; i < maxbits && !found; i++) {
			vector<int> tmp = elms[i];
			int len = tmp.size();
			do {
				bool ng = false;
				for (int j = 0; j < len; j++) {
					if (ok(b, tmp[j], tmp[(j + 1) % len]) || 
						ok(b, tmp[j], tmp[(j - 1 + len) % len])) {
					} else {
						ng = true;
						break;
					}
				}
				if (!ng) {
					//for (int k = 0; k < len; k++) {
					//	cout << tmp[k] << ", ";
					//}
					//cout << endl;
					ret = max(ret, len);
					found = true;
				}
			} while (next_permutation(tmp.begin(), tmp.end()) && !found);
		}

		/* solution */

		cout << "Case #" << t << ": " << ret << endl;
	}
}

