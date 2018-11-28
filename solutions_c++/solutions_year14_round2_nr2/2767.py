#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <queue>

#include <stdio.h>
#include <ctype.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
//#include <random>
#include <time.h>

using namespace std;

int main() {
	int T;
	int A, B, K;
	int i,a,b,g;
	int x;

	scanf("%d", &T);

	for (i = 0; i < T; i++) {
		scanf("%d %d %d", &A, &B, &K);

		//printf("%d %d %d \n", A, B, K);
		g = 0;
		for (a = 0; a < A; a++) {
			for (b=0; b<B; b++) {
				x = a&b;
				if (x < K) { g++; }
				//printf("%d ", a&b);
			}
		}

	printf("Case #%d: %d\n", i+1, g);
	}
	return 0;
}