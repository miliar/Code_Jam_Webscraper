#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f;
const double eps = 1e-8, pi = acos(-1.0);

const int C = 26;
const int maxn = 100001;
struct trie_t {
	bool flag;
	trie_t *child[C], *fail;
} trie[maxn], *root[20];
int pt;

trie_t *new_trie() { 
	++pt;
	memset(trie + pt, 0, sizeof(trie_t));
	return &trie[pt];
}

void add(int r, char *str) {
	int l = strlen(str);
	trie_t *p = root[r];
	for (int i = 0; i < l; ++i) {
		int ch = str[i]-'A'; // fixed to [0, C - 1], C = |SIGMA|
		if (!p->child[ch]) p->child[ch] = new_trie();
		p = p->child[ch];
	}
	p->flag = true;
}


int target[20], size[20];
int n, m;
char str[20][20];

int build() {
	pt = 0;
	for (int i = 1; i <= m; ++i) root[i] = new_trie();
	for (int i = 1; i <= n; ++i) {
		add(target[i], str[i]);
	}
	return pt;
}

int ans1, ans2;

void dfs(int dep) {
	if (dep == n + 1) {
		for (int i = 1; i <= m; ++i) size[i] = 0;
		for (int i = 1; i <= n; ++i) ++size[target[i]];
		for (int i = 1; i <= m; ++i) {
			if (size[i] == 0) return;
		}
		int tmp = build();
		if (tmp > ans1) {
			ans1 = tmp;
			ans2 = 1;
		} else if (tmp == ans1) ++ans2;
	} else {
		for (int i = 1; i <= m; ++i) {
			target[dep] = i;
			dfs(dep + 1);
		}
	}
}

int main() {
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("D-small-attempt0.out", "w",stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt <= tests; ++tt) {
		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i) {
			scanf("%s", str[i]);
		}
		ans1 = ans2 = 0;
		dfs(1);
		printf("Case #%d: %d %d\n", tt, ans1, ans2);
	}
	return 0;
}
