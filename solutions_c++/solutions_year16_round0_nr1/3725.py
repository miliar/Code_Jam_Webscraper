#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <algorithm>


using namespace std;

int arr[100];
int n[7];


int main() {
	FILE* in = fopen("problem.txt", "r");
	FILE* out = fopen("solve.txt", "w");
	int T;
	int A = 0;
	fscanf(in, "%d", &T);
	while (T >= ++A ) {
		int N;
		fscanf(in, "%d", &N);
		if (N == 0) {
			fprintf(out, "Case #%d: INSOMNIA\n", A);
			continue;
		}
		for (int i = 0; i < 100; i++)
			arr[i] = 0;
	
		int N_jari = 0;
		for (int i = 0; i < 7; i++)
			n[i] = 0;
		for (int i = 0; i < 7; i++) {
			n[i] = N % 10;
			N /= 10;
			if (N <= 0) {
				N_jari = i;
				break;
			}
		}

		int lim = INT_MAX;
		int jari = N_jari;
		int used = 0;
		int target = (1 << 10) - 1;
		while (lim--) {
			int add=0,i  = 0;
			for (i = 0; i <= jari || add > 0; i++) {
				arr[i] += n[i] + add;
				if (arr[i] >= 10) {
					arr[i] -= 10;
					add = 1;
				}
				else
					add = 0;
				used = used | (1 << arr[i]);
			}
			jari = max(i-1, jari);
			if (used == target) {
				fprintf(out, "Case #%d: ", A);
				for (int i = jari; i >= 0; i--)
					fprintf(out, "%d", arr[i]);
				fprintf(out, "\n");
				break;
			}
		}
	}
}