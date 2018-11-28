#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main(void) {

	int n_test = 0;
	int max_shyness = 0;
	char people[1010];
	int now = 0;
	int need = 0;

	FILE *fin = fopen("input.in", "r");
	FILE *fout = fopen("output.txt", "w");

	//scanf("%d", &n_test);
	fscanf(fin, "%d", &n_test);

	for(int i = 0 ; i < n_test ; i++) {

		now = 0;
		need = 0;

		//scanf("%d %s", &max_shyness, people);
		fscanf(fin, "%d %s", &max_shyness, people);

		for(int j = 0 ; j <= max_shyness ; j++) {
			if(now < j) {
				need += j - now;
				now += j - now;
			}
			now += people[j] - '0';
			//printf("j : %d\nnow : %d\nneed : %d\n", j, now, need);
		}

		//printf("Case #%d: %d\n", i + 1, need);
		fprintf(fout, "Case #%d: %d\n", i + 1, need);

	}

	fclose(fin);
	fclose(fout);

	return 0;
}