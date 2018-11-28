#include <cstdlib>
#include <cstdio>

int main()
{
	int TC;
	scanf("%d", &TC);
	
	for (int tc = 1; tc <= TC; ++tc) {
		int C[20] = {0};
		int A1;
		scanf("%d", &A1);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int card;
				scanf("%d", &card);
				if (A1 == i + 1) ++C[card];
			}
		}
		int A2;
		scanf("%d", &A2);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				int card;
				scanf("%d", &card);
				if (A2 == i + 1) ++C[card];
			}
		}
		int checked = -1;
		int count = 0;
		for (int i = 1; i <= 16; ++i) {
			if (C[i] == 2) {
				checked = i;
				count += 1;
			}
		}
		printf("Case #%d: ", tc);
		if (count >= 2) printf("Bad magician!\n");
		else if (count == 1) printf("%d\n", checked);
		else printf("Volunteer cheated!\n");
	}
	return 0;
}
