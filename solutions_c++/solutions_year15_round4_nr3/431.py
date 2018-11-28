#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <ctime>

#define inf 0x3f3f3f3f
#define Inf 0x3FFFFFFFFFFFFFFFLL
#define rep(i, n) for (int i = 0; i < (n); ++i)
#define Rep(i, n) for (int i = 1; i <= (n); ++i)
#define clr(x, a) memset(x, (a), sizeof x)
using namespace std;
typedef long long ll;
int const N = 220;
map<string, int> mp;
int idx;
set<int> eng, fri;
bool ce[N*20], cf[N*20];
bool de[N], df[N];

vector<int> v[N];
vector<string> vs[N];

int getIdx(string s) {
	if (mp.find(s) == mp.end()) mp[s] = ++idx;
	return mp[s];
}
int main() {
	freopen("C-small-attempt2.in", "r", stdin);
	freopen("c-small-ans2.txt", "w", stdout);
	int T, ca = 1;
	cin >> T; int n;
	string buf, s;
	while (T--) {
		cerr<<T<<endl;
		cin >> n; cin.ignore();
		idx = 0; mp.clear();
		rep(i, n) {
			v[i].clear(); vs[i].clear();
			getline(cin, buf);
			istringstream is(buf);
			while (is >> s) {
				vs[i].push_back(s);
			}
		}
		for (int i = 2; i < n; ++i) {
			rep(j, vs[i].size()) {
				v[i].push_back(getIdx(vs[i][j]));
			}
		}
		int lim = idx;
		
		rep(i, 2) {
			rep(j, vs[i].size()) {
				v[i].push_back(getIdx(vs[i][j]));
			}
		}
		eng.clear(), fri.clear();
		clr(ce, 0), clr(cf, 0);
		rep(i, v[0].size()) {
			eng.insert(v[0][i]);
			ce[v[0][i]] = 1;
		}
		rep(i, v[1].size()) {
			fri.insert(v[1][i]);
			cf[v[1][i]] = 1;
		}
		int ans = 0;
		for (int i = lim + 1; i <= idx; ++i) {
			if (ce[i] && cf[i]) ++ans;
		}
		int t = inf;
		int m = 1 << (n - 2);
		rep(i, m) {
			int q = 0;
			clr(de, 0), clr(df, 0);
			
			rep(j, n - 2) {
				if (i >> j & 1) {
					rep(k, v[j+2].size()) {
						de[v[j+2][k]] = 1;
					}
				} else {
					rep(k, v[j+2].size()) {
						df[v[j+2][k]] = 1;
					}
				}
			}

			Rep(j, lim) {
				if ((ce[j]||de[j]) && (cf[j]||df[j])) {
					++q;
				}
			}
			t = min(t, q);
		}
		printf("Case #%d: %d\n", ca++, ans + t);
	}
	return 0;
}
