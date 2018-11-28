#include <cstdio>
#include <cstring>

int main()
{
	int T;
	scanf("%d", &T);
	for (int cases = 1; cases <= T; ++cases) {
		char s[100 + 18];
		scanf("%s", s + 1);
		int n = strlen(s + 1);
		int v = 0, ans = 0;
		for (int i = n; i; --i)
			if ((s[i] == '+') ^ v != 1) {
				v ^= 1;
				++ans;
			}
		printf("Case #%d: %d\n", cases, ans);
	}
	return 0;
}
