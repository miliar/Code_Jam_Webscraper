#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;
typedef long long ll;

//int solve() {
//	int D;
//	cin >> D;
//	ll ar[1001] = {};
//	for (int i = 0; i < D; ++i) {
//		int c;
//		cin >> c;
//
//		ar[c]++;
//	}
//
//
//
//}

struct State {
	State(int t) : time(t) {
		fill(ar, ar + 10, 0);
	}

	bool operator < (const State& st) const {
		return time < st.time;
	}

	bool isDone() const {
		for (int i = 1; i < 10; ++i) if (ar[i]) return false;

		return true;
	}

	void skip() {
		++time;

		for (int i = 1; i < 10; ++i) {
			ar[i - 1] = ar[i];
			ar[i] = 0;
		}
	}

	void split(int i, int d) {
		int i1 = d;
		int i2 = i - d;

		time += ar[i];
		ar[i1] += ar[i];
		ar[i2] += ar[i];
		ar[i] = 0;
	}

	int time;
	int ar[10];
};

int solve() {
	multiset<State> q;
	int n; cin >> n;

	int mx = 0;

	State start(0);
	for (int i = 0; i < n; ++i) {
		int x; cin >> x;
		mx = max(mx, x);

		++start.ar[x];
	}

	q.insert(start);

	while (true) {
		State st = *q.begin();
		q.erase(q.begin());

		if (st.isDone()) {
			return min(mx, st.time);
		}

		// do nothing
		State st0 = st;
		st0.skip();
		q.insert(st0);

		for (int i = 4; i < 10; ++i) {
			if (st.ar[i]) {
				for (int j = 1, h = i / 2; j <= h; ++j) {
					State st1 = st;
					st1.split(i, j);

					q.insert(st1);
				}
			}
		}
	}
}

int main() {
	int T; cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		cerr << tc << endl;
		cout << "Case #" << tc << ": " << solve() << endl;
	}
}