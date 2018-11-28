#include <stdio.h>
#include <string.h>

int T;
int C;

int isok[10][10];
char str[2001];
int result[10];

int main(void) {
	FILE *fp;
	fopen_s(&fp, "A-large.in", "rt");
	FILE *fpp;
	fopen_s(&fpp, "output.txt", "w+");
	fscanf_s(fp, "%d", &T);
	while (T--) {
		memset(isok, 0, sizeof(isok));
		memset(result, 0, sizeof(result));
		fscanf_s(fp, "%s", str, sizeof(str));
		fprintf(fpp,"Case #%d: ", ++C);
		for (int i = 0; i < strlen(str); i++) {
			if (str[i] == 'Z') {
				result[0]++;
			}
			else if (str[i] == 'E') {

			}
			else if (str[i] == 'R') {
				result[3]++;
			}
			else if (str[i] == 'O') {
				result[1]++;
			}
			else if (str[i] == 'N') {

			}
			else if (str[i] == 'T') {

			}
			else if (str[i] == 'W') {
				result[2]++;
			}
			else if (str[i] == 'H') {
			}
			else if (str[i] == 'F') {
				result[5]++;
			}
			else if (str[i] == 'U') {
				result[4]++;
			}
			else if (str[i] == 'I') {
				result[9]++;
			}
			else if (str[i] == 'V') {
				result[7]++;
			}
			else if (str[i] == 'S') {
			}
			else if (str[i] == 'X') {
				result[6]++;
			}
			else if (str[i] == 'G') {
				result[8]++;
			}
		}
		result[3] = (result[3] - result[0]) - result[4];
		result[1] = (result[1] - result[0]) - result[2] - result[4];
		result[5] = result[5] - result[4];
		result[9] = result[9] - result[6] - result[8] - result[5];
		result[7] -= result[5];

		int j;
		for (int i = 0; i < 10; i++) 
			for (j = 0; j < result[i]; j++) 
				fprintf(fpp,"%d", i);
		fprintf(fpp,"\n");
	}
	return 0;
}