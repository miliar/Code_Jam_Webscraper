#include <cstdio>
#include <cstring>

int main()
{
	int N; 
	scanf("%d", &N);

	for (int n = 1; n <= N; n++) {
		int max; 
		scanf("%d", &max);

		char s[max + 1];
		scanf("%s", s);

		int f = 0;
		int subtotal = 0;

		for (int i = 1; i <= strlen(s); i++) {
			int d = s[i-1] - '0';

			subtotal += d;
			if (subtotal < i) {
				f += i - subtotal;
				subtotal = i;
			}
		}

		printf("Case #%d: %d\n", n, f);
	}

	return 0;
}