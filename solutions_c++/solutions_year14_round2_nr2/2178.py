#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 101
#define TOL 0.000001


#define max(a,b) ((a) >= (b) ? (a) : (b))
#define min(a,b) ((a) <= (b) ? (a) : (b))

using namespace std;

char mat[N][N];



int main () {

	int t, tst, z, i, j, p, m, n, r, l, l2, c, rez, rcmin, x, y, d, k, sum, a, b;
	
	
	scanf("%d", &tst);


	for (t = 0; t < tst; t++) {
		scanf("%d %d %d", &a, &b, &k);
		
		sum = 0;
		for (i = 0; i < a; i++)
			for (j = 0; j < b; j++) 		
				if ((i&j) < k)
					sum++;
		
		printf("Case #%d: ",t+1);
		printf ("%d\n", sum);
	}
	
	return 0;

}
