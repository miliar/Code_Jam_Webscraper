#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;
#define pii pair<int, int>
#define pdd pair<double, double>
#define mp make_pair
#define x first
#define y second
#define L(s) ((int)(s).size())
#define pb push_back
#define VI vector<int>
#define ll long long
#define all(s) (s).begin(), (s).end()
map<string, set<int> > can;
pii oth;
inline pii naive(int n, int p) {
	VI v(0), tms(0); 
	for(int i = 0; i < (1 << n); ++i) {
		v.pb(i);
		tms.pb(0);
	}
	int tot = 0;
	do {
		++tot;
		map<string, VI> cur;
		cur.clear();
		cur[""] = v;
		for(int i = 0; i < n; ++i) {
			map<string, VI> nxt;
			nxt.clear();
			for(map<string, VI>::iterator it = cur.begin(); it != cur.end(); ++it) {
				VI tmp = it->y;
				for(int j = 0; j < L(tmp); j += 2) {
					if (tmp[j] < tmp[j + 1]) {
						nxt[it->x + "W"].pb(tmp[j]);
						nxt[it->x + "L"].pb(tmp[j + 1]);
					} else {
						nxt[it->x + "W"].pb(tmp[j + 1]);
						nxt[it->x + "L"].pb(tmp[j]);
					}
				}
			}
			cur = nxt;
			for(map<string, VI>::iterator it = cur.begin(); it != cur.end(); ++it) {
				for(int j = 0; j < L(it->y); ++j) {
					can[it->x].insert(it->y[j]);
				}
			}
		}
		map<string, VI>::iterator it = cur.end(); 
		for(int act = p - 1; act >= 0; --act) {
			--it;
			tms[it->y[0]]++;
		}

		if (tot == 1) {
			VI res(0);
			for(map<string, VI>::iterator it = cur.begin(); it != cur.end(); ++it) res.pb(it->y[0]);
			reverse(all(res));
			set<int> st;st.clear();
			for(int j = 0; j < p; ++j) {
				st.insert(res[j]);
			}
			set<int>::iterator it = st.end(); --it;
			oth.y = *it;
			for(int j = 0; ; ++j) {
				if (st.find(j) == st.end()) {
					oth.x = j - 1;
					break;
				}
			}
			return mp(1, 1);
		}

	}while(next_permutation(all(v)));
	int max_can = -1;
	int min_can = (1 << n);
	for(int i = 0; i < L(tms); ++i) {
		if (tms[i] == tot) min_can = i;
		if (tms[i]) max_can = i;
	}
	return mp(min_can, max_can);
}
pii dfs(string s, int st, int fn) {
	if (L(s) == 0) return mp(st, st);
	pii lft = dfs(s.substr(0, L(s) - 1), st, st + (fn - st) / 2);
	pii rgt = dfs(s.substr(0, L(s) - 1), st + (fn - st) / 2, fn);
	if (s[L(s) - 1] == 'W') {
		return mp(lft.x, rgt.y);
	} else {
		return mp(lft.y, rgt.x);
	}
}
inline ll rev(ll num, int n) {
	ll ans = 0;
	for(int bit = 0; bit < n; ++bit) 
		if (num & (1LL << bit))
			ans |= (1LL << (n - 1 - bit));
	return ans;
}
inline ll get(int n, ll p) {
	ll tail = 0;
	for(int bit = n - 1; bit >= 0; --bit) {
		tail += (1LL << bit);
		if (rev(tail, n) >=  p) tail -= (1LL << bit);
	}
	return tail;
}
inline pair<ll, ll> solve(int n, ll p) {
	pair<ll, ll> ans = mp(get(n, p), ((~get(n, (1LL << n) - p)) & ((1LL << n) - 1)) - 1);
	if (p == (1LL << n)) ans.y = p - 1;
	return ans;
}
int n, p, tc;
int main() {
	/*for(int p = 1; p <= 16; ++p) {
		naive(4, p);
		pair<ll, ll> tt = solve(4, p);
		cout << p << " " << oth.x << " " << oth.y << " " << tt.x << " " << tt.y << endl;
	}*/
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> tc;
	for(int tn = 1; tn <= tc; ++tn) {
		cerr << tn << endl;
		int n; ll p;
		cin >> n >> p;
		pair<ll, ll> tt = solve(n, p);
		//cout << tt.y << " " << tt.x << endl;
		cout << "Case #" << tn << ": " << tt.y << " " << tt.x << endl;
		//naive(n, (int)p);
		//cout << oth.x << " " << oth.y << endl;
	}
//	cin >> n >> p;
//	pii res = naive(n, p);
//	cout << res.x << " " << res.y << endl;
} 