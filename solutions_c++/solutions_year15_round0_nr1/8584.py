#include <cstdio>
#include <string.h>

int main() {
	//freopen("A-small-attempt1.in", "r", stdin);
	freopen("A-large.in", "r", stdin);
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t, n, count = 0, aud = 0;
	char in;
	scanf("%d", &t);
	for (int i=0; i<t; i++) {
		count = 0;
		aud = 0;
		scanf("%d", &n);
		for (int j=0; j<=n; j++) {
			scanf(" %c", &in);
			if (aud < j) {
				count+= j - aud;
				aud = j;
			}
			aud+=in-'0';
		}
		printf("Case #%d: %d\n", i+1, count);
	}
}