#include <bits/stdc++.h>

using namespace std;

char s[10000];
int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++) {
		int n, tot = 0, need = 0;
		scanf("%d %s", &n, &s);
		for (int i = 0; i <= n; i++) {
			if (tot < i)
				need += i - tot, tot = i;
			tot += (s[i] - '0');
		}
		printf("Case #%d: %d\n", T, need);
	}
	return 0;
}
