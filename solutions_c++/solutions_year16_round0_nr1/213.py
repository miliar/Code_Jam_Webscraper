#include<stdio.h>

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++) {
		int N;
		scanf("%d", &N);
		if (N == 0) {
			printf("Case #%d: INSOMNIA\n", t);
		} else {
			bool s[10] = {false};
			int c = N;
			while (true) {
				int d = c;
				while (d > 0) {
					s[d%10] = true;
					d /= 10;
				}
				bool f = false;
				for (int i=0; i<10; i++) {
					if (!s[i]) {
						f = true;
						break;
					}
				}
				if (!f) {
					break;
				}
				c += N;
			}
			printf("Case #%d: %d\n", t, c);
		}
	}
	return 0;
}