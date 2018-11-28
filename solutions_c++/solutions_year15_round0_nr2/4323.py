#include <stdio.h>
#include <math.h>

char infile[] = "B-small-attempt1.in";
char outfile[] = "out.txt";
const int AMax = 1000;
int A[AMax + 1];
int B[AMax + 1];

int main() {
	FILE* fin = fopen(infile, "rb");

	if(!fin) {
		printf("file not found\n");
		return 0;
	}

	FILE* fout = fopen(outfile, "wb");

	int T, D, k;
	fscanf(fin, "%d", &T);

	for(int i = 0; i < T; ++ i) {
		for(k = 0; k <= AMax; ++ k) {
			A[k] = 0;
		}
		int Am = 0;

		fscanf(fin, "%d", &D);

		for(int k = 0; k < D; ++ k) {
			int num;
			fscanf(fin, "%d", &num);
			A[num] ++;

			if(num > Am) {
				Am = num;
			}
		}

		int min = Am;

		for(int div = 2, dmax = sqrt((double)Am) + 1; div < dmax; ++ div) {
			int treash = Am/div + 1;
			
			for(int k = 0; k <= Am; ++ k) {
				B[k] = A[k];
			}
			
			int spend = 0;

			for(int k = Am; k > 0; --k) {
				if(B[k] > 0) {
					if(k + spend < min) {
						min = k + spend;
					}

					double splits = k / (double)treash;
					int s = (int)splits;
					if(s < splits) {
						s++;
					}

					if(s < 2) {
						s = 2;
					}

					int splited = k / s;
					int rest = k - splited * (s - 1);
					
					spend += B[k]*(s - 1);

					if(spend > min) {
						// can not do better
						break;
					} else {
						B[splited] += s - 1;
						B[rest] += 1;						
					}
				}
			}
		}			

		fprintf(fout, "Case #%d: %d\n", i + 1, min );
	}


	fcloseall();
	return 0;
}