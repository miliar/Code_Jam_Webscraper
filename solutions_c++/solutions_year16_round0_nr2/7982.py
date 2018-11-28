#include <cstdio>
#include <cstring>

char kek[123];
int t, n, ans;

int main()
{
	scanf("%d", &t);
	for (int ti = 1; ti <= t; ti++) {
		ans = 0; scanf("%s", kek); n = strlen(kek);
		for (int i = 1; i < n; i++) {
			if (kek[i] != kek[i-1]) ans++;
		}
		printf("Case #%d: %d\n", ti, ans + (kek[n-1] == '-'));
	}
	return 0;
}