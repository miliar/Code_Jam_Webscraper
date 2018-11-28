#include<iostream>
using namespace std;

int upper(int a, int b) {
	int ans = a / b;
	if (ans * b == a) return ans;
	return ans + 1;
}

int main() {
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t, it, c, r, w, ans;
	cin >> t;
	for (it = 1; it <= t; it++) {
		cin >> r >> c >> w;
		cout << "Case #" << it << ": " << upper(c, w) * r + w - 1 << "\n";
	}
	return 0;
}