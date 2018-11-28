#include <stdio.h>

char str[1003];
int n;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);

	for (int T = 1; T <= t; T++){
		scanf("%d %s", &n, str);
		int c = 0;
		int ans = 0;
		for (int i = 0; i <= n; i++){
			int a = str[i] - '0';
			if (c >= i)c += a;
			else{
				ans += i - c;
				c += i - c;
				c += a;
			}
		}

		printf("Case #%d: %d\n", T, ans);
	}
}