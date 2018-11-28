#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fp, *fw;

int main() {
	fp = fopen("D:\\GCJ\\A-large.in", "r");
	fw = fopen("D:\\GCJ\\outAL.txt", "w");
	int cse, i, g = 1, smax, cur, res;
	char str[1010];
	fscanf(fp, "%d", &cse);
	while(cse--) {
		fscanf(fp, "%d %s", &smax, str);
		cur = 0;
		res = 0;
		for(i = 0; i < smax + 1; ++i) {
			if (cur >= i) {
				cur += str[i] - '0';
			}
			else {
				res += i - cur;
				cur = i + str[i] - '0';
			}
		}
		fprintf(fw, "Case #%d: %d\n", g++, res);
	}
	fclose(fp);
	fclose(fw);
	return 0;
}
