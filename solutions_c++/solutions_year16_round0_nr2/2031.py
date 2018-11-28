#include <cstdio>
#include <cstring>

int casei, cases;
char st[110];

int main() {
	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		scanf(" %s", st);
		int len = strlen(st);
		st[len] = '+';
		int ans = 0;
		for (int i = 0; i < len; ++i)
			if (st[i] != st[i + 1]) ++ans;
		printf("Case #%d: %d\n", casei, ans);
	}
	return 0;
}
