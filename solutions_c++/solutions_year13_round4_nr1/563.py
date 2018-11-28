#include <iostream>
#include <algorithm>
using namespace std;

const int MOD = 1000002013;
const int N = 1000 + 10;

int n, m;
pair<int, int> st[N], ed[N];

int f(int x) {
	if (x == 0) {return 0;}
	return (x - 1) * x >> 1;
}

int main() {
	int T, cas = 0;
	for (cin >> T; T; --T) {
		long long origin = 0, most = 0;
		cin >> n >> m;
		for (int i = 0; i < m; ++i) {
			cin >> st[i].first >> ed[i].first >> st[i].second;
			ed[i].second = st[i].second;
			origin = (origin + static_cast<long long>(f(ed[i].first - st[i].first)) * st[i].second) % MOD;
		}
		sort(st, st + m);
		sort(ed, ed + m);
		for (int i = m - 1; i >= 0; --i) {
			for (int j = 0; j < m && st[i].second; ++j) if (ed[j].first >= st[i].first) {
				long long p = min(st[i].second, ed[j].second);
				most = (most + f(ed[j].first - st[i].first) * p) % MOD;
				ed[j].second -= p;
				st[i].second -= p;
			}
		}
		cout << "Case #" << ++cas << ": " << (most - origin + MOD) % MOD << endl;
	}
	return 0;
}
