#include<stdio.h>

int main() {
	int t, s, arr[1001];
	char str[1002];

	scanf("%d", &t);

	for (int i = 0; i < t; ++i) {
		scanf("%d", &s);
		scanf("%s", str);

		for (int j = 0; str[j] != '\0'; ++j) {
			arr[j] = str[j] - 48;
		}

		int st = 0, rq = 0, req;

		for (int j = 0; j <= s; ++j) {
			if (j <= st) {
				st = st + arr[j];
			} else {
				req = j - st;
				st = st + arr[j] + req;
				rq = rq + req;
			}
		}

		printf("Case #%d: %d\n", i + 1, rq);
	}
}
