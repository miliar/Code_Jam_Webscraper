#include <cstdio>

//#define SMALL
#define LARGE

int t;
char s[105];

int solve() {
	char *p = s;
	int ret = 0, add = 0;
	while (*p) {
		if (*p == '+') {
			add = 1;
		} else {
			while (*p && *p == '-')
				++p;
			ret += 1 + add;
			add = 1;
		}
		if (!*p)
			break;
		++p;
	}
	return ret;
}

int main()
{
#ifdef SMALL
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
#endif
#ifdef LARGE
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
#endif

	scanf("%d", &t);
	for (int Case = 1; Case <= t; ++Case) {
		scanf("%s", s);
		printf("Case #%d: %d\n", Case, solve());
	}
	return 0;
}
