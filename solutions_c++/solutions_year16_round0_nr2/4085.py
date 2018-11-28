#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;

#define MAXN (100+10)

int t, n;
char s[MAXN];

bool check(char c, int mode) {
	if (mode == 0) return c == '+';
	else return c == '-';
}

int cal(int k, int mode) {
	if (k < 0) return 0;
	if (check(s[k], mode)) return cal(k-1, mode);
	else return 1 + cal(k-1, 1-mode);
}

int solve() {
	n = strlen(s);
	return cal(n-1, 0);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for (int i = 1;i <= t;++i) {
		scanf("%s", &s);
	//	printf("%s\n", s);
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}