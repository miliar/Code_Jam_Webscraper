#pragma comment(linker,"/stack:256000000")

#include <cmath> 
#include <ctime> 
#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <cstring> 
#include <cstdlib> 
#include <queue> 
#include <cstdio> 
#include <cfloat>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

int a[10010];
bool u[10010];

void solve() {
	int n, x;
	cin >> n >> x;
	REP(i, n) cin >> a[i];
	sort(a, a + n);
	reverse(a, a + n);
	REP(i, n) u[i] = 0;
	int cnt = 0;
	REP(i, n) {
		if (u[i]) continue;
		u[i] = 1;
		int need = x - a[i];
		int pos = -1;
		for (int j = i + 1; j < n; j++) {
			if (u[j]) continue;
			if (a[j] <= need) {
				if (pos == -1 || a[j] > a[pos]) {
					pos = j;
				}
			}
		}
		if (pos != -1) {
			u[pos] = 1;
		}
		++cnt;
	}
	cout << cnt;
}

int main() {
#ifdef LOCAL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int tst = 1; tst <= T; tst++) {
		cerr << tst << endl;
		cout << "Case #" << tst << ": ";
		solve();
		cout << endl;
	}
	return 0;
}