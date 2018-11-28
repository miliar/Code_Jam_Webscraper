#include <stdio.h>
#include <string.h>
int main(void) {
	int n,i = 0,j;
	int t;
	char temp;
	char input[200];
	int cnt;
	FILE *fp;
	fopen_s(&fp, "B-large.in", "rt");
	FILE *fpp;
	fopen_s(&fpp,"output.txt", "w+");
	fscanf_s(fp,"%d", &t);
	for (int j = 1; j <= t; j++) {
		cnt = 1;
		memset(input, 0, sizeof(input));
		fscanf_s(fp, "%s", &input, sizeof(input));
		temp = input[0];
		for (i = 1; i < strlen(input); i++) {
			if (temp != input[i]) {
				cnt++;
				temp = input[i];
			}
		}
		if (input[i - 1] == '+') {
			cnt--;
		}
		fprintf(fpp,"Case #%d: %d\n", j, cnt);
	}
	return 0;
}