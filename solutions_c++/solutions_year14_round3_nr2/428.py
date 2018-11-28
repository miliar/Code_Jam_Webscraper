#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";
		int n;
		cin >> n;
		vector<string> c(n);
		vector<int> cnt(256);
		vector<bool> ocr(256);
		vector<bool> btw(256);
		vector<char> pre(256);
		vector<char> nxt(256);
		vector<bool> vis(256);
		bool yes = true;
		for (int i = 0; i < n; i++) {
			cin >> c[i];
			c[i].erase(unique(c[i].begin(), c[i].end()), c[i].end());
			for (int j = 0; j < c[i].size(); j++) {
				ocr[c[i][j]] = true;
			}
			for (int j = 1; j < c[i].size() - 1; j++) {
				if (btw[c[i][j]]) {
					yes = false;
				} else {
					btw[c[i][j]] = true;
				}
			}
			if (c[i].size() == 1) {
				cnt[c[i][0]]++;
			} else {
				if (c[i][0] == c[i][c[i].size() - 1]) {
					yes = false;
				}
				if (nxt[c[i][0]]) {
					yes = false;
				} else {
					nxt[c[i][0]] = c[i][c[i].size() - 1];
				}
				if (pre[c[i][c[i].size() - 1]]) {
					yes = false;
				} else {
					pre[c[i][c[i].size() - 1]] = c[i][0];
				}
			}
		}
		for (int i = 'a'; i <= 'z'; i++) {
			if (ocr[i] && !btw[i] && !vis[i] && !pre[i]) {
				int u = i;
				vector<char> lst;
				do {
					lst.push_back(u);
					vis[u] = true;
				} while (u = nxt[u]);
			}
		}
		for (int i = 'a'; i <= 'z'; i++) {
			if (ocr[i] && !btw[i] && !vis[i]) {
				yes = false;
			}
			if (btw[i] && (pre[i] || nxt[i])) {
				yes = false;
			}
		}
		if (yes) {
			const long long MOD = 1000000007;
			long long fac[n + 1];
			fac[0] = 1;
			for (int i = 1; i <= n; i++)
				fac[i] = fac[i - 1] * i % MOD;
			long long ans = 1;
			long long cmp = 0;
			vector<bool> vis(256);
			for (int i = 'a'; i <= 'z'; i++) {
				if (ocr[i] && !btw[i] && !vis[i] && !pre[i]) {
					int u = i;
					vector<char> lst;
					do {
						lst.push_back(u);
						vis[u] = true;
					} while (u = nxt[u]);
					for (int j = 0; j < lst.size(); j++) {
						ans = ans * fac[cnt[lst[j]]] % MOD;
					}
					cmp++;
				}
			}
			ans = ans * fac[cmp] % MOD;
			cout << ans << endl;
		} else {
			cout << 0 << endl;
		}
	}
}
