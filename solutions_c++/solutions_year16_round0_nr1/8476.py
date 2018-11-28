#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main() {
	int t, n;
	freopen("A-large.in", "r", stdin);
	freopen("a.out", "w", stdout);
	scanf("%d", &t);
	for (int a = 1; a <= t; a++) {
		scanf("%d", &n);
		printf("Case #%d: ", a);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		int cnt = 0, ok = 0;
		int arr[11] = { 0, };
		for (int i = 1; ; i++) {
			int now = n * i;
			int tmp = now;
			while (now > 0) {
				if (arr[now % 10] == 0) {
					arr[now % 10] = 1;
					cnt++;
				}
				now /= 10;
				if (cnt == 10) {
					printf("%d\n", tmp);
					ok = 1;
					break;
				}
			}
			if (ok) break;
		}
	}
	fclose(stdin);
	fclose(stdout);
}
