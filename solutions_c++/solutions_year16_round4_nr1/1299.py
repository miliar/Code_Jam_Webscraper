#include <bits/stdc++.h>

#define fc first
#define sc second
#define mp make_pair

using namespace std;

const int MAXN = (1 << 13);

bool bad = false;
int cnt[3];
int a[MAXN];
int last;

void dfs(int d, int l, int r) {
	if (r - l == 1) {
		cnt[d]--;
		a[l] = d;
		return;
	}
	if (d == 0) {
		int m = (l + r) / 2;
		dfs(0, l, m);
		dfs(1, m, r);
	}	
	if (d == 1) {
		int m = (l + r) / 2;
		dfs(1, l, m);
		dfs(2, m, r);
	}
	if (d == 2) {
		int m = (l + r) / 2;
		dfs(0, l, m);
		dfs(2, m, r);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t, n, r, s, p;
	vector <char> c;
	cin >> t;
	for (int kk = 0; kk < t; kk++) {
		string er = "";
		cin >> n >> r >> p >> s;
		n = (1 << n);
		cnt[0] = p, cnt[1] = r, cnt[2] = s;
		vector <string> ans;
		dfs(0, 0, n);
		bool good = true;
		for (int d = 0; d < 3; d++) {
			if (cnt[d] < 0) {
				good = false;
			}
		}
		if (good) {
			string t = "";
			for (int i = 0; i < n; i++) {
				t += (a[i] == 0 ? 'P' : (a[i] == 1 ? 'R' : 'S'));
			}
			int sz = 1;
			while (sz < n) {
				vector <string> go;
				for (int i = 0; i < n; i += sz) {
					string rar = "";
					for (int j = i; j < i + sz; j++) {
						rar += t[j];
					}
					go.push_back(rar);
				}
				for (int p = 0; p < (int) go.size() - 1; p += 2) {
					if (go[p] > go[p + 1]) {
						swap(go[p], go[p + 1]);
					}
				}
				t = "";
				for (int p = 0; p < (int) go.size(); p++) {
					t += go[p];
				}
				sz *= 2;
			}
			ans.push_back(t);
		}
		good = true;
		cnt[0] = p, cnt[1] = r, cnt[2] = s;
		dfs(1, 0, n);
		for (int d = 0; d < 3; d++) {
			if (cnt[d] < 0) {
				good = false;
			}
		}
		if (good) {
			string t = "";
			for (int i = 0; i < n; i++) {
				t += (a[i] == 0 ? 'P' : (a[i] == 1 ? 'R' : 'S'));
			}
			int sz = 1;
			while (sz < n) {
				vector <string> go;
				for (int i = 0; i < n; i += sz) {
					string rar = "";
					for (int j = i; j < i + sz; j++) {
						rar += t[j];
					}
					go.push_back(rar);
				}
				for (int p = 0; p < (int) go.size() - 1; p += 2) {
					if (go[p] > go[p + 1]) {
						swap(go[p], go[p + 1]);
					}
				}
				t = "";
				for (int p = 0; p < (int) go.size(); p++) {
					t += go[p];
				}
				sz *= 2;
			}
			ans.push_back(t);
		}
		good = true;
		cnt[0] = p, cnt[1] = r, cnt[2] = s;
		dfs(2, 0, n);
		for (int d = 0; d < 3; d++) {
			if (cnt[d] < 0) {
				good = false;
			}
		}
		if (good) {
			string t = "";
			for (int i = 0; i < n; i++) {
				t += (a[i] == 0 ? 'P' : (a[i] == 1 ? 'R' : 'S'));
			}
			int sz = 1;
			while (sz < n) {
				vector <string> go;
				for (int i = 0; i < n; i += sz) {
					string rar = "";
					for (int j = i; j < i + sz; j++) {
						rar += t[j];
					}
					go.push_back(rar);
				}
				for (int p = 0; p < (int) go.size() - 1; p += 2) {
					if (go[p] > go[p + 1]) {
						swap(go[p], go[p + 1]);
					}
				}
				t = "";
				for (int p = 0; p < (int) go.size(); p++) {
					t += go[p];
				}
				sz *= 2;
			}
			ans.push_back(t);
		}
		if (ans.size()) {
			sort(ans.begin(), ans.end());
			er = ans[0];
		} else {
			er = "IMPOSSIBLE";
		}
		cout << "Case #" << kk + 1 << ": " << er << endl;
	}
}