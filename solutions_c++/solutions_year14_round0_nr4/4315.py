#include <cstdio>
#include <cstring>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
	if (*(double*)a > *(double*)b) return 1;
	else return -1;
}

int main() {
	freopen("in.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int n, start_war, start_cheat, win1, win2;
	double naomi[1000], ken[1000];
	int t;
	scanf("%d", &t);
	for (int a=0; a<t; a++) {
		scanf("%d", &n);
		memset(naomi, 0, sizeof(naomi));
		memset(ken, 0, sizeof(ken));
		start_war = 0;
		start_cheat = 0;
		for (int i=0; i<n; i++) {
			scanf("%lf", &naomi[i]);
		}
		for (int i=0; i<n; i++) {
			scanf("%lf", &ken[i]);
		}
		win1 = 0;
		win2 = n;
		qsort(naomi, n, sizeof(double), cmp);
		qsort(ken, n, sizeof(double), cmp);
		
		for(int i=0; i<n; i++) {
			for (int j=start_cheat; j<n; j++) {
				if (ken[i] < naomi[j]){
					start_cheat = j+1;
					win1++;
					break;
				}
			}
			for (int j=start_war; j<n; j++) {
				if (ken[j] > naomi[i]) {
					start_war = j+1;
					win2-=1;
					break;
				}
			}
		}
		printf("Case #%d: %d %d\n", a+1, win1, win2);
	}
}
