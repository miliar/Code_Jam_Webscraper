#include <bits/stdc++.h>
using namespace std;

const int P = 1000000007;

int m, n, id[10], ma, cnt;
char s[10][100];

struct Trie {
	static const int SIZE = 1000;
	int e[SIZE][26], sz;
	void clear() {
		sz = 1;
		memset(e[0], -1, sizeof(e[0]));
	}
	int size() {
		return sz == 1 ? 0 : sz;
	}
	void insert(const char* s) {
		int x = 0;
		for (int i = 0; s[i]; ++i) {
			int k = s[i] - 'A';
			if (e[x][k] == -1) {
				memset(e[sz], -1, sizeof(e[sz]));
				e[x][k] = sz++;
			}
			x = e[x][k];
		}
	}
} trie[4];

int build() {
	for (int i = 0; i < n; ++i) trie[i].clear();
	for (int i = 0; i < m; ++i) {
		trie[id[i]].insert(s[i]);
	}
	int ret = 0;
	for (int i = 0; i < n; ++i) {
		ret += trie[i].size();
	}
	return ret;
}

void dfs(int k) {
	if (k == m) {
		int x = build();
		if (x > ma) {
			ma = x;
			cnt = 1;
		} else if (x == ma) {
			++cnt;
		}
		return ;
	}
	for (int i = 0; i < n; ++i) {
		id[k] = i;
		dfs(k+1);
	}
}

int main() {
	int T; scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; ++i) {
			scanf("%s", s[i]);
		}
		ma = cnt = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", cas, ma, cnt);
	}
}
