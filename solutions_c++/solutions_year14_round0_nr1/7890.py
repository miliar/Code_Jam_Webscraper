#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<vector>
using namespace std;
int ar1[5], ar2[5];
int main() {
	int t;
	scanf("%d", &t);
	for (int kase = 1; kase <= t; kase++) {
		int r1, r2;
		scanf("%d", &r1);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int x;
				scanf("%d", &x);
				if (i == r1) {
					ar1[j] = x;
				}
			}
		}
		scanf("%d", &r2);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int x;
				scanf("%d", &x);
				if (i == r2) {
					ar2[j] = x;
				}
			}
		}

		int ans = -1;
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				if (ar1[i] == ar2[j]) {
					if (ans == -1) {
						ans = ar1[i];
					} else {
						ans = 17;
					}
				}
			}
		}
		printf("Case #%d: ", kase);
		if (ans == -1) {
			printf("Volunteer cheated!\n");
		} else if (ans == 17) {
			printf("Bad magician!\n");
		} else {
			printf("%d\n", ans);
		}
	}
	return 0;
}
