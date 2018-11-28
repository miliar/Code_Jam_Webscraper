#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int k = 1; k <= t; k++)
	{
		long long sum, ans = 0;
		int n, chk[11] = { 0 };
		scanf("%d", &n);

		sum = n;

		bool isfind = true;
		if (n == 0) {
			printf("Case #%d: INSOMNIA\n",k);
			isfind = false;
		}
		
		while (isfind) {
			isfind = false;
			char s[100] = { 0 };
			itoa(sum, s, 10);//정수 -> 문자열;
			int len = strlen(s);
			
			for (int i = 0; i < len; i++) {
				chk[(s[i]-'0')]++;
				bool find = false;
				for (int i = 0; i < 10; i++) {
					if (chk[i] == 0) {
						find = true;
						break;
					}
				}
				if (!find) {
					ans = sum;
					break;
				}
			}
			if (ans != 0) {
				printf("Case #%d: %lld\n", k, ans);
				break;
			}
			else isfind = true;
			sum += n;
		}

	}
	return 0;
}