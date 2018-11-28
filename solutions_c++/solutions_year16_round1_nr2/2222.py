#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <ctime>
#include <cassert>
#include <climits>
#include <memory.h>
#include <bitset>

using namespace std;

int t, n, x, a[101][101], b[101], c[101];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> t;
	for (int ii = 0; ii < t; ii++) {
		cin >> n;
		for (int i = 0; i < 2 * n - 1; i++)
			b[i] = c[i] = 0;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				a[i][j] = -1;
		}
		vector<vector<int> > v(2 * n - 1);
		multiset<vector<int> > s;
		for (int i = 0; i < 2 * n - 1; i++) {
			for (int j = 0; j < n; j++) {
				cin >> x;
				v[i].push_back(x);
			}
			s.insert(v[i]);
		}
		int pos = 0;
		int zn = 0;
		vector<pair<int, int> > v1;
		for (int i = 0; i < n; i++) {
			int mi = 1000000007;
			int n1 = -1, n2 = -1;
			for (int j = 0; j < v.size(); j++) {
				if (!b[j] && v[j][i] < mi) {
					mi = v[j][i];
					n1 = j;
					n2 = -1;
				}
				else if (!b[j] && v[j][i] == mi) {
					n2 = j;
				}
			}
			if (n2 == -1) {
				pos = i;
				zn = mi;
				b[n1] = 1;
				for (int j = 0; j < n; j++) {
					c[j] = v[n1][j];
				}
			}
			else {
				v1.push_back(make_pair(n1, n2));
				b[n1] = 1;
				b[n2] = 1;
			}
		}
		vector<int> ans;
		int cc = 0;
		for (int i = 0; i < n; i++) {
			if (i == pos) {
				ans.push_back(zn);
				cc = -1;
				continue;
			}
			if (c[i] == v[v1[i + cc].first][pos]) {
				ans.push_back(v[v1[i + cc].second][pos]);
			}
			else {
				ans.push_back(v[v1[i + cc].first][pos]);
			}
		}
		cout << "Case #" << ii + 1 << ": ";
		for (int i = 0; i < ans.size(); i++)
			cout << ans[i] << ' ';
		cout << endl;
	}

	return 0;
}