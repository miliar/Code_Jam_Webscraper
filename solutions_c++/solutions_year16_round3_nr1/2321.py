#include <cstdio>

using namespace std;

int main() {
	int testcases;
	int nparties;
	int nsenators;
	
	int parties[30];
	
	scanf("%d", &testcases);
	
	for(int t = 1; t <= testcases; ++t) {
		scanf("%d", &nparties);
		
		nsenators = 0;
		for(int i = 0; i < nparties; ++i) {
			scanf("%d", &parties[i]);
			nsenators += parties[i];
		}
		
		printf("Case #%d:", t);
		while(nsenators > 0) {
			// Find max two?
			int maxa = 0;
			int maxaidx = 0, maxbidx = -1;
			int nmax = 0;
			
			for(int i = 0; i < nparties; ++i) {
				if(maxa < parties[i]) {
					maxa = parties[i];
					
					maxaidx = i;
					maxbidx = -1;
					nmax = 1;
				}
				else if(maxa == parties[i]) {
					maxbidx = i;
					nmax++;
				}
			}
			
			parties[maxaidx]--;
			nsenators--;
			
			printf(" %c", maxaidx + 'A');
			
			if(maxbidx != -1 && nmax <= 2) {
				parties[maxbidx]--;
				nsenators--;
				printf("%c", maxbidx + 'A');
			}
		}
		printf("\n");
	}

	return 0;
}