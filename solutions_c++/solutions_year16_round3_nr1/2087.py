#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
struct po {
	int id, num;
} a[110];
bool cmp(po x, po y) {
	return x.num > y.num;
}
int main() {
	int T, p;
	int cas = 1;
	scanf("%d", &T);
	while (T--) {
		int sum = 0;
		memset(a, 0, sizeof(a));
		printf("Case #%d:", cas++);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i].num);
			sum += a[i].num;
			a[i].id = i;
		}
		sort(a, a + n, cmp);
		while (sum > 1) {
			int u = a[0].id;
			if (a[0].num > 1) {
				a[0].num -= 2;
				sort(a, a + n, cmp);
				if (a[0].num * 2 <= (sum - 2)) {
					printf(" %c%c", u + 'A', u + 'A');
					sum -= 2;
					continue;
				} else {
					for (int i = 0; i < n; i++) {
						if (u == a[i].id) {
							a[i].num += 2;
							break;
						}
					}
				}
			}
			sort(a, a + n, cmp);
			if (a[1].num > 0) {
				int q1 = a[0].id, q2 = a[1].id;
				a[0].num--;
				a[1].num--;
				sort(a, a + n, cmp);
				if (a[0].num * 2 <= (sum - 2)) {
					printf(" %c%c", q1 + 'A', q2 + 'A');
					sum -= 2;
					continue;
				} else {
					for (int i = 0; i < n; i++) {
						if (q1 == a[i].id || q2 == a[i].id) {
							a[i].num++;
						}
					}
					sort(a, a + n, cmp);
				}
			}
			int y = a[0].id;
			a[0].num--;
			printf(" %c", y + 'A');
			sum--;
			sort(a, a + n, cmp);
		}
		sort(a, a + n, cmp);
		if (sum == 1) {
			printf(" %c\n", a[0].id + 'A');
		} else
			printf("\n");
	}
	return 0;
}
