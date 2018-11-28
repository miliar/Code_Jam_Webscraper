#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int count;
	char number;
} PARTY;

PARTY parties[30];

int compare(const void *a, const void *b) {
	PARTY *t1, *t2;
	t1 = ((PARTY*)a);
	t2 = ((PARTY*)b);

	return (t2->count - t1->count);
}

int main() {
	int T;

	scanf("%d", &T);

	for(int i = 1; i <= T; i++) {
		int n, total = 0;

		scanf("%d", &n);

		for(int j = 0; j < n; j++) {
			scanf("%d", &parties[j].count);

			total += parties[j].count;
			parties[j].number = 'A'+j;
		}

		printf("Case #%d: ", i);

		while(total > 0) {
			qsort(parties, n, sizeof(PARTY), compare);

			printf("%c", parties[0].number);
			parties[0].count--;
			total--;

			qsort(parties, n, sizeof(PARTY), compare);

			if(parties[0].count < parties[1].count && (parties[1].count-1) <= ((total-1)/2)) {
				printf("%c", parties[1].number);
				parties[1].count--;
				total--;
			}
			else if(parties[0].count > parties[1].count && (parties[0].count-1) <= ((total-1)/2)) {
				printf("%c", parties[0].number);
				parties[0].count--;
				total--;
			}
			else if(parties[0].count > 0 && parties[0].count == parties[1].count && parties[1].count <= ((total-1)/2)) {
				printf("%c", parties[0].number);
				parties[0].count--;
				total--;
			}

			printf(" ");
		}
		printf("\n");
	}

	return 0;
}