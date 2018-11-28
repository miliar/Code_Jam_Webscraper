#include <iostream>
#include <cstring>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#define ll long long
#define VI vector<int>
#define inf 1000000000
#define L(s) ((int)(s).size())
#define x first 
#define y second
#define pii pair<int, int>
#define mp make_pair
#define pb push_back
#define all(s) (s).begin(), (s).end()
int n, t, a[1111], d[1111];
map<VI, int> res;
map<VI, VI> prv;
queue<VI> q;
VI fin;
void solve(int n) {
	VI st(0);
	for(int i = 0; i < n; ++i) st.pb(i);
	do {
		int pos = 0;
		while(pos < n - 1 && st[pos + 1] > st[pos]) ++pos;
		while(pos < n - 1 && st[pos + 1] < st[pos]) ++pos;
		if (pos == n - 1) {res[st] = 0; q.push(st); }
	} while(next_permutation(all(st)));
	while(!q.empty()) {
		VI v = q.front();
		q.pop();
		for(int i = 0; i < n - 1; ++i) {
			VI w = v;
			swap(w[i], w[i + 1]);
			if (!res.count(w)) {
				res[w] = res[v] + 1;
				q.push(w);
			}
		}
	}
}
int rev[1111];
inline int cntswap(VI v, int bit) {
	VI s = v;
	sort(all(s));
	if (bit) reverse(all(s));
	int ans = 0;
	for(int i = 0; i < L(v); ++i) {
		int pos = 0; while(v[pos] != s[i]) ++pos;
		while(pos != i) {
			swap(v[pos], v[pos - 1]);
			++ans;
			--pos;
		}
	}
	return ans;
}
int mainsolve(VI v) {
	int ans = inf;
	int maxpos = max_element(all(v)) - v.begin();
	for(int pos = 0; pos < n; ++pos) {
		int cur = 0;
		VI lft(0), rgt(0);
		for(int i = 0; i < n; ++i) {
			if (i == maxpos) continue;
			if (L(lft) < pos) lft.pb(v[i]); else rgt.pb(v[i]);
		}
		ans = min(ans, abs(maxpos - pos) + cntswap(lft, 0) + cntswap(rgt, 1));
	}
	return ans;
}
int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	for(int i = 1; i <= 10; ++i) solve(i);
	cin >> t;
//	t = 10000;
	for(int tc = 1; tc <= t; ++tc) {
		cin >> n;
	//	n = 6;
		for(int i = 0; i < n; ++i) {
			cin >> a[i]; d[i] = a[i];
		}		
		sort(d, d + n);
		for(int i = 0; i < n; ++i) {
			a[i] = lower_bound(d, d + n, a[i]) - d;
		}
		/*for(int i = 0; i < n; ++i) a[i] = i;
		
		random_shuffle(a, a + n);
		
		if (tc < 179) {continue;} */
		VI v(a, a  + n);
		
	/*	int ans0 = solve(v);
		VI w = fin;
		for(int i = 0; i < L(w); ++i) cout << w[i] << " "; cout <<endl;
		w = prv[w];
		for(int i = 0; i < L(w); ++i) cout << w[i] << " "; cout <<endl;
		w = prv[w];
		for(int i = 0; i < L(w); ++i) cout << w[i] << " "; cout <<endl;
		w = prv[w];
		for(int i = 0; i < L(w); ++i) cout << w[i] << " "; cout <<endl;
		int ans1 = mainsolve(v);
*/
//		if (ans0 != ans1) {
//			cerr << "ERROR " << tc << endl;
//			exit(0);
//		}
//		cerr << " OK " << tc << endl;
//		continue;

		cout << "Case #" << tc <<": ";
		cout << res[v] << endl;
	}
}
	