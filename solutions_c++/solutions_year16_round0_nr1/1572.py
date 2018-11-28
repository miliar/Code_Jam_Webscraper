#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

#pragma warning (disable:4996)

using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-ll.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	for (; cas <= t; cas++) {
		long long n, m;
		cin >> n;
		m = n;
		set<long long> a, st;
		while (a.size() < 10) {
			if (st.count(n)) break;
			st.insert(n);
			long long nn = n;
			while (nn) {
				a.insert(nn % 10);
				nn /= 10;
			}
			n += m;
		}
		cout << "Case #" << cas << ": ";
		if (a.size() == 10) cout << n - m << endl;
		else cout << "INSOMNIA\n";
	}
	return 0;
}
