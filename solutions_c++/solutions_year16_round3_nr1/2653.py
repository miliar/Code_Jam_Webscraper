#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cmath>
#include <climits>
#include <numeric>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <sstream>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, T;
	cin >> t;
	T = t;
	while (t--) {
		cin >> n;
		vector<int> p(n);
		for (int i = 0; i < n; i++)
			cin >> p[i];
		int sum = accumulate(p.begin(), p.end(), 0);
		string ss = "";
		while (sum) {
			int max = 0;
			for (int i = 0; i < n; i++) {
				if (p[max] < p[i]) max = i;
			}
			ss.push_back('A' + max);
			p[max]--;
			if (--sum == 0) break;
			max = 0;
			for (int i = 0; i < n; i++) {
				if (p[max] < p[i]) max = i;
			}
			if (sum == 2) {
				ss.push_back(' ');
				continue;
			}
			ss.push_back('A' + max);
			p[max]--;
			sum--;
			ss.push_back(' ');
		}
		cout << "Case #" << T - t << ": ";
		cout << ss << endl;
	}
	return 0;
}