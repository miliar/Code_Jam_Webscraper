#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <ctime>

#pragma warning (disable:4996)

using namespace std;

typedef long long ll;

bool popcnt(ll a) {
	int s = 0;
	int s28 = 0;
	int s6 = 0;
	int i = 0;
	while (a) {
		if (a & 1) {
			s++;
			if (i & 1) {
				s28 += 2;
				s6 += 6;
			}
			else {
				s28++;
				s6++;
			}
		}
		i++;
		a >>= 1;
	}
	if (s != 6 && s != 12) return false;  // 3,4,5,7,8,9
	if (s28 % 3) return false;
	if (s6 % 7) return false;
	return true;
}

int main() {
	//freopen("C-large.in", "r", stdin);
	freopen("c-l.out", "w", stdout);
	cout << "Case #1:\n";
	int n = 32, j = 500;
	ll m = (1LL << (n - 1)) + 1;
	while (j && m < (1LL << n)) {
		if (popcnt(m)) {
			j--;
			char b[70];
			itoa(m, b, 2);
			cout << b << " 3 2 3 2 7 2 3 2 3\n";
		}
		m += 2;
	}
	return 0;
}

//long long mypow(ll a, ll b) {
//	if (b == 0) return 1;
//	return a * mypow(a, b - 1);
//}
//
//int main() {
//	freopen("D-large.in", "r", stdin);
//	freopen("d-l.out", "w", stdout);
//	int t, cas = 1;
//	cin >> t;
//	while (t--) {
//		ll k, c, s;
//		cin >> k >> c >> s;
//		cout << "Case #" << cas++ << ":" ;
//		if (s * c < k) cout << " IMPOSSIBLE\n";
//		else {
//			ll p = mypow(k, c - 1);
//			for (int i = 0; i < k; i += c) {
//				ll pp = p;
//				ll ans = 1;
//				for (int j = 0; j < min(k, c); j++) {
//					ans += pp * (i + j);
//					pp /= k;
//				}
//				cout << ' ' << min(ans, p * k);
//			}
//			cout << endl;
//		}
//	}
//	return 0;
//}

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
