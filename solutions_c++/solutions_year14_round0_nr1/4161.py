#include <cstdio>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	scanf("%d\n", &T);
	for (int ti = 1; ti <= T; ti++) {
		int v1, v2, a1[4][4], a2[4][4];
		scanf("%d\n", &v1);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) scanf("%d", &a1[i][j]);
		scanf("%d\n", &v2);
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) scanf("%d", &a2[i][j]);
		int ans = -1, n = 0;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				if (a1[v1 - 1][i] == a2[v2 - 1][j])
					ans = a1[v1 - 1][i], n++;
		printf("Case #%d: ", ti);
		if (n == 1)
			printf("%d\n", ans);
		else if (n > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}
