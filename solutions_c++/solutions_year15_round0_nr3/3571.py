#include <cstdio>
#include <cstdlib>

using namespace std;

typedef char c_type;

const c_type ONE = '1';
const c_type M_ONE = '2';
const c_type I = '3';
const c_type M_I = '4';
const c_type J = '5';
const c_type M_J = '6';
const c_type K = '7';
const c_type M_K = '8';
const int L_MAX = 10000;

c_type tabliczka[8][8] = {
	{ ONE, I, J, K, M_ONE, M_I, M_J, M_K },
	{ I, M_ONE, K, M_J, M_I, ONE, M_K, J },
	{ J, M_K, M_ONE, I, M_J, K, ONE, M_I },
	{ K, J, M_I, M_ONE, M_K, M_J, I, ONE },
	{ M_ONE, M_I, M_J, M_K, ONE, I, J, K },
	{ M_I, ONE, M_K, J, I, M_ONE, K, M_J },
	{ M_J, K, ONE, M_I, J, M_K, M_ONE, I },
	{ M_K, M_J, I, ONE, K, J, M_I, M_ONE },
};

c_type pattern[L_MAX];

int get_id(c_type a) {
	if (a == ONE) return 0;
	else if (a == I) return 1;
	else if (a == J) return 2;
	else if (a == K) return 3;
	else if (a == M_ONE) return 4;
	else if (a == M_I) return 5;
	else if (a == M_J) return 6;
	else if (a == M_K) return 7;
	else return -1;
}

c_type mul(c_type a, c_type b) {
	return tabliczka[get_id(a)][get_id(b)];
}

void wczytaj(c_type c, int i) {
	if (c == 'i')
		pattern[i] = I;
	else if (c == 'j')
		pattern[i] = J;
	else // if (c == 'k')
		pattern[i] = K;
}

void print(int result, int t) {
	if (result) {
		printf("Case #%d: YES\n", t);
	} else {
		printf("Case #%d: NO\n", t);
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
			c_type c = getchar();
			wczytaj(c, i);
		}
		getchar();
		int a = pattern[0];
		int r = 0;
		for (int i = 1, it = 1; i < X * L; ++i, ++it) {
			it %= L;
			if ((r == 0 && a == I) 
			 || (r == 1 && a == J)
			 || (r == 2 && a == K)) {
				r++;
				a = pattern[it];
			} else {
				a = mul(a, pattern[it]);
			}
		}
		print((r == 2 && a == K) || (r == 3 && a == ONE), t);
	}
	return 0;
}