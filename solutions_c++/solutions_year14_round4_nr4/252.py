#include <bits/stdc++.h>
using namespace std;
typedef long long lint;

int max_num, num, n, m;
char s[1020][102];
int a[1020], use[1020];

struct Trie {
	Trie *next[26];
	Trie() {
		for (int i = 0; i < 26; i++) {
			next[i] = NULL;
		}
	}
	~Trie() {
		for (int i = 0; i < 26; i++) {
			if (next[i]) {
				delete next[i];
			}
		}
	}
};

int pp;
Trie *root[102];

void insert(Trie *r, char *s) {
	if (*s == 0) {
		return;
	}
	int c = *s - 'A';
	if (r->next[c]) {
		insert(r->next[c], s + 1);
	} else {
		r->next[c] = new Trie();
		pp++;
		insert(r->next[c], s + 1);
	}
}

void dfs(int x) {
	if (x == m) {
		pp = 0;
		for (int i = 0; i < n; i++) {
			if (use[i]) {
				root[i] = new Trie();
				pp++;
			}
		}
		for (int i = 0; i < m; i++) {
			insert(root[a[i]], s[i]);
		}
		for (int i = 0; i < n; i++) {
			if (use[i]) {
				delete root[i];
			}
		}
		if (pp > max_num) {
			max_num = pp;
			num = 1;
		} else if (pp == max_num) {
			num++;
		}
		return;
	}
	for (int i = 0; i < n; i++) {
		a[x] = i;
		use[i]++;
		dfs(x + 1);
		use[i]--;
	}
}

int main() {
	int n_case = 0;
	scanf("%d", &n_case);
	for (int ca = 1; ca <= n_case; ca++) {
		max_num = 0, num = 0;
		scanf("%d%d", &m, &n);
		for (int i = 0; i < m; i++) {
			scanf("%s", s[i]);
		}
		dfs(0);
		printf("Case #%d: %d %d\n", ca, max_num, num);
	}
	return 0;
}
