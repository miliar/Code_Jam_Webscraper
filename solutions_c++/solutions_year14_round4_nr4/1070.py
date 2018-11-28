#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

vector<bool> mark;    // Markierung für Tiefensuche
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (auto i=(c).begin(); i!=(c).end(); i++)
#define mp make_pair
#define pb push_back

struct trie {
	vs ws;
	int nc = 0;
	void add(const string & s) {
		ws.pb(s);
	}
	int gtc() {
		int r = ws[0].length() + 1;
		FOR(i, 1, ws.size()) {
			int same = 0;
			while(same < ws[i-1].size() && same < ws[i].size() && ws[i-1][same] == ws[i][same]) same++;
			r += ws[i].size() - same;
		}
		return r;
	}
};

int main() {
	int tc;
	cin >> tc;
	FOR(t, 0, tc) {
		int w, n;
		cin >> w >> n;

		vs ws(w);
		FOR(i, 0, w) cin >> ws[i];
		sort(all(ws));

		vector<int> v(w+1);
		vector<trie> ts(n);
		int best = 0, bestC = 0;
		if (n == 1) {
			FOR(i, 0, w) {
				ts[v[i]].ws.pb(ws[i]);
			}
			cout << "Case #" << t+1 << ": " << ts[0].gtc() << " " << 1 << endl;
			continue;
		}
		while(v[w] == 0) {
			v[0]++;
			int k = 0;
			while(v[k] == n) {
				v[k] = 0;
				v[k+1]++;
				k++;
			}
			FOR(i, 0, n) ts[i].ws.clear();
			FOR(i, 0, w) {
				ts[v[i]].ws.pb(ws[i]);
			}
			int kk = 0;
			FOR(i, 0, n) {
				if (ts[i].ws.size() == 0) {
					kk = -1;
					break;
				}
				kk += ts[i].gtc();
			}
			if (kk != -1) {
				if (kk == best) {
					bestC++;
				} else if (kk > best) {
					best = kk;
					bestC = 1;
				}
			}
		}

		cout << "Case #" << t+1 << ": " << best << " " << bestC << endl;
	}
}


