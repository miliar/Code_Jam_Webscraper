#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <iostream>
#include <string.h>
#include <math.h>
using namespace std;

#define SIZE 10001
#define __i 2
#define __j 3
#define __k 4


int mult(int i, int j) {
	int sign = 1;
	if (i * j < 0) {
		sign = -1;
	}
	switch (abs(i)) {
	case 1:
		switch (abs(j)) {
			case 1:
				return 1 * sign;
			case __i:
				return __i * sign;
			case __j:
				return __j * sign;
			case __k:
				return __k * sign;
		}
	case __i:
		switch (abs(j)) {
			case 1:
				return __i * sign;
			case __i:
				return -1 * sign;
			case __j:
				return __k * sign;
			case __k:
				return -1 *__j * sign;
		}
	case __j:
		switch (abs(j)) {
			case 1:
				return __j * sign;
			case __i:
				return -1 * __k * sign;
			case __j:
				return -1 * sign;
			case __k:
				return __i * sign;
		}
	case __k:
		switch (abs(j)) {
			case 1:
				return __k * sign;
			case __i:
				return __j * sign;
			case __j:
				return -1 * __i * sign;
			case __k:
				return -1 * sign;
		}
	default:
		return -200;
	
	}
}



int calc_string(char * s, int i, int j, int len) {
	int s1 = s[0] - 'i' + 2;
	int s2 = s[i + 1] - 'i' + 2;
	int s3 = s[j + 1] - 'i' + 2;
	for (int i1 = 1; i1 <= i; ++i1) {
		s1 = mult(s1, s[i1] - 'i' + 2);
	}
	for (int i1 = i + 2; i1 <= j; ++i1) {
		s2 = mult(s2, s[i1] - 'i' + 2);
	}
	for (int i1 = j + 2; i1 <= len - 1; ++i1) {
		s3 = mult(s3, s[i1] - 'i' + 2);
	}
	if (s1 == __i && s2 == __j && s3 == __k) {
		return 1;
	} else {
		printf("%d %d failed: %d %d %d\n", i, j, s1, s2, s3);
		return 0;
	}
}

int main(void) {
	FILE * iff = fopen("in", "r");
	FILE * off = fopen("out", "w");
	int L, X;
	int T;

	fscanf(iff, "%d", &T);

	char **matrix = (char**)malloc(SIZE * sizeof(char*));
	for (int i = 0; i < SIZE; ++i ) {
		 matrix[i] = (char*)malloc( SIZE * sizeof(char));
	}
	for (int cse = 1; cse <= T; ++cse) {
		// printf("--------------------------------------------------------%d\n",cse);
		
		fscanf(iff, "%d %d", &L, &X);
		char s[SIZE];
		char s_cpy[SIZE];
		fscanf(iff,"%s",s);
		strcpy(s_cpy, s);
		for (int i = 1; i < X; ++i) {
			strcat(s, s_cpy);
		}
		int ok = 0;
		for (int k = 1; k <= L * X ; ++k) {
			matrix[k][k] = s[k - 1] - 'i' + 2;
			for (int i = k + 1; i <= L * X ; ++i) {
				matrix[k][i] = mult(matrix[k][i - 1], s[i - 1] - 'i' + 2);

			}
		}
		// printf("SIZES: %d\n",L * X);
		// for (int k = 1; k <= L * X; ++k) {
		// 	for (int i = 1; i <= L * X ; ++i) {
		// 		printf("%d ",matrix[k][i]);
		// 	}
		// 	printf("\n");
		// }


		for (int k = 1; k <= L * X - 2; ++k) {
			for (int i = k + 1; i <= L * X - 1 ; ++i) {
				if (matrix[1][k] == __i && matrix[k + 1][i] == __j && matrix[i + 1][L * X] == __k) {
					fprintf(off,"Case #%d: YES\n",cse);
					ok = 1;
					break;
				} else {
					// printf("%d %d failed: %d %d %d\n", k, i, matrix[1][k], matrix[k + 1][i], matrix[i + 1][L * X]);
				}
				if (ok == 1) {
					break;
				}
			}
			if (ok == 1) {
				break;
			}
		}
		
		// for (int i = 0; i < L * X - 2; ++i) {
		// 	for (int j = i + 1 ; j < L * X - 1; ++j) {
		// 		if (calc_string(s, i, j, L * X) == 1) {
		// 			fprintf(off,"Case #%d: YES\n",cse);
		// 			ok = 1;
		// 			break;
		// 		}
		// 		if (ok == 1) {
		// 			break;
		// 		}
		// 	}
		// 	if (ok == 1) {
		// 		break;
		// 	}
		// }
		if (ok == 0) {
			fprintf(off,"Case #%d: NO\n",cse);
		}
		 
	}
	
	

	
	
	fclose(iff);
	fclose(off);
	return 0;
}