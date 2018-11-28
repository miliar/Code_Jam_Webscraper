#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;

bool check(vvi& a) {
	if (a.size() == 0) return true;
	if (a[0].size() == 0) return true;

	int mn = a[0][0];
	for (size_t i = 0; i < a.size(); ++i)
		for (size_t j = 0; j < a[i].size(); ++j)
			mn = min(a[i][j], mn);

	for (size_t i = 0; i < a.size(); ++i)
		if (count(a[i].begin(), a[i].end(), mn) == a[i].size()) {
			a.erase(a.begin() + i);
			return check(a);
		}

	for (size_t j = 0; j < a[0].size(); ++j) {
		int cnt = 0;
		for (size_t i = 0; i < a.size(); ++i) cnt += a[i][j] == mn;
		if (cnt == a.size()) {
			for (size_t i = 0; i < a.size(); ++i)
				a[i].erase(a[i].begin() + j);
			return check(a);
		}
	}
	return false;
}

void solve() {
	int n, m;
	cin >> n >> m;

	vvi a(n, vi(m));
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < m; ++j)
			cin >> a[i][j];
	
	static int testid = 0;
	cout << "Case #" << ++testid << ": ";
	cout << (check(a) ? "YES" : "NO") << endl; 
}

int main() {
	int t;
	cin >> t;
	while (t--) solve();
	return 0;
}
