#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int T, p, l, ans;
char s[101];

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (int k = 1; k <= T; k++) {
		scanf("%s", s + 1);
		if (s[1] == '+') p = 1; else p = 0;
		l = strlen(s + 1);
		ans = 0;
		for (int i = 1; i < l; i++) if (s[i] != s[i + 1]) ans++, p ^= 1;
		if (!p) ans++;
		printf("Case #%d: %d", k, ans);
		if (k != T) printf("\n");
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}