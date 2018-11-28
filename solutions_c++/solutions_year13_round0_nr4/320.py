#include <iostream>
#include <vector>
#include <map>

using namespace std;

typedef vector<int> vi;

struct room {
	int need;
	vi have;
};

void add(map<int, int>& m, vi& k) {
	for (size_t i = 0; i < k.size(); ++i)
		++m[k[i]];
}

void sub(map<int, int>& m, int k) {
	--m[k];
}

void solve() {
	int n, k;
	cin >> k >> n;
	vi start(k);
	for (int i = 0; i < k; ++i)
		cin >> start[i];

	vector<room> r(n);
	for (int i = 0; i < n; ++i) {
		cin >> r[i].need;
		int s;
		cin >> s;
		r[i].have.resize(s);
		for (int j = 0; j < s; ++j)
			cin >> r[i].have[j];
	}

	vi w(1<<n);
	w[0] = true;
	for (size_t m = 1; m < w.size(); ++m) {
		map<int, int> keys;
		add(keys, start);
		for (int i = 0; i < n; ++i) {
			if (m & (1<<i)) {
				// nothing
			} else {
				add(keys, r[i].have);
				sub(keys, r[i].need);
			}
		}

		for (int i = 0; i < n; ++i) if (m & (1<<i)) {
			if (keys[r[i].need] && w[m ^ (1<<i)])
				w[m] = true;
		}
	}


	static int testid = 0;
	cout << "Case #" << ++testid << ":";
	if (w[(1<<n)-1] == false)
		cout << " IMPOSSIBLE" << endl;
	else {
		int M = (1<<n)-1;
		map<int, int> keys;
		add(keys, start);
		while (M) {
			for (int i = 0; i < n; ++i) if (M & (1<<i))
				if (keys[r[i].need] && w[M - (1<<i)]) {
					cout << ' ' << i + 1;
					M -= 1 << i;
					sub(keys, r[i].need);
					add(keys, r[i].have);
					break;
				}
		}
		cout << endl;
	}
}

int main() {
	int t;
	cin >> t;
	while (t--) solve();
	return 0;
}
