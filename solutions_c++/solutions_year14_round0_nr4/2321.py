#include <iostream>
#include <cstdio>
using namespace std;

void readAndSortArray(double a[1001], int n, FILE *in) {
	for (int i = 1; i <= n; i++) {
		fscanf(in, "%lf", &a[i]);
		int j = i;
		while (j > 1 && a[j] > a[j-1]) {
			double aux = a[j];
			a[j] = a[j - 1];
			a[j - 1] = aux;
			j--;
		} 
	}
}

// to check if I did the reading and the sorting good
// debugging purposes
void printArray(double a[1001], int n) {
	for (int i = 1; i <= n; i++) {
		printf("%lf ", a[i]);
	}
	printf("\n");
}

int solveReal(double N[1001], double K[1001], int n) {
	int points = 0;
	int NHead = 1, KHead = 1;
	int NTail = n, KTail = n;
	while ( NHead <= NTail && KHead <= KTail) {
		if (N[NHead] > K[KHead]) {
			points ++;
			NHead ++;
			KTail --;
		} else {
			NHead ++;
			KHead ++;
		}
	}
	return points;
}

int solveCheat(double N[1001], double K[1001], int n) {
	int points = 0;
	int NHead = 1, KHead = 1;
	int NTail = n, KTail = n;
	while ( NHead <= NTail && KHead <= KTail) {
		if (N[NTail] < K[KTail]) {
			NTail --;
			KHead ++;
		} else {
			points ++;
			NTail --;
			KTail --;
		}
	}
	return points;
}
void solve (int &real, int &cheat, FILE *in) {
	int n;
	double N[1001], K[1001];
	fscanf(in, "%d", &n);

	readAndSortArray(N, n, in);
	readAndSortArray(K, n, in);

	real = solveReal(N, K, n);
	cheat = solveCheat(N, K, n);
}

int main (int argc, char** argv) {
	int T;
	FILE *in, *out;
	in = fopen("input", "r");
	out = fopen("output", "w");
	fscanf(in, "%d", &T);

	for (int i = 1; i <= T; i++) {
		int real, cheat;
		solve(real, cheat, in);
		fprintf(out, "Case #%d: %d %d\n", i, cheat, real);
	}
	fclose (in);
	fclose (out);
	return 0;
}
