#include <cstdio>
#include <cstring>

char str[110];

int main()
{
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T; ++tt)
	{
		scanf("%s", str);
		int n = strlen(str);
		int cnt = str[n - 1] == '-';
		for (int i = 1; i < n; ++i)
			cnt += str[i] != str[i - 1];
		printf("Case #%d: %d\n", tt, cnt);
	}
	return 0;
}

