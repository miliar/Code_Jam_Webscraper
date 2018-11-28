#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;


int
main(void) {
    int N, A, T, n;
    int i, j, lastj, L, cons;
	long long nval;
	char M[1000001];
	char c;
    
    scanf("%d\n", &T);

    for (i = 0; i < T; i++) {
		scanf("%s %d", &M, &n);
		j = 0;
		cons = 0;
		nval = 0;
		while (M[j++] != '\0') ;
		L = j - 1;
		j = 0;
		lastj = n-1;
		while ((c = M[j++]) != '\0') {
			if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
				cons++;
			} else {
				cons = 0;
			}
			if (cons >= n) {
				nval += (long long)(j - lastj) * (long long)(L - j + 1);
				lastj = j;
			}
		}

		printf("Case #%d: %d\n", i+1, nval);
    }
}
