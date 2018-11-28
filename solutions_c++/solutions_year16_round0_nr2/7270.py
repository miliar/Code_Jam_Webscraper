#include <stdio.h>
#include <string.h>

int main() {
	int T, i, j, k, cnt;
	char Pancake[150];

	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("out.txt", "w");

	fscanf(fin,"%d", &T);
	for (i = 1;i <= T;i++) {
		cnt = 0;
		for (j = 0;j < 150;j++)
			Pancake[j] = 0;
		fscanf(fin,"%s", Pancake);

		for (j = strlen(Pancake)-1;j >= 0;j--) {
			if (Pancake[j] == '-') {
				for (k = 0;k <= j;k++) {
					if (Pancake[k] == '-')
						Pancake[k] = '+';
					else
						Pancake[k] = '-';
				}
				cnt++;
			}
		}
		fprintf(fout,"Case #%d: %d\n",i, cnt);
	}
	return 0;
}