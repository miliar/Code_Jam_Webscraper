#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> pii;

#define dbg(x) cerr __LINE__ << ": " << #x << " = " << x << endl;

void solve(int test) {
	int n; cin >> n;
	vector<pii> p;
	for (int i = 0; i < n; i++) {
		int x; cin >> x;
		p.push_back(pii(x, i));
	}

	cout << "Case #" << test << ": ";
	while (true) {
		sort(p.begin(), p.end());
		if (p[n-1].first == 0) break;
		
		int sum = 0;
		for (int i = 0; i < n; i++) {
			sum += p[i].first;
		}
		for (int i = 0; i < n; i++) {
			if (p[i].first > sum - p[i].first)
				cerr << "testcase " << test << endl;
		}
		
		if (p[n-1].first == 1) {
			int k = 0;
			for (int i = 0; i < n; i++)
				k += p[i].first > 0;
			if (k & 1) {
				p[n-1].first--;
				cout << char('A' + p[n-1].second) << " ";
			} else {
				p[n-1].first--;
				p[n-2].first--;
				cout << char('A' + p[n-1].second) << char('A' + p[n-2].second) << " ";
			}
		} else {
			cout << char('A' + p[n-1].second);
			if (p[n-1].first == p[n-2].first) {
				p[n-2].first--;
				cout << char('A' + p[n-2].second);
			}
			p[n-1].first--;
			cout << " ";
		}
	}
	cout << endl;
}

int main() {
	freopen("in2.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
	return 0;
}
