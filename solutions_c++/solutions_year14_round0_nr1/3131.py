#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 16

#define max(a,b) ((a) >= (b) ? (a) : (b))
#define min(a,b) ((a) <= (b) ? (a) : (b))

using namespace std;

int v[N+1];

int main () {

	int t, tst, x, y, z, i, j, k, p, m, n=4, r, r2;
	
	
	scanf("%d", &tst);

	for (t = 0; t < tst; t++) {
		scanf("%d", &r);
		
		memset(v, 0, sizeof(v));
		for (i = 0; i < n; i++) 
			for (j = 0; j < n; j++) {
				scanf("%d", &x);
				if (i==r-1) {
					v[x] = 1;
				}	
			}
			
			
		scanf("%d", &r2);
		k = 0;
		for (i = 0; i < n; i++) 
			for (j = 0; j < n; j++) {
				scanf("%d", &x);
				if ((i==r2-1) && v[x]){
					y = x;
					k++;
				}
			}
		
		if(!k)
			printf("Case #%d: Volunteer cheated!\n", t+1);
		else if (k==1)
			printf("Case #%d: %d\n", t+1, y);
		else
			printf("Case #%d: Bad magician!\n", t+1);
	
	}
		return 0;
	
}	
	

