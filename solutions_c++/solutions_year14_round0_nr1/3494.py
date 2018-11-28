#include <cstdio>
int il [17], akt, t, temp, ret;
int main () {
	scanf ("%d", &t);
	for (int k = 1; k <= t; k ++)  {
		for (int i = 0; i < 18; i ++) il [i] = 0;
		ret = -1;
		
		for (int q = 0; q < 2; q ++) {
			scanf ("%d", &akt);
			for (int i = 1; i <= 4; i ++) {
				for (int j = 1; j <= 4; j ++) {
					scanf ("%d", &temp);
					if (i == akt) {
						il [temp] ++;
					}
				}
			}
		}
		for (int i = 1; i <= 16; i ++) {
			if (ret == -1 && il [i] == 2) ret = i;
			else if (ret != -1 && il [i] == 2) ret = -2;
		}
		if (ret == -1)      printf ("Case #%d: Volunteer cheated!\n", k);
		else if (ret == -2) printf ("Case #%d: Bad magician!\n", k);
		else                printf ("Case #%d: %d\n", k, ret);
	}
}
