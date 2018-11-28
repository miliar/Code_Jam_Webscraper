#include<stdio.h>
#include <iostream>
#include <string.h>
#include <string>
using namespace std;
string ans;
string tmp;
char rps[3] = { 'R', 'P', 'S' };
int n, r, p, s;
bool check() {
	int cr, cp, cs;
	cr = cp = cs = 0;
	for (int i = 0; i < tmp.size(); ++i) {
		if (tmp[i] == 'R')
			cr++;
		if (tmp[i] == 'P')
			cp++;
		if (tmp[i] == 'S')
			cs++;
	}
	if (cr == r && cp == p && cs == s) {
		return true;
	}
	return false;
}
void dfs1(int n, int now) {
	if (n == 0) {
		tmp.push_back(rps[now]);
		return;
	}
	dfs1(n - 1, now);
	dfs1(n - 1, (now + 1) % 3);
}
void dfs2(int st, int l) {
	if (l == 1) {
		return;
	}
	dfs2(st, l / 2);
	dfs2(st + l / 2, l / 2);
	if (tmp.substr(st, l / 2) > tmp.substr(st + l / 2, l / 2)) {
		for (int i = 0; i < l / 2; ++i) {
			swap(tmp[st + i], tmp[st + i + l / 2]);
		}
	}
}
int main() {
	int t, cas = 0;
	scanf("%d", &t);
	while (t--) {
		cas++;
		scanf("%d%d%d%d", &n, &r, &p, &s);
		tmp.clear();
		ans.clear();
		dfs1(n, 0);
		if (check()) {
			dfs2(0, 1 << n);
			if (ans.empty() || ans > tmp) {
				ans = tmp;
			}
		}
		tmp.clear();
		dfs1(n, 1);
		if (check()) {
			dfs2(0, 1 << n);
			if (ans.empty() || ans > tmp) {
				ans = tmp;
			}
		}
		tmp.clear();
		dfs1(n, 2);
		if (check()) {
			dfs2(0, 1 << n);
			if (ans.empty() || ans > tmp) {
				ans = tmp;
			}
		}
		if (ans.empty()) {
			cout << "Case #" << cas << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << cas << ": " << ans << endl;
		}
	}

}
