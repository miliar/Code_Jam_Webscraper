#include <iostream>
#include <vector>

using namespace std;

FILE *f = fopen("counting_sheep.in", "r");
FILE *g = fopen("counting_sheep.out", "w");

int T;
long long N;
int numbers[10];
int tmp[100];
int n[100];

void convert(long long p, int t[100]) {
	int pos = 0;
	while (p > 0) {
		t[++pos] = p % 10;
		p = p / 10;
	}
	t[0] = pos;
}

bool verify(int t[100]) {
	for (auto i = 1; i <= t[0]; ++i) {
		numbers[t[i]] = 1;
	}
	for (int i = 0; i < 10; ++i) {
		if (!numbers[i]) return false;
	}
	return true;
}

void multiply(int A[100], int B[100]) {
	int C[100];
	int i, j, T = 0;

	C[0] = A[0] + B[0] - 1;
	for (i = 1; i <= A[0] + B[0];) C[i++]=0;
	for (i = 1; i <= A[0]; i++)
	for (j = 1; j <= B[0]; j++)
		C[i + j - 1] += A[i] * B[j];
	for (i = 1; i <= C[0]; i++) { 
		T = (C[i] += T) / 10;
		C[i] %= 10;
	}
	if (T) C[++C[0]] = T;

	for (int i = 0; i <= C[0]; ++i) {
		A[i] = C[i];
	}
}

int main() {
	fscanf(f, "%d", &T);

	for (int t = 0; t < T; ++t) {
		fscanf(f, "%lld", &N);
		fprintf(g, "Case #%d: ", t + 1);

		if (N != 0) {
			for (int i = 0; i < 10; ++i) numbers[i] = 0;
			int p = 1;
			convert(N, n);
			bool found = verify(n);

			while (!found) {
				convert(p, tmp);
				multiply(tmp, n);
				found = verify(tmp);
				p++;
			}
			for (int i = tmp[0]; i >= 1; --i) {
				fprintf(g, "%d", tmp[i]);
			}
			fprintf(g, "\n");
		}
		else {
			fprintf(g, "INSOMNIA\n");
		}
	}
}