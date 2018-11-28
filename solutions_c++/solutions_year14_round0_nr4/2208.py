#include <stdio.h>
#include <algorithm>

#define MAX_N 1000

using namespace std;

double naomi[MAX_N], ken[MAX_N];

bool cmp1(double a, double b) { return (a<b); }
bool cmp2(double a, double b) { return (a>b); }

int main() {

	int t, k;
	int n, i, j;
	int ken_p, naomi_p_wc;

	scanf("%d", &t);
	for(k=1;k<=t;k++) {
		ken_p = naomi_p_wc = 0;
		for(i=0;i<MAX_N;i++)
			naomi[i] = ken[i] = 0;
		scanf("%d", &n);
		for(i=0;i<n;i++)
			scanf("%lf", &naomi[i]);
		for(i=0;i<n;i++)
			scanf("%lf", &ken[i]);
		
		sort(naomi, naomi+n, cmp2);
		sort(ken, ken+n, cmp2);
		/*
		for(i=0;i<n;i++) printf("%lf ", naomi[i]);
		puts("");
		for(i=0;i<n;i++) printf("%lf ", ken[i]);
		puts("");
		*/
		//for(i=0;i<n && naomi[i]<ken[i]; i++)
		//	ken_p_wc++;
		i = j = 0;
		while(i<n && j<n) {
			if(naomi[i] > ken[j]) {
				naomi_p_wc++;
				i++, j++;
			}
			else j++;
		}

		sort(naomi, naomi+n, cmp1);
		sort(ken, ken+n, cmp1);
		i = j = 0;
		while(i<n && j<n) {
			if(naomi[i] < ken[j]) {
				ken_p++;
				i++, j++;
			}
			else j++;
		}

		printf("Case #%d: %d %d\n", k, naomi_p_wc, n-ken_p);
	}

	return 0;
}
