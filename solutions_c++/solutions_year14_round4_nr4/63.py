#include <cstdio>
#include <set>
#include <string>
std::set<std::string> t;
int cur[8], m, n, ans, anscnt;
std::string s[8];
char buf[10];
void dfs(int dep) {
	if (dep == m) {
		int cnt = 0;
		for (int i = 0; i < n; i++) {
			t.clear();
			for (int j = 0; j < m; j++) {
				if (cur[j] == i) {
					for (int k = 1; k <= s[j].size(); k++)
						t.insert(s[j].substr(0, k));
				}
			}
			if (!t.size()) return;
			cnt += t.size()+1;
		}
		if (cnt == ans) anscnt++;
		else if (cnt > ans) ans = cnt, anscnt = 1;
	} else {
		for (int i = 0; i < n; i++)
			cur[dep] = i, dfs(dep+1);
	}
}
int main() {
	int T; scanf("%d", &T);
	for (int _ = 1; _ <= T; _++) {
		printf("Case #%d: ", _);
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++)
			scanf("%s", buf), s[i] = buf;
		ans = 0;
		dfs(0);
		printf("%d %d\n", ans, anscnt);
	}
	return 0;
}
