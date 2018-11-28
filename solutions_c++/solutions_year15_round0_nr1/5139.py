#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 1002

char A[N];



int main(int argc, const char * argv[]) {
	
	FILE *ifp, *ofp;
	ifp = fopen(argv[1], "r");
	
	int T = 0;
	int C = 0;
	
	fscanf(ifp, "%d", &T);

	int cas			= 0;
	int minFriends	= 0;
	int currentClaping = 0;
	int temp		= 0;
	int diff		= 0;

	while (T--) {
		fscanf(ifp, "%d %s", &C, A);
		
		cas++;
		minFriends		= 0;
		currentClaping	= 0;
		temp			= A[0] - '0';
		currentClaping += temp;

		for (int i = 1; i < C + 1; i++) {

			temp = A[i] - '0';

			if (currentClaping < i) {
				diff			= i - currentClaping;
				minFriends	   += diff;
				currentClaping += diff;
			}

			currentClaping += temp;
		}

		printf("Case #%d: %d\n", cas, minFriends);
	}

	fclose(ifp);
	return 0;
}