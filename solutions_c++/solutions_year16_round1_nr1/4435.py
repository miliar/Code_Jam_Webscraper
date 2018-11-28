#include <stdio.h>
#include <string.h>

int main(void) {

	int t;
	int length;
	char temp1[1500] = { 0, };
	char string[1500] = { 0, };
	char dab[1500] = { 0, };
	char temp[1500] = { 0, };

	FILE *fin = fopen("A-large.in", "r");
	FILE *fout = fopen("A-large.out", "w");

	//intput T, number of testcase
	fscanf(fin, "%d", &t);
	//scanf("%d", &t);

	for (int i = 1; i <= t; i++) {
	
		string[0] = '\0';
		dab[0] = '\0';

		fscanf(fin, "%s", string);
		//scanf("%s", string);
		length = strlen(string);

		temp[0] = string[0];
		strcat(dab,temp);

		for (int i = 1; i < length; i++) {
			if (dab[0] <= string[i]) {
				temp[0] = string[i];
				strcat(temp1, temp);
				strcat(temp1, dab);
				strcpy(dab, temp1);
				temp[0] = '\0';
				temp1[0] = '\0';
			}
			else {
				temp[0] = string[i];
				strcat(dab, temp);
				temp[0] = '\0';
			}
		}

		fprintf(fout, "Case #%d:  %s\n", i, dab);
		//printf("Case # %d:  %s\n", i, dab);
	}

	fclose(fin);
	fclose(fout);
}