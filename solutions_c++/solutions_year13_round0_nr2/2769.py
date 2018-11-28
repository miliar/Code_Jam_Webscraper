#include <cstdio>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define rep(i, n) for (int i = 0, _##i = (n); i < _##i; ++i)
#define dwn(i, n) for (int i = (n); --i >= 0;)
#define repr(i, l, r) for (int i = (l), _##i = (r); i < _##i; ++i)
#define dwnr(i, l, r) for (int i = (r), _##i = (l); --i >= _##i;)
#define repi(i, a) for (__typeof((a).begin()) i = (a).begin(), _##i=(a).end(); i != _##i; ++i)
#define dwni(i, a) for (__typeof((a).rbegin()) i = (a).rbegin(), _##i=(a).rend(); i != _##i; ++i)
#define w(a) #a << ": " << (a) << "  "

int arr[100][100];
int test[100][100];

int main() { freopen("a.in", "r", stdin); freopen("a.out", "w", stdout);
	int testn;
	cin >> testn;
	rep (tc, testn) {
		memset(test, 63, sizeof(test));
		int n, m;
		cin >> n >> m;
		rep (i, n) {
			rep (j, m) {
				cin >> arr[i][j];
			}
		}
		rep (i, n) {
			int mx = 0;
			rep (j, m) {
				mx = max(mx, arr[i][j]);
			}
			rep (j, m) {
				test[i][j] = min(test[i][j], mx);
			}
		}
		rep (j, m) {
			int mx = 0;
			rep (i, n) {
				mx = max(mx, arr[i][j]);
			}
			rep (i, n) {
				test[i][j] = min(test[i][j], mx);
			}
		}
		bool ok = true;
		rep (i, n) {
			rep (j, m) {
				if (test[i][j] != arr[i][j]) {
					ok = false;
				}
			}
		}
		cout << "Case #" << tc + 1 << ": " << (ok ? "YES" : "NO") << '\n';
	}
}
