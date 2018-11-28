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
#include <cassert>

using namespace std; 

#define REP(i, n) for (int (i) = 0; (i) < (n); (i)++) 
#define sz(v) (int)(v).size() 
#define all(v) (v).begin(), (v).end()

void solve() {
	int n;
	cin >> n;
	vector <int> a(n);
	REP(i, n) cin >> a[i];
	int res = 0;
	REP(it, n) {
		int pos = min_element(all(a)) - a.begin();
		res += min(pos, sz(a) - 1 - pos);
		a.erase(a.begin() + pos);
	}
	cout << res;
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