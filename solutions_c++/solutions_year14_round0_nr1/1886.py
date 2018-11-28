#include <cstdio>
using namespace std;
unsigned short shown = 0;
int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		shown = 0;
		int r, card, ans = 0;
		scanf("%d", &r);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &card);
				if (i == r)
					shown |= 1 << (card-1);
			}
		scanf("%d", &r);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				scanf("%d", &card);
				if (i == r && ((shown & (1<<(card-1))) > 0))
					if (ans == 0)
						ans = card;
					else
						ans = -1;
			}
		printf("Case #%d: ", t);
		if (ans == 0)
			printf("Volunteer cheated!\n");
		else if (ans == -1)
			printf("Bad magician!\n");
		else
			printf("%d\n", ans);
	}
	return 0;
}

