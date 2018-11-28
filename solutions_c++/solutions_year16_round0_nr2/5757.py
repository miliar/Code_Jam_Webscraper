#include <cstdio>

int main() {
	freopen("output.txt", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);
	for (nowCase = 1; nowCase <= numCase; nowCase++) {
		printf("Case #%d: ", nowCase);

		char str[110];
		scanf("%s", str);

		int ans = 0;
		for (int i = 0; str[i]; i++) {
			if ((str[i+1] == 0 && str[i] != '+') || (str[i+1] != 0 && str[i+1] != str[i]))
				ans++;
		}
		printf("%d\n", ans);
	}

	return 0;
}