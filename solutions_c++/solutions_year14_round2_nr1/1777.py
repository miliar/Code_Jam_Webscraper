#include <stdio.h>
#include <string.h>
#include <algorithm>

#define MAX_N 155
#define MAX_LENGTH 45

using std::sort;

struct string {
	char str[MAX_LENGTH];
} source[MAX_N], target[MAX_N];

int N, L, best;

bool operator < (const string &A, const string &B)
{
	return strcmp(A.str, B.str) < 0;
}

void xswitch(int i)
{
	int j;

	for (j = 0; j < N; j++) {
		if (source[j].str[i] == '1')
			source[j].str[i] = '0';
		else 
			source[j].str[i] = '1';
	}
	sort(source, source + N);
}

void dfs(int i, int n)
{
	int j;

	if (i >= L) {
		if (best == -1 || best > n) best = n;
		return;
	}

	for (j = 0; j < N; j++) 
		if (source[j].str[i] != target[j].str[i]) break;
	if (j == N) dfs(i + 1, n);

	xswitch(i);
	for (j = 0; j < N; j++) 
		if (source[j].str[i] != target[j].str[i]) {
			xswitch(i);
			return;
		}

	dfs(i + 1, n + 1);
	xswitch(i);
}

int main()
{
	int T, t, i;

	scanf("%d", &T);
	for (t = 1; t <= T; t++) {
		scanf("%d%d", &N, &L);
		for (i = 0; i < N; i++) 
			scanf("%s", source[i].str);
		for (i = 0; i < N; i++) 
			scanf("%s", target[i].str);

		best = -1;
		sort(source, source + N);
		sort(target, target + N);
		dfs(0, 0);

		if (best == -1) printf("Case #%d: NOT POSSIBLE\n", t);
		else printf("Case #%d: %d\n", t, best);
	}

	return 0;
}

