#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <sstream>
using namespace std;
#define ll long long
#define pii pair<int, int>
#define mp make_pair
#define x first
#define y second
#define pb push_back
#define VI vector<int>
#define all(s) (s).begin(),(s).end()
#define L(s) (int)(s).size()
#define inf 1000000000
int t, n;
map<string, int> wds;
VI a[22];
char tmp[222222];
int bad[55555];
int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	gets(tmp); sscanf(tmp, "%d", &t);
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		gets(tmp); sscanf(tmp, "%d", &n);
		wds.clear();
		for(int i = 0; i < n; ++i) {
			a[i].clear();
			gets(tmp);
			istringstream iss(tmp);
			string wd;
			while(iss >> wd) {
				if (!wds.count(wd)) {
					int val = L(wds);
					wds[wd] = val;
				}
				a[i].pb(wds[wd]);
			}
		}
		//cerr << L(wds) << endl;
		int ans = 1e9;
		for(int _mask = 0; _mask < (1 << (n - 2)); ++_mask) {
			int mask = _mask * 4 + 2;
			int cur = 0;
			for(int i = 0; i < n; ++i) {
				int bit = 0; if (mask & (1 << i)) bit = 1;
				for(int j = 0; j < L(a[i]); ++j) {
					bad[a[i][j]] |= (1 << bit);
				}
			}
			for(int i = 0; i < L(wds); ++i) {
				if (bad[i] == 3) ++cur;
				bad[i] = 0;
			}
			ans = min(ans, cur);
		}
		cout << "Case #" << tc << ": " << ans << endl;
	}
}
