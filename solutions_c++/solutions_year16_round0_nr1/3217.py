#pragma warning(disable:4996)
#include <stdio.h>

int check[10];
int count;

int main() {
	int ts, n;
	long long num, temp, ans;
	FILE *wfp;

	wfp = fopen("output.txt", "w");

#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
#endif

	scanf("%d", &ts);

	for (int t = 1; t <= ts; t++) {
		for (int i = 0; i < 10; i++)
			check[i] = 0;
		count = 0;

		scanf("%d", &n);
		num = n;

		if (num == 0) {
			ans = 0;
		}
		else {
			int tmp;
			for (int i = 1; i <= 100; i++) {
				ans = i * num;
				while (ans > 0) {
					tmp = ans % 10;
					ans /= 10;
					if (check[tmp] == 0) {
						count++;
						check[tmp] = 1;
					}
				}
				if (count == 10) {
					ans = i * num;
					break;
				}
			}

			if (count != 10)
				ans = -1;
		}

		if (ans == 0) {
			fprintf(wfp, "Case #%d: %s\n", t, "INSOMNIA");
		}
		else 
			fprintf(wfp, "Case #%d: %lld\n", t, ans);
	}

	fclose(wfp);

	return 0;
}