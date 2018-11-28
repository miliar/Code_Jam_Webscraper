#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

#define LIMIT 1024

int main()
{
	int T, N ;
	double weights1[LIMIT], weights2[LIMIT];
	int i, j, k, l;
	int naomiScore, kenScore, naomiScore1, kenScore1 ;

	scanf("%d", &T);
	for( i = 1; i <= T; i ++ ) {
		for( j = 0; j < LIMIT; j ++ ) {
			weights1[j] = 2;
			weights2[j] = 2;
		}

		scanf("%d", &N);
		for( j = 0; j < N; j ++ ) {
			scanf("%lf", &weights1[j]);
		}
		sort( weights1, weights1 + N);

		for( j = 0; j < N; j ++ ) {
			scanf("%lf", &weights2[j]);
		}
		sort( weights2, weights2 + N);

		/*
		 * First we will find out if both were playing war
		 */
		naomiScore = 0;
		kenScore = 0;
		k = 0;
		l = j - 1;
		for( j = N-1; j >= 0; j -- ) {
			if( weights1[j] > weights2[l] ) {
				naomiScore ++;
				k = k + 1;
			} else {
				kenScore ++;
				l = l - 1;
			}
		}

		/*
		 * Now we will find out if naomi is playing deceitful war
		 */
		naomiScore1 = 0;
		kenScore1 = 0;
		k = 0;
		l = j - 1;
		for( j = 0; j < N; j ++ ) {
			if( weights1[j] > weights2[k] ) {
				naomiScore1 ++;
				k ++;
			} else {
				kenScore1 ++;
			}
		}

		printf("Case #%d: %d %d\n", i, naomiScore1, naomiScore );
	}

	return 0;
}
