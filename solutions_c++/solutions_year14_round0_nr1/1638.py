#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int mag[4][4], row[4];

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int i, j, m, n, r, t;
	scanf("%d", & t);
	for (int c = 0; c < t; c++) {
		scanf("%d", & r);
		r--;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				scanf("%d", & mag[j][i]);
		for (i = 0; i < 4; i++)
			row[i] = mag[i][r];
		scanf("%d", & r);
		r--;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				scanf("%d", & mag[j][i]);
		m = 0;
		n = -1;
		for (i = 0; i < 4; i++) {
			for (j = 0; j < 4; j++) {
				if (row[i] == mag[j][r]) {
					m++;
					n = row[i];
				}
			}
		}
		printf("Case #%d: ", c + 1);
		if (m == 0)
			printf("Volunteer cheated!\n");
		else if (m == 1)
			printf("%d\n", n);
		else printf("Bad magician!\n");
	}
	return 0;
}


