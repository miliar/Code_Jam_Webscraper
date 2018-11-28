#include <cstdio>

int card() {
	int ans, card = 0, c;
	bool mark[16] = {false};

	scanf("%d", &ans);
	for (int y = 0; y < 4; ++y) {
		for (int x = 0; x < 4; ++x) {
			scanf("%d", &c);
			if (y + 1 == ans) mark[c - 1] = true;
		}
	}

	scanf("%d", &ans);
	for (int y = 0; y < 4; ++y) {
		for (int x = 0; x < 4; ++x) {
			scanf("%d", &c);
			if (y + 1 == ans && mark[c - 1]) {
				if (0 == card)
					card = c;
				else
					card = -1;
			}
		}
	}
	return card;
}

int main() {
	int n = 0;
	scanf("%d", &n);
	for (int x = 0; x < n; ++x) {
		printf("Case #%d: ", x + 1);
		int y = card();
		if (y > 0)
			printf("%d\n", y);
		else if (y == 0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
	}
	return 0;
}