#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int e, num, trie[100000][26], q, m, n, opt, ways, tn, ti, i, calls, breaks;
vector<string> v[4];
string a[10000];

int trie_sz (vector<string> v) {
	int i, j;
	for(i = 1; i <= num; i++) 
		for(j = 0; j < 26; j++) trie[i][j] = 0;
	num = 1;
	for(i = 0; i < v.size(); i++) {
		q = 1;
		for(j = 0; j < v[i].size(); j++) if (trie[q][v[i][j] - 'A'] == 0) {
			++num;
			trie[q][v[i][j] - 'A'] = num;
			q = num;
		} else q = trie[q][v[i][j] - 'A'];
	}
	return num;
}

void rec (int k, int serv) {
	v[serv].push_back(a[k]);
	if (k == m) {
		++calls;
		int tek = 0, ts;
		for(int i = 0; i < n; i++) {
			if (v[i].size() == 0) {
				++breaks;
				v[serv].pop_back();
				return;
			}
			tek += trie_sz(v[i]);
		}
//		cout << tek << " " << opt << endl;
		if (tek > opt) {
//			cerr << "optimum changed!" << endl;
			opt = tek;
			ways = 1;
		} else if (tek == opt) ++ways;
	} else {
		for(int i = 0; i < n; i++) rec(k + 1, i);
	}
	v[serv].pop_back();
}

int main () {
	freopen("input.txt", "r", stdin);
	cin >> tn;
	for(ti = 1; ti <= tn; ti++) {
		opt = -1; ways = breaks = calls = 0;
		cin >> m >> n;
		for(i = 1; i <= m; i++) {
			cin >> a[i];
		}
		for(e = 0; e < n; e++) rec(1, 0);
//		cout << calls << " " << breaks << endl;
		cout << "Case #" << ti << ": " << opt << " " << ways << endl;
	}
	return 0;
}