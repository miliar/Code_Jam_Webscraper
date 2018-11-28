#include <cstdio>

int T, N, M, a[20], ans, cnt, cs;
char s[20][20];

struct Node {
	Node *s[26];
}*root[10], buffer[100000], *tot;

Node *newNode() {
	for(int i = 0; i < 26; ++i) {
		tot->s[i] = 0;
	}
	return tot++;
}

void dfs(int x) {
	if(x < N) {
		for(a[x] = 0; a[x] < M; ++a[x]) {
			dfs(x + 1);
		}
	}
	else {
		tot = buffer;
		for(int i = 0; i < M; ++i) {
			root[i] = 0;
		}
		for(int i = 0; i < N; ++i) {
			if(!root[a[i]]) {
				root[a[i]] = newNode();
			}
			Node *cur = root[a[i]];
			for(int j = 0; s[i][j]; ++j) {
				if(!cur->s[s[i][j] - 'A']) {
					cur->s[s[i][j] - 'A'] = newNode();
				}
				cur = cur->s[s[i][j] - 'A'];
			}
		}
		if((int)(tot - buffer) > ans) {
			ans = (int)(tot - buffer);
			cnt = 0;
		}
		if((int)(tot - buffer) == ans) {
			++cnt;
		}
	}
}

int main() {
	freopen("d-input", "r", stdin);
	freopen("out", "w", stdout);
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d", &N, &M);
		for(int i = 0; i < N; ++i) {
			scanf("%s", s[i]);
		}
		ans = cnt = 0;
		dfs(0);
		printf("Case #%d: %d %d\n", ++cs, ans, cnt);
	}
	return 0;
}