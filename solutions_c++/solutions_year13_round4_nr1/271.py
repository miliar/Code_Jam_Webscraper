#include <cstdio>
#include <algorithm>
#include <iostream>
#include <stack>
using namespace std;

#define mp(a,b) make_pair(a, b)

struct Event {
	int q, t;
	bool fin;
	bool operator<(const Event &second) const {
		if (t != second.t) {
			return t < second.t;
		} else {
			return fin < second.fin;
		}
	}
} arr[2005];

long long n, m;
const int kMod = 1000002013;

long long GetCost(long long s, long long f) {
	return (n * (f - s) - (f - s) * (f - s + 1) / 2) % kMod;
}

long long Solve() {
	cin >> n >> m;
	stack<pair<int, int> > S;
	int q = 0;
	long long desired = 0, real = 0;
	for (int i = 0; i < m; ++i) {
		long long o, e, p;
		cin >> o >> e >> p;
		arr[q].t = o;
		arr[q].fin = false;
		arr[q].q = p;
		++q;

		arr[q].t = e;
		arr[q].fin = true;
		arr[q].q = p;
		++q;
	
		desired = (desired + GetCost(o, e) * p) % kMod;
	}
	sort(arr, arr + q);
	for (int i = 0; i < q; ++i) {
		if (!arr[i].fin) {
			S.push(mp(arr[i].t, arr[i].q));
		} else {
			int left = arr[i].q;
			while (left > 0) {
				pair<int, int> last = S.top();
				S.pop();
				int can = min(left, last.second);
				real = (real + can * GetCost(last.first, arr[i].t)) % kMod;
				last.second -= can;
				left -= can;
				if (last.second > 0) {
					S.push(last);
				}
			}
		}
	}
	desired -= real;
	if (desired < 0) {
		desired += kMod;
	}
	cout << desired << endl;
}

int main() {
	freopen("a_large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; ++I) {
		printf("Case #%d: ", I + 1);
		Solve();
	}
	return 0;
}