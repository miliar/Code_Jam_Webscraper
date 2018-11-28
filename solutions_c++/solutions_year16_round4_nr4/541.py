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

const int N = 5e5 + 200;
const int SL = 2500;
#define MP make_pair
#define lli long long int
#define y1 y123123

int a[4][4];
int n;
int sn;

int bc(int v) {
	int ans = 0;
	while (v) {
		ans += v & 1;
		v >>= 1;
	}
	return ans;
}

vector<pair<int, int> >  gen(int start) {
	int b = (1 << sn);
	vector<pair<int, int> > result;
	for (int mask = start; mask < b; ++mask) {
		if ((mask & start) == start) {
			bool ok = 1;
			for (int i = 0; i < n && ok; ++i) {
				int cnt = 0;
				for (int j = 0; j < n; ++j) {
					cnt += ((1 << (i*n + j)) & mask) > 0;
				}
				ok &= cnt > 0;
			}
			if (ok) result.push_back(MP(bc(mask), mask));
		}
	}
	sort(result.begin(), result.end());
	return result;
}

vector<int> v;
bool used[10];

bool dfs(int i) {
	if (i == n) return true;
	int men = v[i];
	int cnt = 0;
	for (int to = 0; to < n; ++to) {
		if (!used[to] && a[men][to]) {
			used[to] = 1;
			cnt++;
			if (!dfs(i + 1)) {
				used[to] = 0;
				return false;
			}
			used[to] = 0;
		}
	}
	return cnt > 0;
}

bool check(int mask) {
	for (int i = 0; i < n; ++i) v[i] = i;
	for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) a[i][j] = (mask & (1 << (i*n + j))) > 0;
	do {
		if (!dfs(0)) return false;
	} while (next_permutation(v.begin(), v.end()));
	return true;
}

int main() {
	ios_base::sync_with_stdio(0);

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	cin >> T;
	for (int qq = 0; qq < T; ++qq) {
		cout << "Case #" << (qq + 1) << ": ";

		cin >> n;
		sn = n*n;
		int start = 0;
		for (int i = 0; i < sn; ++i) {
			char c;
			cin >> c;
			if (c == '1') start |= (1 << i);
		}
		vector<pair<int, int> > all = gen(start);
		v.resize(n);		
		for (int i = 0; i < all.size(); ++i) {
			if (check(all[i].second)) {
				cout << all[i].first - bc(start);
				break;
			}
		}


		cout << endl;
	}
}