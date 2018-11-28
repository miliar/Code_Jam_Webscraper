#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 1010

int cmp(const void *a, const void *b)
{
	if(*(double *)a > *(double*)b) return 1;
	else if(*(double*)a < *(double*)b) return -1;
	return 0;
}
double naomi[N];
double ken[N];
int main()
{
	int t, i, j, k, n, j1,j2, k1,k2;
	int war, dwar;
	scanf("%d", &t);
	for(i = 1; i <= t; i++) {
		scanf("%d", &n);
		for(j = 0; j < n; j++) scanf("%lf", &naomi[j]);
		for(j = 0; j < n; j++) scanf("%lf", &ken[j]);
		qsort(naomi, n, sizeof(double), cmp);
		qsort(ken, n, sizeof(double), cmp);
//		for(j = 0; j < n; j++) printf("%lf\n", naomi[j]);
//		printf("=====\n");
//		for(j = 0; j < n; j++) printf("%lf\n", ken[j]);
		war = dwar = 0;
		war = n;
		for(j = 0, k = 0; j < n; j++) {
			while(k < n && ken[k] <= naomi[j]) k++;
			if(k < n) {
				war--;
				k++;
			}
		}
		dwar = 0;
		for(j = 0, k1 = 0, k2 = n - 1; j < n && k2 >= k1; j++) {
			if(naomi[j] > ken[k1]) {dwar++;k1++;}
			else k2--;
		} 
		printf("Case #%d: %d %d\n", i, dwar, war);
	}
	return 0;
}
