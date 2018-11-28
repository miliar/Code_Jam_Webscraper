#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
using namespace std;

int r1, r2, a[10][10], b[10][10];

int main() {
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti ++) {
		printf("Case #%d: ", ti);
		scanf("%d", &r1);
		for (int i = 1; i <= 4; i ++)
			for (int j = 1; j <= 4; j ++)
				scanf("%d", &a[i][j]);
		scanf("%d", &r2);
		for (int i = 1; i <= 4; i ++)
			for (int j = 1; j <= 4; j ++)
				scanf("%d", &b[i][j]);
		int ct = 0, last_one = -1;
		for (int j = 1; j <= 4; j ++) {
			int num = a[r1][j], found = 0;
			for (int j = 1; j <= 4; j ++)
				if (b[r2][j] == num) {
					found = 1;
					last_one = num;
					break;
				}
			if (found) ct ++;
		}
		if (ct == 1) {
			printf("%d\n", last_one);
		} else 
		if (ct == 0) {
			printf("Volunteer cheated!\n");
		} else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}

