
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define T_MAX 100
#define S_MAX 1000

int t, smax;
int ans;

int main(void) {

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	char *s = (char *)malloc(S_MAX*2*sizeof(int));

	fscanf(fp, "%d", &t);
	for (int tc=1; tc<=t; tc++) {
		fscanf(fp, "%d %s", &smax, s);

		ans = 0;
		int stand_now = 0;
		for (int i=0; i<=smax-1; i++) {
			stand_now += s[i] - '0';
			if (stand_now < i+1) {
				ans ++;
				stand_now ++;
			}
		}

		fprintf(ofp, "Case #%d: %d\n", tc, ans);
	}

	return 0;
}