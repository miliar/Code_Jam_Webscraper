#include <cstdio>
#include <cstring>

int main() {
	freopen("output.txt", "w", stdout);

	int numCase, nowCase;
	scanf("%d", &numCase);
	for (nowCase = 1; nowCase <= numCase; nowCase++) {
		printf("Case #%d: ", nowCase);

		int num;
		scanf("%d", &num);

		if (num == 0) puts("INSOMNIA");
		else {
			bool check[10];
			int cCount = 0;
			memset(check, 0, sizeof(check));

			int i;
			for (i = 0; cCount < 10;) {
				i++;
				int tmp = num * i;
				while (tmp) {
					if (check[tmp % 10] == 0) {
						check[tmp % 10] = 1;
						cCount++;
					}
					tmp /= 10;
				}
			}

			printf("%d\n", num * i);
		}
	}

	return 0;
}