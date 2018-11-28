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
		int n;
		vector<int> p;
		cin >> n;
		for (int i = 0; i < n; i++) {
			int tmp;
			cin >> tmp;
			p.push_back(tmp);
		}
		vector<char> ret;
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += p[i];
		}

		while (sum > 0) {
			int max = 0;
			int idx = -1;
			for (int i = 0; i < n; i++) {
				if (max < p[i]) {
					max = p[i];
					idx = i;
				}
			}
			ret.push_back(char('A' + idx));
			p[idx]--;
			sum--;
		}

		/* solution */

		int len = ret.size();
		cout << "Case #" << t << ": ";
		for (int i = 0; i < len; i++) {
			cout << ret[i];
			if (i == len - 3 || (i < len - 2 && i % 2)) {
				cout << " ";
			}
		}
		cout << endl;
	}
}

