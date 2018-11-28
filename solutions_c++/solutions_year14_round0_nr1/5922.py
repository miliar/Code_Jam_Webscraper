#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <iterator>
#include <utility>
#include <list>
#include <stack>
#include <iomanip>
//#include <bitset>

#define MAX_INT 2147483647
#define MAX_LONG 9223372036854775807ll
#define MAX_ULONG 18446744073709551615ull
#define MAX_DBL 1.7976931348623158e+308
#define EPS 1e-9;

#define INF 1000000000

using namespace std;
 
int t, a1, a2, r0[4], r1[4], r2[4], i, j, k, carta, cont;

int main() {
	
	scanf("%d", &t);
	
	for (i=1; i<=t; i++) {
		
		scanf("%d", &a1);
		
		for (j=1; j<=4; j++) {
			if (j == a1) {
				scanf("%d %d %d %d", &r1[0], &r1[1], &r1[2], &r1[3]);
			} else {
				scanf("%d %d %d %d", &r0[0], &r0[1], &r0[2], &r0[3]);
			}
		}
		
		scanf("%d", &a2);
		
		for (j=1; j<=4; j++) {
			if (j == a2) {
				scanf("%d %d %d %d", &r2[0], &r2[1], &r2[2], &r2[3]);
			} else {
				scanf("%d %d %d %d", &r0[0], &r0[1], &r0[2], &r0[3]);
			}
		}
		
		cont = 0;
		for (j=0; j<4; j++) {
			for (k=0; k<4; k++) {
				if (r1[j] == r2[k]) {
					cont++;
					carta = r1[j];
				}
			}
		}
		
		if (cont == 1) {
			printf("Case #%d: %d\n", i, carta);
		} else if (cont == 0) {
			printf("Case #%d: Volunteer cheated!\n", i);
		} else {
			printf("Case #%d: Bad magician!\n", i);
		}
		
	}
	
	
	return 0;
}