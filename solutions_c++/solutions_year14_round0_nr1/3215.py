#include <cstdio>
#include <cstdlib>

void solve(const int case_no) {
	int answer;
	scanf("%d", &answer);
	int dummy;
	int cards1[4];
	for(int i = 0; i < 4; i++) {
		if (i == answer-1) {
		   	scanf("%d %d %d %d", &cards1[0], &cards1[1], &cards1[2], &cards1[3]);
		}
		else scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
	}
	scanf("%d", &answer);
	int cards2[4];
	for(int i = 0; i < 4; i++) {
		if (i == answer-1) {
			scanf("%d %d %d %d", &cards2[0], &cards2[1], &cards2[2], &cards2[3]);
		}
		else scanf("%d %d %d %d", &dummy, &dummy, &dummy, &dummy);
	}
	int result = 0;
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			if (cards1[i] == cards2[j]) {
				if (result != 0) {
					printf("Case #%d: Bad magician!\n", case_no);
					return;
				}
				result = cards1[i];
			}
		}
	}
	if (result != 0) {
		printf("Case #%d: %d\n", case_no, result);
		return;
	}
	printf("Case #%d: Volunteer cheated!\n", case_no);
	return;
}

int main(int, char**) {
	int count;
	scanf("%d\n", &count);

	for(int i = 0; i < count; i++) {
		solve(i+1);
	}
	return EXIT_SUCCESS;
}
