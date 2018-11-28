#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int ans1, ans2;
int can[17];

int main(void) {
	int T, x = 1;
	scanf("%d", &T);
	while (T--) {		
		scanf("%d", &ans1);
		memset(can, 0, sizeof(can));
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++) {
				int a;
				scanf("%d", &a);
				if (i == ans1)
					can[a]++;
			}

		scanf("%d", &ans2);
		for (int i = 1; i <= 4; i++) 
			for (int j = 1;j <= 4; j++) {
				int a;
				scanf("%d", &a);
				if (i == ans2)
					can[a]++;					
			}

		
		int cnt = 0, y;
		for (int i = 1; i <= 16; i++) {
			if (can[i] == 2) {
				cnt++;
				y = i;
			}
		}
		printf("Case #%d: ", x++);
		if (cnt == 0) {
			puts("Volunteer cheated!");
			continue;
		}
		if (cnt == 1) {
			printf("%d\n", y);
			continue;
		}
		puts("Bad magician!");

	}

	return 0;
}