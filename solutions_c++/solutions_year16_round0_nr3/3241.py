#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <vector>
#include <math.h>
#define MAX 10000000000000000

using namespace std;

typedef unsigned long long int64;

int64 convert(int num, int base, int jari) {
	int64 res = 0;
	int64 mul = 1;
	for (int i = 0; i < jari; i++) {
		if (1 << i & num)
			res += mul;
		mul *= base;
	}
	return res;
}

int64 getdivisor(int64 num) {
	int64 sqr = sqrt(num);
	for (int64 i = 2; i <= sqr; i++) {
		if (num % i == 0)
			return i;
	}
	return -1;
}

int main() {
	FILE* in = fopen("problem.txt", "r");
	FILE* out = fopen("solve.txt", "w");

	int T;
	fscanf(in, "%d", &T);
	for (int times = 1; times <= T; times++) {
		int N, J;
		fscanf(in, "%d %d", &N, &J	);
		int64 target = (1 << (N-1)) + 1;
		
		printf("Case #%d:\n", times);
		fprintf(out,"Case #%d:\n", times);
		while (J) {
			bool suc = true;
			int64 base[11];
			int64 div[11];
			for (int i = 2; i <= 10; i++) {
				base[i] = convert(target, i, N);
				div[i] = getdivisor(base[i]);
				if (div[i] == -1) {
					suc = false;
					break;
				}
			}
			if (suc) {
				J--;
				for (int i = N - 1; i >= 0; i--) {
					if (1 << i & target) {
						printf("1");
						fprintf(out,"1");
					}

					else {
						printf("0");
						fprintf(out, "0");
					}
				}
				for (int i = 2; i <= 10; i++) {
					printf(" %llu", div[i]);
					fprintf(out, " %llu", div[i]);
				}
					
				printf("\n");
				fprintf(out,"\n");

			}
			target+=2;
		}
		
	}
}