#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

using namespace std;

int m, n;
char s[1000][11];

int ans, cnt;
vector<int> st[100];
void dfs(int i) {
	if (i == m) {
		int get = 0;
		for (int j = 0; j < n; j++) {
			vector<string> lst;
			for (unsigned k = 0; k < st[j].size(); k++) {
				int len = strlen(s[st[j][k]]);
				for (int i = 0; i <= len; i++) {
					lst.push_back(string(s[st[j][k]], s[st[j][k]] + i));
				}
			}
			sort(lst.begin(), lst.end());
			get += unique(lst.begin(), lst.end()) - lst.begin();
		}
		if (get > ans) {
			ans = get;
			cnt = 0;
		}
		if (ans == get)
			cnt++;
	} else {
		for (int j = 0; j < n; j++) {
			st[j].push_back(i);
			dfs(i + 1);
			st[j].pop_back();
		}
	}
}

int main() {
	freopen("src/out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		cerr << t << endl;
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++) {
			scanf("%s", s[i]);
		}
		ans = 0;
		dfs(0);
		printf("%d %d\n", ans, cnt);
	}
}
