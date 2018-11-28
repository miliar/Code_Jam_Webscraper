#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <stack>
#include <vector>

using namespace std;

#define pb push_back
#define mp make_pair
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define foreach(e, x) for (__typeof(x.begin()) e = x.begin(); e != x.end(); e++)
typedef long long LL;
typedef pair<int, int> PII;

int t, m, n;
string s[8];
vector<int> serv[4];
int trie[4][100][26], triec[4];
int ans, ansc;

void go(int m) {
	if (m == 0) {
		for (int i = 0; i < n; ++i)
			if (serv[i].empty())
				return;
		/*cout << endl << endl;
		for (int i = 0; i < n; ++i) {
			cout << serv[i].size() << endl;
			REP(j, serv[i].size())
				cout << serv[i][j] << ' ';
			cout << endl;
		}
		cout << endl << endl;*/
		for (int i = 0; i < n; ++i) {
			triec[i] = 1;
			for (int j = 0; j < 26; ++j)
				trie[i][0][j] = -1;
		}
		REP(i, n) REP(j, serv[i].size()) {
			int cur = 0;
			string &ss = s[serv[i][j]];
			REP(k, ss.length()) {
				if (trie[i][cur][ss[k] - 'A'] == -1) {
					trie[i][cur][ss[k] - 'A'] = triec[i];
					REP(t, 26) {
						trie[i][triec[i]][t] = -1;
					}
					++triec[i];
				}
				cur = trie[i][cur][ss[k] - 'A'];
			}
		}
		int cur = 0;
		REP(i, n)
			cur += triec[i];
		if (cur > ans) {
			ans = cur;
			ansc = 1;
		} else if (cur == ans)
			++ansc;
		return;
	}
	for (int i = 0; i < n; ++i) {
		serv[i].pb(m - 1);
		go(m - 1);
		serv[i].pop_back();
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int test = 1; test <= t; ++test) {
		cin >> m >> n;
		REP(i, m)
			cin >> s[i];
		ans = 0;
		ansc = 0;
		for (int i = 0; i < n; ++i)
			serv[i].clear();
		go(m);
		cout << "Case #" << test << ": " << ans << ' ' << ansc << endl;
	}
	return 0;
}
