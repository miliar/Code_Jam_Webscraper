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

int m, n;
int x[10];
int t[100][26];
vector <string> str;
int worst, res;

void go(int p) {
	if (p == m) {
		REP(i, n) {
			bool OK = 0;
			REP(j, m) {
				if (x[j] == i) {
					OK = 1;
				}
			}
			if (!OK) {
				return;
			}
		}
		int sum = 0;
		REP(i, n) {
			vector <int> id;
			REP(j, m) {
				if (x[j] == i) {
					id.push_back(j);
				}
			}
			assert(sz(id) > 0);
			memset(t[0], -1, sizeof(t[0]));
			int T = 1;
			REP(j, sz(id)) {
				string s = str[id[j]];
				int v = 0;
				REP(k, sz(s)) {
					if (t[v][s[k] - 'A'] == -1) {
						memset(t[T], -1, sizeof(t[T]));
						t[v][s[k] - 'A'] = T++;
					}
					v = t[v][s[k] - 'A'];
				}
			}
			sum += T;
		}
		if (sum > worst) {
			worst = sum;
			res = 1;
		} else if (sum == worst) {
			res++;
		}
	} else {
		REP(i, n) {
			x[p] = i;
			go(p + 1);
		}
	}
}

void solve() {
	worst = res = 0;
	cin >> m >> n;
	str.clear();
	str.resize(m);
	REP(i, m) cin >> str[i];
	go(0);
	cout << worst << " " << res;
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