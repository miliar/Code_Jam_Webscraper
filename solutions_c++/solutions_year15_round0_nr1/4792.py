#include <stdio.h>
#pragma warning(disable:4996)
FILE *in = fopen("A.in", "r");
FILE *out = fopen("A.out", "w");
char str[1111];
int main(){
	int n, len;
	fscanf(in,"%d", &n);
	for (int i = 1; i <= n; i++){
		fscanf(in,"%d", &len);
		fscanf(in,"%s", str);
		int now = 0,ans = 0;
		for (int j = 0; j <= len; j++){
			if (now < j && str[j] != '0'){
				ans = ans + j - now;
				now = j;
			}
			now = now + str[j] - '0';
		}
		fprintf(out,"Case #%d: %d\n", i, ans);
		for (int j = 0; j < len; j++){ str[j] = 0; }
	}
	return 0;
}