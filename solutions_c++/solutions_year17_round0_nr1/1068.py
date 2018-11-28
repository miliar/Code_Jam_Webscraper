#include<stdio.h>
#include<string.h>
char b[2000];
int l;
FILE *in = fopen("A-large.in", "r");
FILE *out = fopen("output.txt", "w");
int main() {
	int n,m,j,k,cnt;
	fscanf(in,"%d", &n);
	for (int i = 1; i<=n; i++) {
		cnt = 0;
		fscanf(in,"\n%s %d", b, &m);
		l = strlen(b);
		for (j = 0; j <= l-m; j++) {
			if (b[j] == '-') {
				for (k = j; k < j + m; k++) {if (b[k] == '-') b[k] = '+'; else b[k] = '-';}
				cnt++;
			}
		}
		for (j = l - m + 1; j < l; j++) { if (b[j] == '-') break; }
		if (j == l) fprintf(out,"Case #%d: %d\n", i, cnt); else fprintf(out,"Case #%d: IMPOSSIBLE\n", i);
	}
	return 0;
}