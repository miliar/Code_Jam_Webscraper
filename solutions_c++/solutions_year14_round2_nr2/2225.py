#include<stdio.h>
#include<vector>
#include<string.h>


using namespace std;

int main() {
	int T, i, j, A, B, K, a, b,buf;
	FILE* f1 = fopen("B-small-attempt1.in", "r+");
	FILE* f2 = fopen("B-small-attempt1.out", "w+");
	int count;

	fscanf(f1, "%d", &T);
	for (j = 0; j < T; j++) {
		count = 0;
		fscanf(f1, "%d %d %d", &A, &B, &K);
		
		if (K <= A && K <= B){
			count = (A + B-K)*K;
			for (a = K; a < A; a++) {
				for (b = K; b < B; b++) {
					buf = a&b;
					if (buf < K) count++;
				}
			}
		}
		else {
			count = A*B;
		}

		fprintf(f2, "Case #%d: %d\n", j + 1, count);
	}
	fclose(f1);
	fclose(f2);
	return 0;
}

