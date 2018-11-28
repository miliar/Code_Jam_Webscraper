#include <algorithm>
#include <cmath>
#include <cstdio>
#include <memory.h>

using namespace std;

int M1[11][11], M2[11][11];

int Cnt[22];

int main(void)
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC, t = 0;
	scanf("%d", &TC);
	while (TC--) {
		int Ans1, Ans2;
		scanf("%d", &Ans1);
		for (int i = 1; i <= 4; i++) for (int j = 1; j <= 4; j++) scanf("%d", &M1[i][j]);
		scanf("%d", &Ans2);
		for (int i = 1; i <= 4; i++) for (int j = 1; j <= 4; j++) scanf("%d", &M2[i][j]);
		memset(Cnt, 0, sizeof (Cnt));
		for (int i = 1; i <= 4; i++) {
			Cnt[M1[Ans1][i]]++;
			Cnt[M2[Ans2][i]]++;
		}
		int Cnt2 = 0, Ans = -1;
		for (int i = 1; i <= 16; i++) {
			if (Cnt[i] == 2) {
				Cnt2++;
				Ans = i;
			}
		}
		if (Cnt2 == 1) printf("Case #%d: %d\n", ++t, Ans);
		else if (Cnt2 == 0) printf("Case #%d: Volunteer cheated!\n", ++t);
		else printf("Case #%d: Bad magician!\n", ++t);
	}

	return 0;
}
