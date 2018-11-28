#include <cstdio>
#include <vector>

void solve(int test) {
	printf("Case #%d: ", test);
	std::vector<int> cnt(16);
	for (int iter = 0; iter < 2; iter++) {
		int x; scanf("%d", &x), x--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				int y; scanf("%d", &y), y--;
				if (i == x) cnt[y]++;
			}
		}
	}
	int index = -1;
	for (int i = 0; i < 16; i++) {
		if (cnt[i] == 2) {
			if (index != -1) {
				printf("Bad magician!\n");
				return;
			} else {
				index = i;
			}
		}
	}
	if (index == -1) {
		printf("Volunteer cheated!\n");
	} else {
		printf("%d\n", index + 1);
	}
}

int main() {
	int T; scanf("%d", &T);
	for (int test = 1; test <= T; test++) {
		solve(test);
	}
}
