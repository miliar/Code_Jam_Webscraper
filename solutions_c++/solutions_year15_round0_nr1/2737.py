#include <iostream>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <unordered_set>


using namespace std;


int t;


int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	cin >> t;
	for (int k = 0; k < t; k++) {
		int n;
		cin >> n;
		vector<int> c;
		c.resize(n + 1);
		string s;
		cin >> s;
		for (int i = 0; i <= n; i++) {
			c[i] = s[i] - '0';
		}
		int l = 0;
		int r = 1000000000;
		while (l != r) {
			int m = (l + r) / 2;
			int sum = c[0] + m;
			bool b = true;
			for (int j = 1; j <= n; j++) {
				if (j <= sum) {
					sum += c[j];
				} else {
					b = false;
				}
			}
			if (b) {
				r = m;
			} else {
				l = m + 1;
			}
		}
		cout << "Case #" << k + 1 << ':' << ' '<< l << endl;
	}
    return 0;
}
