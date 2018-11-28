#include <stdio.h>

int cases, kejs;
int i, j, a1, a2;
int a[4][4], b[4][4];
bool has[17], cheat, bad;

int main() {
    scanf("%d", &cases);
    for (kejs = 1; kejs <= cases; kejs++) {
        printf("Case #%d: ", kejs);
        scanf("%d", &a1);
				for (i = 1; i <= 16; i++) has[i] = false;
				for (i = 0; i < 4; i++) {
					scanf("%d%d%d%d", &a[i][0], &a[i][1], &a[i][2], &a[i][3]);
					if (i+1 == a1) {
						has[a[i][0]] = 
						has[a[i][1]] = 
						has[a[i][2]] = 
						has[a[i][3]] = true; 
					}
				}
				j = 0;
				cheat = true;
				bad = false;
        scanf("%d", &a2);
				for (i = 0; i < 4; i++) {
					scanf("%d%d%d%d", &b[i][0], &b[i][1], &b[i][2], &b[i][3]);
					if (i+1 == a2) {
						for (int k = 0; k < 4; k++) {
							if (has[b[i][k]]) {
								cheat = false;
								if (j == 0) {
									j = b[i][k];
								} else {
									bad = true;
								}
							}
						}
					}
				}

        if (bad) printf("Bad magician!\n");
				else if (cheat) printf("Volunteer cheated!\n");
        else printf("%d\n", j);
    }
    return 0;
}
