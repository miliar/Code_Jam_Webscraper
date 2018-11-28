#include <iostream>
#include <vector>

using namespace std;

FILE *f = fopen("revenge_pancakes.in", "r");
FILE *g = fopen("revenge_pancakes.out", "w");

int T;
char str[110];
int a[110];
int N;

void removeExtra() {
	while (a[N]) {
		N--;
	}
}

int countEnd(int x) {
	int p = 0;
	int k = N;
	while (k >=0 && a[k] == x) {
		k--, p++;
	}
	return p;
}

int countBegin(int x) {
	int p = 0;
	int k = 0;
	while (k <= N && a[k] == x) {
		k++, p++;
	}
	return p;
}

int minim(int a, int b) {
	if (a < b) return a;
	return b;
}

void flip() {
	int b[110];
	for (int i = 0; i <= N; ++i) {
		b[i] = !a[N - i];
	}
	for (int i = 0; i <= N; ++i) {
		a[i] = b[i];
	}
}

int main() {
	fscanf(f, "%d\n", &T);

	for (int t = 0; t < T; ++t) {
		fgets(str, 110, f);
		N = 0;
		for (int i = 0; i < strlen(str); ++i) {
			if (str[i] == '-') a[N++] = 0;
			if (str[i] == '+') a[N++] = 1;
		}
		N--;
		// cout << "N = " << N << endl;

		int sol = 0;
		while (N >= 0) {
			removeExtra();
			int p = countEnd(0);
			int l = countBegin(1);
			// int k = minim(p, l);
			int k = l;
			if (k > 0) {
				for (int i = 0; i < k; ++i)
					a[i] = 0;
				sol++;
			}	
			if (N >= 0) {
				flip();
				sol++;
			}
		}

		fprintf(g, "Case #%d: %d\n", t + 1, sol);
	}
}