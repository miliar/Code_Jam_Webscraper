#include <cstdio>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T, C;
	scanf("%d", &T);
	C = T;
	while (C--) {
		int ansa, ansb, ans;
		int grida[5][5], gridb[5][5];

		scanf("%d", &ansa);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &grida[i][j]);

		scanf("%d", &ansb);
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				scanf("%d", &gridb[i][j]);

		ans = 0;
		for (int i = 1; i <= 4; i++)
			for (int j = 1; j <= 4; j++)
				if (grida[ansa][i] == gridb[ansb][j])
					if (ans == 0)
						ans = grida[ansa][i];
					else
						ans = -1;

		if (ans == 0)
			printf("Case #%d: Volunteer cheated!\n", T - C);
		else if (ans == -1)
			printf("Case #%d: Bad magician!\n", T - C);
		else
			printf("Case #%d: %d\n", T - C, ans);
	}
}
