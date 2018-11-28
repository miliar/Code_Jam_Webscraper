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
	
	int N, capacity, i, count, available, remaining, start;
	int c[1024*16];
	int used[1024*16];
	for (t=1; t<=testCases; t++) {
		cin >> N >> capacity;
		for (i=0; i<N; i++) cin >> c[i];
		sort(&c[0], &c[N], std::greater<int>());
		
	//	for (i=0; i<N; i++) printf("%d ", c[i]); printf("\n");
		
		for (i=0; i<N; i++) used[i] = 0;
		
		count = 0;
		remaining = N;
		start = 0;
		while (remaining) {
			available = capacity;
			//first file
			for (i=start; i<N; i++) if (used[i]==0) {
				available -= c[i];
				used[i] = 1;
				remaining--;
				start = i+1;
				count++;
			//	printf("first %d, available %d\n", c[i], available);
				break;
			}
			
			//second file
			if (c[N-1] <= available) {
				for (i=start; i<N; i++) if (used[i]==0 && c[i] <= available) {
					used[i] = 1;
					remaining--;
				//	printf("second %d\n", c[i]);
					break;
				}
			}
		}
		
		
		
		printf("Case #%d: ", t);
		printf("%d", count);
		printf("\n");
	}
	
	
	return 0;
}