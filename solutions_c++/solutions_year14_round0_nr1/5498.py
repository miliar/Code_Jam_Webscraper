#include <iostream>
#include <stdio.h>
using namespace std;
int a[20];
int main() {
	int i, j;
	int t, cas = 0;
	int n, x;
	scanf("%d", &t);
	while (t--) {
		cas++;
		memset(a, 0, sizeof(a));
		scanf("%d", &n);
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i == n - 1)
					a[x]++;
			}
		}
		scanf("%d", &n);
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				scanf("%d", &x);
				if (i == n - 1)
					a[x]++;
			}
		}
		int cnt, id;
		cnt = 0;
		for (i = 1; i <= 16; ++i) {
			if (a[i] == 2) {
				id = i;
				cnt++;
			}
		}
		printf("Case #%d: ", cas);
		if (cnt == 0)
			puts("Volunteer cheated!");
		else if (cnt > 1)
			puts("Bad magician!");
		else
			printf("%d\n", id);

	}
}
