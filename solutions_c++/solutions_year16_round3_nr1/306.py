#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void solve() {
	int n;
	cin >> n;
	vector<int> a(n);
	for (int i = 0; i < n; ++i) cin >> a[i];
	
	int id = max_element(a.begin(), a.end()) - a.begin();
	int s = 0;
	for (int i = 0; i < a.size(); ++i)
		s += a[i];
	static int test_id;
	++test_id;
	cout << "Case #" << test_id << ":";
	
	for (int i = 0; i < a.size(); ++i) {
		if (i == id) continue;
		while (s > a[id] * 2 && a[i] > 0) {
			cout << " " << char('A' + i);
			--s; --a[i];
		}
	}
	
	for (int i = 0; i < a.size(); ++i) {
		if (i == id) continue;
		while (a[i] > 0) {
			cout << " " << char('A' + i) << char('A' + id);
			--a[i];
		}
	}
	
	cout << endl;
}

int main() {
	int t;
	cin >> t;
	while (t-->0)
		solve();
	return 0;
}