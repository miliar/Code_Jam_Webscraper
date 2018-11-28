#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

int main(void) {
	int t, testCases;
	cin >> testCases;
	
	int N, a[1024], i, min, index, toRight, toLeft, minDist, totalDist;
	
	for (t=1; t<=testCases; t++) {
		cin >> N;
		for (i=0; i<N; i++) cin >> a[i];
		
		totalDist = 0;
		while (N) {
			min = a[0];
			index = 0;
			for (i=1; i<N; i++) if (a[i] < min) { min = a[i]; index = i; }
			toRight = index;
			toLeft = N-1-index;
			minDist = (toRight<toLeft) ? toRight : toLeft;
			
		//	for (i=0; i<N; i++) printf("%d ", a[i]); printf("\nmin %d, dist %d\n", min, minDist);
			
			totalDist += minDist;
			N--;
			for (i=index; i<N; i++) a[i] = a[i+1];
		}
		
		printf("Case #%d: ", t);
		printf("%d", totalDist);
		printf("\n");
	}
	
	
	return 0;
}