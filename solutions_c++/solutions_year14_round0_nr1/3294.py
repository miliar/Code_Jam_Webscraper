#include <stdio.h>
#include <string.h>

int poss[20];

int main() {
	int T;
	scanf(" %d", &T);
	for (int _42 = 1; _42 <= T; _42++) {
		memset(poss, 0, sizeof(poss));
		int q1, q2;
		scanf(" %d", &q1);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int a;
				scanf(" %d ", &a);
				if (i == q1)
					poss[a]++;
			}
		}
		scanf(" %d", &q2);
		for (int i = 1; i <= 4; i++) {
			for (int j = 1; j <= 4; j++) {
				int a;
				scanf(" %d ", &a);
				if (i == q2)
					poss[a]++;
			}
		}

		int c2 = 0, ans;
		for (int i = 1; i <= 16; i++) {
			if (poss[i] == 2) {
				c2++;
				ans = i;
			}
		}
		
		if (c2 == 0) {
			printf("Case #%d: Volunteer cheated!\n", _42);
		}
		else if (c2 == 1) {
			printf("Case #%d: %d\n", _42, ans);
		}
		else {
			printf("Case #%d: Bad magician!\n", _42);
		}
	}
	return 0;
}