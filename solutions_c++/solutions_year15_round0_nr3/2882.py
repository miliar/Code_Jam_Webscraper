#include <cstdio>
#include <cstdlib>

using namespace std;

const char JEDEN = '1';
const char M_JEDEN = '0';
const char I = 'i';
const char M_I = 'I';
const char J = 'j';
const char M_J = 'J';
const char K = 'k';
const char M_K = 'K';

char mul(char a, char b) {
	if (a == JEDEN && b == JEDEN) return JEDEN;
	else if (a == JEDEN && b == I) return I;
	else if (a == JEDEN && b == J) return J;
	else if (a == JEDEN && b == K) return K;
	else if (a == I && b == JEDEN) return I;
	else if (a == I && b == I) return M_JEDEN;
	else if (a == I && b == J) return K;
	else if (a == I && b == K) return M_J;
	else if (a == J && b == JEDEN) return J;
	else if (a == J && b == I) return M_K;
	else if (a == J && b == J) return M_JEDEN;
	else if (a == J && b == K) return I;
	else if (a == K && b == JEDEN) return K;
	else if (a == K && b == I) return J;
	else if (a == K && b == J) return M_I;
	else if (a == K && b == K) return M_JEDEN;

	else if (a == M_JEDEN && b == JEDEN) return M_JEDEN;
	else if (a == M_JEDEN && b == I) return M_I;
	else if (a == M_JEDEN && b == J) return M_J;
	else if (a == M_JEDEN && b == K) return M_K;
	else if (a == M_I && b == JEDEN) return M_I;
	else if (a == M_I && b == I) return JEDEN;
	else if (a == M_I && b == J) return M_K;
	else if (a == M_I && b == K) return J;
	else if (a == M_J && b == JEDEN) return M_J;
	else if (a == M_J && b == I) return K;
	else if (a == M_J && b == J) return JEDEN;
	else if (a == M_J && b == K) return M_I;
	else if (a == M_K && b == JEDEN) return M_K;
	else if (a == M_K && b == I) return M_J;
	else if (a == M_K && b == J) return I;
	else if (a == M_K && b == K) return JEDEN;

	else if (a == JEDEN && b == M_JEDEN) return M_JEDEN;
	else if (a == JEDEN && b == M_I) return M_I;
	else if (a == JEDEN && b == M_J) return M_J;
	else if (a == JEDEN && b == M_K) return M_K;
	else if (a == I && b == M_JEDEN) return M_I;
	else if (a == I && b == M_I) return JEDEN;
	else if (a == I && b == M_J) return M_K;
	else if (a == I && b == M_K) return J;
	else if (a == J && b == M_JEDEN) return M_J;
	else if (a == J && b == M_I) return K;
	else if (a == J && b == M_J) return JEDEN;
	else if (a == J && b == M_K) return M_I;
	else if (a == K && b == M_JEDEN) return M_K;
	else if (a == K && b == M_I) return M_J;
	else if (a == K && b == M_J) return I;
	else if (a == K && b == M_K) return JEDEN;

	else if (a == M_JEDEN && b == M_JEDEN) return JEDEN;
	else if (a == M_JEDEN && b == M_I) return I;
	else if (a == M_JEDEN && b == M_J) return J;
	else if (a == M_JEDEN && b == M_K) return K;
	else if (a == M_I && b == M_JEDEN) return I;
	else if (a == M_I && b == M_I) return M_JEDEN;
	else if (a == M_I && b == M_J) return K;
	else if (a == M_I && b == M_K) return M_J;
	else if (a == M_J && b == M_JEDEN) return J;
	else if (a == M_J && b == M_I) return M_K;
	else if (a == M_J && b == M_J) return M_JEDEN;
	else if (a == M_J && b == M_K) return I;
	else if (a == M_K && b == M_JEDEN) return K;
	else if (a == M_K && b == M_I) return J;
	else if (a == M_K && b == M_J) return M_I;
	else if (a == M_K && b == M_K) return M_JEDEN;
	else {
		// printf("Przypał\n");
	}
}

const int L_MAX = 10000;

char wzor[L_MAX];
char slowo[L_MAX];

void wczytaj(char c, int i) {
	if (c == 'i') {
		wzor[i] = I;
	} else if (c == 'j') {
		wzor[i] = J;
	} else if (c == 'k') {
		wzor[i] = K;
	}
	else {
		// printf("2Przypał\n");
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		int L, X;
		scanf("%d %d", &L, &X);
		getchar();
		for (int i = 0; i < L; ++i) {
			char c = getchar();
			wczytaj(c, i);
		}
		getchar();
		for (int i = 0; i < X; ++i) {
			for (int j = 0; j < L; ++j) {
				slowo[i*L + j] = wzor[j];
			}
		}
		// for (int i = 0; i < X * L; ++i) {
			// printf("%c", slowo[i]);
		// }
		// printf("\n");
		int a = slowo[0];
		int ile = 0;
		for (int i = 1; i < X*L; ++i) {
			if (a == I && ile == 0) {
				ile = 1;
				a = slowo[i];
			} else if (a == J && ile == 1) {
				ile = 2;
				a = slowo[i];
			} else if (a == K && ile == 2) {
				ile = 3;
				a = slowo[i];
			} else {
				a = mul(a, slowo[i]);
			}
		}
		// printf("%c\n", a);
		// if (X * L >= 3 && a == M_JEDEN) {
			// printf("Case #%d: YES\n", t);
		if (ile == 2 && a == K) {
			printf("Case #%d: YES\n", t);
		} else if (ile == 3 && a == JEDEN) {
			printf("Case #%d: YES\n", t);
		} else {
			printf("Case #%d: NO\n", t);
		}
	}
	return 0;
}