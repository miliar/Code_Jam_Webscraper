#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <complex>
#include <cstdio>
#include <vector>
#include <cctype>
#include <string>
#include <ctime>
#include <cmath>
#include <set>
#include <map>

typedef long double LD;
typedef long long LL;

using namespace std;

#define sz(A) (int)(A).size()
#define mp make_pair
#define pb push_back

const int N = 1005;

string s[N];
int m, n, res[N * N], root[N], cnt, serv[N], mx;
bool ok[N];

struct node {
	int to[26];
};

node trie[N * N / 26];

int occ = 0;

void add(int v, string str) {
	int now = v;
	for (int i = 0; i < sz(str); i++) {
		if (!trie[now].to[str[i] - 'A']) {
			cnt++;
			trie[now].to[str[i] - 'A'] = cnt;
		}
		now = trie[now].to[str[i] - 'A'];
//		if (occ == 1)
//			cerr << now << " " << cnt << endl;
	}
}                           

void solve() {
	for (int i = 0; i <= cnt; i++) {
		for (int j = 0; j < 26; j++)
			trie[i].to[j] = 0;
	}
	cnt = 0;	
	int cnt_serv = 0;
	for (int i = 0; i < n; i++) {
		cnt++;
		ok[i] = 0;
		root[i] = cnt;		
	}
	for (int i = 0; i < m; i++) {
		add(root[ serv[i] ], s[i]);				
		if (!ok[serv[i]]) {
			ok[serv[i]] = 1;
			cnt_serv++;
		}
	}
	occ++;
/*	if (occ == 2) {
		for (int i = 1; i <= cnt; i++) {
			for (int j = 0; j < 26; j++) {
				if (trie[i].to[j]) {
					cerr << i << " " << char('A' + j) << " " << trie[i].to[j] << endl;
				}
			}
		}
	}*/

//	cerr << cnt_serv << " " << cnt << endl;  
	if (cnt_serv == n) {
		res[cnt]++;
		mx = max(mx, cnt);
	}
}

void dfs(int pos) {
	if (pos == m) {
		solve();
		return;
	}
	for (int i = 0; i < n; i++) {
		serv[pos] = i;
		dfs(pos + 1);
	}
}

int main() {
	int t;
	cin >> t;

	for (int q = 0; q < t; q++) {
		mx = 0;
		memset(res, 0, sizeof(res));
		cin >> m >> n;
		for (int i = 0; i < m; i++) 
			cin >> s[i];
		dfs(0);
		for (int i = 0; ; i++)
			if (res[i]) {
				printf("Case #%d: %d %d\n", q + 1, mx, res[mx]);
				break;
			}
	}

	return 0;
}
