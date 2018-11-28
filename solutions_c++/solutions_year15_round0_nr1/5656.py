#include <stdio.h>
FILE *in, *out;
#pragma warning(disable:4996)
int main(){
	out = fopen("1.out", "w");
	int c, n;
	int a[2000];
	char s[2000];
	int sum,sigma;
	scanf("%d", &c);
	for (int i = 0; i < c; i++){
		scanf("%d", &n);
		sum = 0;
		sigma = 0;
		scanf("%s", s);
		for (int j = 0; j < n; j++){
			a[j] = s[j] - '0';
			sigma += a[j];
			if (sigma < j + 1){
				sum += (j + 1 - sigma);
				sigma += (j + 1 - sigma);
			}
		}
		fprintf(out,"Case #%d: %d\n", i+1, sum);
	}
	return 0;
}