#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int n;
double ken[1000], nao[1000];

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		//input
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%lf", &nao[i]);
		}
		for (int i = 0; i < n; i++) {
			scanf("%lf", &ken[i]);
		}
		
		sort(nao, nao+n);
		sort(ken, ken+n);
		
		//solve
		int an = 0, ak = 0;
		int ki = 0, ni = 0;
		while (ni < n) {
			if (nao[ni] > ken[ki]) {
				an++;
				ki++;
			}
			ni++;
		}

		ni = ki = 0;
		while (ki < n) {
			if (ken[ki] > nao[ni]) {
				ak++;
				ni++;
			}
			ki++;
		}
		
		//output
		printf("Case #%d: %d %d\n", t, an, n-ak);
	}
	return 0;
}