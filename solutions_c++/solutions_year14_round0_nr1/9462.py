#include <stdio.h>
#include <math.h>
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int a[20] = {0};

int main() {
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A-small-attempt3.out", "w", stdout);
	int x, y, z, t, j, k, fl, i, n, p, r, q, l, kol, flag, m;
	scanf("%i", &z);
	for(t = 1; t <= z; t++) {
		scanf("%i", &x);
		memset(a, 0, sizeof(a));
		for(i = 1; i <= 4; i++) {
			for(j = 1; j <= 4; j++) {
				scanf("%i", &y);
				if(i == x)
					a[y]++;
			}
		}
		scanf("%i", &x);
		for(i = 1; i <= 4; i++) {
			for(j = 1; j <= 4; j++) {
				scanf("%i", &y);
				if(i == x)
					a[y]++;
			}
		}
		fl = x = 0;
		for(i = 1; i <= 16; i++) {
			if(a[i] == 2) {
				fl++;
				x = i;
			}
		}
		if(!fl) {
			printf("Case #%i: Volunteer cheated!\n", t);
		}
		
		if(fl == 1) {
			printf("Case #%i: %i\n", t, x);
		}
		
		if(fl > 1) {
			printf("Case #%i: Bad magician!\n", t);
		}
	}

	return 0;
}