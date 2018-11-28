#include <stdio.h>
#include <algorithm>
using namespace std;

int biggest(double a, double * v, int n);

int main() {
	int t;
	scanf("%d", &t);
	
	int n;
	double naomi[1010], ken[1010];
	
	for(int test=1; test<=t; test++) {
		scanf("%d", &n);
		for(int i=0; i<n; i++) {
			scanf("%lf", &naomi[i]);
		}
		for(int i=0; i<n; i++) {
			scanf("%lf", &ken[i]);
		}
		
		sort(naomi, naomi+n);
		sort(ken, ken+n);
		
		int decei = 0, j = 0;
		for(int i=0; i<n; i++) {
			if(naomi[i] > ken[j]) {
				decei++;
				j++;
			} else {
				// nothing
			}
		}
		
		int normal = 0;
		for(int i=0; i<n; i++) {
			if(biggest(naomi[i], ken, n)) {
				normal++;
			}
		}
		printf("Case #%d: %d %d\n", test, decei, normal);
	}
}

int biggest(double a, double * v, int n) {
	for(int i=0; i<n; i++) if(v[i] != -1 && v[i] > a) {
		v[i] = -1;
		return false;
	}
	return true;
}
