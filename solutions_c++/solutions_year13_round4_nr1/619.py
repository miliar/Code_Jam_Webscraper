#include <iostream>
#include <string>
#include <map> 
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>


using namespace std;

#define ll long long
#pragma comment(linker, "/STACK:64000000")

const int maxn = 1 << 17;
const int inf = 1000000007;
const int mod = 1000002013;

int n, m;
int o[maxn], e[maxn], p[maxn];
int op[maxn], ep[maxn], pp[maxn];

void reading() {
	cin >> n >> m;
	for (int i = 0; i < m; i++)
		cin >> o[i] >> e[i] >> p[i], op[i] = o[i], ep[i] = e[i], pp[i] = p[i];
}

int f(int x) {
	ll res = 1LL * n * x % mod + x - 1LL * x * (x + 1) / 2 % mod;
	return res % mod;
}

int solve() {
	vector<pair<int, pair<int, int> > > v;
	for (int i = 0; i < m; i++) {
		v.push_back(make_pair(o[i], make_pair(0, i)));
		v.push_back(make_pair(e[i], make_pair(1, i)));
	}

	vector<pair<int, pair<int, int> > > v2;
	multiset<pair<int, pair<int, int> > > st;
	st.insert(make_pair(2e9, make_pair(-1, -1)));
	sort(v.begin(), v.end());
	for (int i = 0; i < v.size(); i++) {
		if (v[i].second.first == 0) {
			while (p[v[i].second.second]) {
				pair<int, pair<int, int> > o = *st.begin();
				if (o.first >= e[v[i].second.second]) break;
				st.erase(st.begin());
				int u = v[i].second.second;
				int k = min(o.second.second, p[u]);
				p[u] -= k;
				if (o.second.second > k) {
					st.insert(make_pair(o.first, make_pair(o.second.first, o.second.second - k)));
				}
				st.insert(make_pair(e[u], make_pair(o.second.first, k)));
				st.insert(make_pair(o.first, make_pair(v[i].first, k)));
			}
			if (p[v[i].second.second])
				st.insert(make_pair(e[v[i].second.second], make_pair(v[i].first, p[v[i].second.second])));
		} else {
			while (!st.empty() && st.begin()->first == v[i].first) {
				pair<int, pair<int, int> > o = *st.begin();
				st.erase(st.begin());
				v2.push_back(o);
			}
		}
	}

	while (1) {
		bool f = 0;
		for (int i = 0; i < v2.size(); i++) if (v2[i].second.second > 0) {
			for (int j = 0; j < v2.size(); j++) if (v2[j].second.second > 0) {
				if (v2[i].second.first < v2[j].second.first && v2[j].second.first <= v2[i].first && v2[i].first < v2[j].first) {
					int k = min(v2[i].second.second, v2[j].second.second);
					if (!k) continue;
					v2[i].second.second -= k;
					v2[j].second.second -= k;
					v2.push_back(make_pair(v2[i].first, make_pair(v2[j].second.first, k)));
					v2.push_back(make_pair(v2[j].first, make_pair(v2[i].second.first, k)));
				}
			}
		}
		if (!f) break;
	}

	int MOD = 1000002013, ans = 0;
	for (int i = 0; i < m; i++) {
		ans = (ans + 1LL * f(ep[i] - op[i]) * pp[i] % MOD) % MOD;
	}
	for (int i = 0; i < v2.size(); i++) 
		ans = ((ll)ans - 1LL * f(v2[i].first - v2[i].second.first) * v2[i].second.second % MOD + MOD) % MOD;
	return ans;
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
    int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		reading();
		cout << solve() << endl;
	}

	return 0;
}