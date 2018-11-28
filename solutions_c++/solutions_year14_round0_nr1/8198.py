#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int TT;
	scanf("%d", &TT);
	for (int T = 1; T <= TT; T++) {

		int a;
		int x[17] = { 0 };
		scanf("%d", &a);
		for (int i = 0; i < 16; i++) {
			int v;
			scanf("%d", &v);
			if (i / 4 == a - 1)
				x[v]++;
		}
		scanf("%d", &a);
		for (int i = 0; i < 16; i++) {
			int v;
			scanf("%d", &v);
			if (i / 4 == a - 1)
				x[v]++;
		}
		int ret = 0;
		int cnt = 0;
		for (int i = 1; i <= 16; i++) {
			if (x[i] == 2) {
				cnt++;
				ret = i;
			}
		}
		printf("Case #%d: ", T);
		if (cnt == 1)
			printf("%d\n", ret);
		else if (cnt ==0)
			printf("Volunteer cheated!\n", ret);
		else
			printf("Bad magician!\n", ret);
	}
}