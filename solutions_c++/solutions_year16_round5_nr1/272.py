#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int f[100][100];
int t;
char s[20020];
char c[20020];
int ss;
int main() {
	scanf("%d", &t);
	for (int tt = 1; tt <= t; tt++) {
		ss = 0;
		scanf("%s", s);
		int n = strlen(s);
		for (int i = 0; i < n; i++) {
			if (ss == 0 || c[ss - 1] != s[i]) {
				c[ss++] = s[i];
			} else {
				ss--;
			}
		}
		printf("Case #%d: %d\n", tt, (n - ss) / 2 * 10 + ss / 2 * 5);
	}
	return 0;
}