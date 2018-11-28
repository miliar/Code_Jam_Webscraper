#include <iostream>
#include <vector>

using namespace std;

FILE *f = fopen("fractiles.in", "r");
FILE *g = fopen("fractiles.out", "w");

int T;
int K, C, S;

int main() {
	fscanf(f, "%d", &T);

	for (int t = 0; t < T; ++t) {
		fscanf(f, "%d %d %d", &K, &C, &S);
		fprintf(g, "Case #%d: ", t + 1);
		long long p = 1;
		long long rez = 1;
		for (int i = 1; i <= C - 1; ++i) {
			rez = rez * K;
		}
		for (int i = 1; i <= S; ++i) {
			p = rez * i;
			fprintf(g, "%lld ", p);
		}

		// fprintf(g, "   %d %d ", K, C);
		fprintf(g, "\n");
	}
}