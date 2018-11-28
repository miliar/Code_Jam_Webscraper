#include <iostream>
#include <cstdio>
using namespace std;

FILE *stream;

int main() {

	freopen_s(&stream, "B-large.in", "r", stdin);
	freopen_s(&stream, "B-large.out", "w", stdout);


	int n;
	scanf_s("%d", &n);

	long double C, F, X, T, f;

	for (int i = 1; i <= n; i++) {
		scanf_s("%Lf %Lf %Lf", &C, &F, &X);
		T = 0.0;
		f = 2.0;

		while ((X / f) > (C / f + X / (f + F))) {
			T = T + C / f;
			f = f + F;
		}
		T = T + X / f;
		printf("Case #%d: %.7Lf\n", i, T);
	}
}
