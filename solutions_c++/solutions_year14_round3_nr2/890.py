#include <stdio.h>
#include <string.h>

#define MAXN 101
#define MAX_LENGTH 101

int N, cnt[256], a[MAXN], res;
char Sets[MAXN][MAX_LENGTH];
bool vis[MAXN];

bool special_case(char *s)
{
	int i, c;
	bool test[256];

	memset(test, 0, sizeof(test));
	for (i = c = 0; s[i]; i++) {
		if (!test[s[i]]) {
			test[s[i]] = 1;
			c = c + 1;
		}
	}

	if (s[0] == s[i-1] && c > 1) return false;

	return true;
}

bool simplify_set(char *s)
{
	char b;
	int i, j, c;

	for (i = 0; s[i]; i++); b = s[--i];
	for (j = i - 1; j >= 0 && s[j] == s[i]; j--); s[j + 2] = 0;
	for (i = 1; s[i] && s[i] == s[0]; i++);

	if (!s[i]) {
		s[1] = b;
		s[2] = 0;
		return true;
	}

	while (1) {
		for (c = 0, j = i; s[j] == s[i]; j++, c++);
		if (!s[j]) break;
		if (c != cnt[s[i]]) return false;
		i = j;
	}

	s[1] = b;
	s[2] = 0;
	return true;
}

bool simplification()
{
	int i, j;

	memset(cnt, 0, sizeof(cnt));
	for (i = 0; i < N; i++) {
		for (j = 0; Sets[i][j]; cnt[Sets[i][j++]]++);
	}

	for (i = 0; i < N; i++) 
		if (!simplify_set(Sets[i])) return false;
	
	memset(cnt, 0, sizeof(cnt));
	for (i = 0; i < N; i++) {
		for (j = 0; Sets[i][j]; cnt[Sets[i][j++]]++);
	}
	
	return true;
}

void read()
{
	int i, j;

	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%s", Sets[i]);
	}
}

bool chk(int k)
{
	int c, i, j;
	char str[1000];

	str[0] = 0;
	for (i = 0; i <= k; i++) 
		strcat(str, Sets[a[i]]);
	
	for (i = 0, c = 1; str[i]; i++) {
		if (str[i] != str[i+1]) {
			if (!str[i+1]) break;
			if (c != cnt[str[i]]) 
				return false;
			c = 1;
			continue;
		}
		c = c + 1;
	}

	return true;
}

void dfs(int k)
{
	int i;

	if (k == N) {
		res++;
		return;
	}

	for (i = 0; i < N; i++) {
		if (!vis[i]) {
			a[k] = i;
			if (!chk(k)) continue;
			vis[i] = 1;
			dfs(k + 1);
			vis[i] = 0;
		}
	}
}

int main()
{
	int T, t;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		read();
		if ((N == 1 && !special_case(Sets[0])) || !simplification()) {
			printf("Case #%d: 0\n", t);
			continue;
		}

		res = 0;
		memset(vis, 0, sizeof(vis));
		dfs(0);
		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}

