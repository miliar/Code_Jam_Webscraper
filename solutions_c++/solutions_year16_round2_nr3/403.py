#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 1e6;
#define MP make_pair
#define lli long long int
#define y1 y123123


int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		int n;
		cin >> n;
		vector<pair<string, string> > v(n);
		for (int i = 0; i < n; ++i) cin >> v[i].first >> v[i].second;
		int bound = (1 << n);
		int ans = 0;
		for (int mask = 0; mask < bound; ++mask) {
			int cnt = 0;
			set<string> s1, s2;
			for (int i = 0; i < n; ++i) {
				if ((1 << i) & mask) {
					s1.insert(v[i].first); s2.insert(v[i].second);
				}
				else {
					++cnt;
				}
			}
			bool ok = 1;
			for (int i = 0; i < n && ok; ++i) {
				if ((1 << i) & mask) {}
				else {
					ok &= s1.find(v[i].first) != s1.end();
					ok &= s2.find(v[i].second) != s2.end();
				}
			}
			if (ok) ans = max(ans, cnt);
		}
		cout << ans;

		cout << endl;
	}
}

