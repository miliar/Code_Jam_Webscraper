#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

#pragma warning (disable:4996)

using namespace std;

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int t, cas = 1;
	cin >> t;
	while (t--) {
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << cas++ << ":" ;
		for (int i = 0; i < k; i++)
			cout << ' ' << i + 1;
		cout << endl;
	}
	return 0;
}

//int main() {
//	freopen("B-large.in", "r", stdin);
//	freopen("b-l.out", "w", stdout);
//	int t, cas = 1;
//	cin >> t;
//	while (t--) {
//		string s;
//		cin >> s;
//		int ans = 0;
//		int n = (int)s.length();
//		for (int i = 1; i < n; i++) {
//			if (s[i] != s[i - 1]) ans++;
//		}
//		if (s[n - 1] == '-') ans++;
//		cout << "Case #" << cas++ << ": " << ans << endl;
//	}
//	return 0;
//}

//int main() {
//	freopen("A-large.in", "r", stdin);
//	freopen("a-ll.out", "w", stdout);
//	int t, cas = 1;
//	cin >> t;
//	for (; cas <= t; cas++) {
//		long long n, m;
//		cin >> n;
//		m = n;
//		set<long long> a, st;
//		while (a.size() < 10) {
//			if (st.count(n)) break;
//			st.insert(n);
//			long long nn = n;
//			while (nn) {
//				a.insert(nn % 10);
//				nn /= 10;
//			}
//			n += m;
//		}
//		cout << "Case #" << cas << ": ";
//		if (a.size() == 10) cout << n - m << endl;
//		else cout << "INSOMNIA\n";
//	}
//	return 0;
//}
