#define MAXN 16

#include <cstdio>
#include <cstring>

using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	scanf("%d", &t);

	int m1[MAXN][MAXN];
	int m2[MAXN][MAXN];

	for (int c = 1; c <= t; c++) {
		int a, b;
		
		scanf("%d", &a);
		a--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &(m1[i][j]));
			}
		}
		scanf("%d", &b);
		b--;
		for (int i = 0; i < 4; i++) {
			for (int j = 0; j < 4; j++) {
				scanf("%d", &(m2[i][j]));
			}
		}

		int check[16 + 1];
		memset(check, 0, sizeof(check));

		for (int i = 0; i < 4; i++) {
			check[m1[a][i]]++;
			check[m2[b][i]]++;
		}

		int count = 0;
		int index = 0;
		for (int i = 1; i <= 16; i++) {
			if (check[i] == 2) {
				count++;
				index = i;
			}
		}

		if (count == 0) {
			printf("Case #%d: Volunteer cheated!\n", c);
		} else if (count == 1) {
			printf("Case #%d: %d\n", c, index);
		} else {
			printf("Case #%d: Bad magician!\n", c);
		}
	}

	return 0;
}