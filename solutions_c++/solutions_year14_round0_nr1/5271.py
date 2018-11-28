#include <stdio.h>
#include <string.h>

int c[20];

void answer()
{
	int k = 0;
	for (int i = 1; i <= 16; ++i) {
		if (c[i] == 2) {
			if (k) {
				puts("Bad magician!");
				return;
			}
			k = i;
		}
	}
	if (k) {
		printf("%d\n", k);
	} else {
		puts("Volunteer cheated!");
	}
}

int main()
{
	int dat;
	scanf("%d", &dat);
	for (int cas = 1; cas <= dat; ++cas) {
		memset(c, 0, sizeof(c));
		for (int t = 2; t--;) {
			int r;
			scanf("%d", &r);
			for (int i = 1; i <= 4; ++i) {
				for (int j = 1; j <= 4; ++j) {
					int x;
					scanf("%d", &x);
					if (r == i) ++c[x];
				}
			}
		}
		printf("Case #%d: ", cas);
		answer();
	}
}
