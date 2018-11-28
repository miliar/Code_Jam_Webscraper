#include <string.h>
#include <stdio.h>
#include <iostream>
#include <map>
#include <vector>
#include <algorithm>
#include <math.h>


#define NMAX 1001
#define N 10

#define min(a,b) ((a) <= (b) ? (a) : (b))
#define max(a,b) ((a) >= (b) ? (a) : (b))


using namespace std;

long long po[N];

int main () {
	
	int i, j, k, t, tst, f, l, fs, dim, ok, fr, nr, n, p, q;
	
	int rez;
	
	po[0] = 1;
	
	for (i = 1; i < N; i++)
		po[i] = po[i-1] << 1;
	
	scanf("%d", &tst);
	
	for (t = 0; t < tst; t++) {
	
		scanf("%d/%d", &p, &q);
		//printf("%d %d\n", p, q);
		
		l = (int)log2(q);
		
		printf("Case #%d: ",t+1);
		
		if (q != po[l]) {
			printf("Impossible\n");
		}
			
		
		else {
			k = ceil(log2((double)q/(double)p));
			printf("%d\n", k);	
		}
						
	}
	
	return 0;
}
