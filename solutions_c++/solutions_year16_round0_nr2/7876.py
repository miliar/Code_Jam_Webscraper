#include <stdio.h>
#include <string.h>

//int check[15];
int check [110];

void flip(int si, int checking) {

	for (int i = 0; i <= si; i++) {
		check[i] = checking;
	}
}

int flipPancake(int si, int fi, int checking, int& dab) {

	//end recursive
	if (si == fi) {
		if (check[fi] == 0) {
			dab++;
			return dab;
		}
		else  return dab;
	}

	//for recursive
	for (int i = si; i <= fi; i++) {
		if (check[i] != checking) {
			si = i;
			checking = check[i];
			break;
		}

		if (i == fi) {
			if (check[i] == 0)	return ++dab;
			else return dab;
		}

	}

	dab++;
	flip(si-1, checking);
	dab = flipPancake(si,fi,checking, dab);

	return dab;

}

int main(void)
{
	int t, n, checking, dab;
	//char small[15];
	char large[110];

	FILE *fin = fopen("B-large.in", "r");
	FILE *fout = fopen("B-large.out", "w");
	fscanf(fin, "%d", &t);
	//scanf("%d", &t);

	for (int i = 1; i <= t; i++) {

		dab = 0;
		fscanf(fin, "%s", large);
		//scanf("%s", small);

		n = strlen(large);	//string length

		for (int i = 0; i < n; i++) {
			if (large[i] == '-')	check[i] = 0;
			else if (large[i] == '+')	check[i] = 1;
		}

		checking = check[0];
		flipPancake(0, n - 1, checking, dab);

		fprintf(fout, "Case #%d:  %d\n", i, dab);
		//printf("Case # %d:  %d\n", i, dab);

		strcpy(large, "");
	}

	fclose(fin);
	fclose(fout);

}