#include <cstdio>

FILE* in = fopen("o.in", "r");
FILE* out = fopen("o.out", "w");

int nCases;

int main() {
	fscanf(in, "%d", &nCases);
	for (int i=0; i<nCases; i++) {
		int n;
		fscanf(in, "%d ", &n);
		int total = 0, nFriends = 0;
		for (int j=0; j<=n; j++) {
			char c;
			fscanf(in, "%c", &c);
			if (total < j) {
				nFriends += j-total;
				total = j;
			}
			int m = c-'0';
			//printf("%d\n", nFriends);
			total += m;
		}
		//printf("\n");

		fprintf(out, "Case #%d: %d\n", i+1, nFriends);
	}
}