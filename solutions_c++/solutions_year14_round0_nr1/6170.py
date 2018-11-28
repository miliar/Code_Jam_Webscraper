#include <iostream>
#include <cstdio>
#include <cassert>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <sstream>
#include <cstdlib>
#include <numeric>
#include <bitset>
#include <deque>
using namespace std;

#define REP(i, m, n) for(int i=(m); i<int(n); ++i)
#define rep(i, n) for(int i=0; i<int(n); ++i)
#define each(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); ++it)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb push_back                                                                          
#define mp make_pair
#define def(a, x) __typeof(x) a = x
#define fi first
#define se second
typedef long long ll;
typedef pair<ll, ll> PI;
const int dx[] = {1, 0, -1, 0, 1, 1, -1, -1}, dy[] = {0, 1, 0, -1, 1, -1, 1, -1};

void solve() {
	int a, b;
	cin >> a;
	set<int> ans1, ans2;
	rep(i, 4) rep(j, 4) {
		int c;
		cin >> c;
		if (a == i+1) ans1.insert(c);
	}
	cin >> b;
	rep(i, 4) rep(j, 4) {
		int c;
		cin >> c;
		if (b == i+1) ans2.insert(c);
	}
	int cnt = 0;
	int res = -1;
	each(it, ans1) if (ans2.count(*it))  cnt++, res = *it;
	if (cnt == 0) cout << "Volunteer cheated!" << endl;
	else if (cnt > 1)cout << "Bad magician!" << endl;
	else cout << res << endl;
}
int main() {
	int T; cin >> T;
	for(int t=1; t<=T; t++) {
		cout << "Case #" << t << ": ";
		solve();
	}
}

