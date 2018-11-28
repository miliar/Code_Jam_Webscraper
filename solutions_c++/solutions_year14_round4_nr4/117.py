#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAXN = 10;

vector<string> b[10];

struct Node {
	Node* ch[26];
}*root, POOL[100], *data= POOL;

string a[10];

int n, m, Ans, cnt;

int Cal(const vector<string>& now) {
	memset(POOL, 0, sizeof POOL); root = data = POOL; data++;
	int ret = 1;
	for (int i = 0; i < now.size(); i++) {
		Node *tmp = root;
		for (int j = 0; j < now[i].length(); j++) {
			if (!tmp->ch[now[i][j] - 'A']) tmp->ch[now[i][j] - 'A'] = data++, ret++;
			tmp = tmp->ch[now[i][j] - 'A'];
		}
	}
	return ret;
}

void Dfs(int u) {
	if (u > n) {
		int tmp = 0;
		for (int i = 1; i <= m; i++) {
			tmp += Cal(b[i]);
			if (b[i].empty()) return;
		}
		if (tmp > Ans) Ans = tmp, cnt = 1; else if (Ans == tmp) cnt++;
		return;
	}
	for (int i = 1; i <= m; i++) {
		b[i].push_back(a[u]);
		Dfs(u + 1);
		b[i].pop_back();
	}
}

int main(void) {
	freopen("in", "r", stdin) ;
	freopen("out", "w", stdout);
	int kase; scanf("%d", &kase); for (int _ = 1; _ <= kase; _++) {
		scanf("%d%d", &n, &m); Ans = 0, cnt = 0;
		for (int i = 1; i <= n; i++) cin >>a[i];
		Dfs(1);
		printf("Case #%d: %d %d\n", _, Ans, cnt);
	}
	return 0;
}

