#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;
#define ll long long
#define inf 1000000000
#define L(s) ((int)(s).size())
#define x first 
#define y second
#define pii pair<int, int>
#define mp make_pair
int t, n, m, k;
string s[11];
int split[11];
int worst = 0, total = 0;
int ch[1111][26];
void divide(int v) {
	if (v == k) {
		int now = 0;
		for(int serv = 0; serv < n; ++serv) {
			int onserv = 0;
			m = 1;
			for(int i = 0; i < 26; ++i) ch[0][i] = -1;
			for(int str = 0; str < k; ++str) {
				if (split[str] != serv) continue;
				++onserv;
				string t = s[str];
				int cur = 0;
				for(int i = 0; i < L(t); ++i) {
					if (ch[cur][t[i] - 'A'] == -1) {
						ch[cur][t[i] - 'A'] = m;
						memset(ch[m], -1, sizeof(ch[m]));
						++m;
					}
					cur = ch[cur][t[i] - 'A'];
				}
			}
			if (!onserv) return;
			now += m;
		}
		if (now > worst) {
			worst = now;
			total = 0;
		}
		if (now == worst) ++total;
		return;
	}
	for(int i = 0; i < n; ++i) {
		split[v] = i;
		divide(v + 1);
	}
}
int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int tc = 1; tc <= t; ++tc) {
		cerr << tc << endl;
		cin >> k >> n;
		for(int i = 0; i < k; ++i) {
			cin >> s[i];
		}
		worst = total = 0;
		divide(0);
		cout << "Case #" << tc <<": ";
		cout << worst << " " << total << endl;
	}
}
