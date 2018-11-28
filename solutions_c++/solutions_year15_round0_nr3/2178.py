#include <iostream>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <queue>
using namespace std;

#define rep(i,N) for((i) = 0; (i) < (N); (i)++)
#define rab(i,a,b) for((i) = (a); (i) <= (b); (i)++)
#define Fi(N) rep(i,N)
#define Fj(N) rep(j,N)
#define Fk(N) rep(k,N)
#define sz(v) (v).size()
#define all(v) (v).begin(),(v).end()

#define SYM_1 1
#define SYM_i 2
#define SYM_j 3
#define SYM_k 4

int multiply(int p, int q) {
	int sign;

	if ((p < 0 && q < 0) || (p > 0 && q > 0)) sign = 1;
	else sign = -1;

	if (p < 0) p = -p;
	if (q < 0) q = -q;

	if (p == SYM_1) return q * sign;
	else if (q == SYM_1) return p * sign;
	else if (p == q) return -SYM_1  * sign;
	else if (p == SYM_i) {
		if (q == SYM_j) return SYM_k * sign;
		if (q == SYM_k) return -SYM_j * sign;
	} else if(p == SYM_j) {
		if (q == SYM_i) return -SYM_k * sign;
		else if (q == SYM_k) return SYM_i * sign;
	} else if(p == SYM_k) {
		if(q == SYM_i) return SYM_j * sign;
		else if (q == SYM_j) return -SYM_i * sign;
	}
	assert(false);
	return 0;
}

vector <int> symbols;

vector <int> mul;
vector <bool> poss_k;

int get_sym(char c) {
	if (c == '1') return SYM_1;
	else if (c == 'i') return SYM_i;
	else if (c == 'j') return SYM_j;
	else if (c == 'k') return SYM_k;
	else return 0;
}

int main() {
	int T,cs;
	int L,X;
	int i,j;
	char s[1000000];

	scanf("%d",&T);

	rab(cs,1,T) {
		scanf("%d %d",&L,&X);
		scanf("%s",s);

		symbols.clear();
		mul.clear();
		poss_k.clear();

		Fi(X) {
			Fj(L) {
				symbols.push_back(get_sym(s[j]));
				mul.push_back(0);
				poss_k.push_back(false);
			}
		}

		mul[sz(symbols) - 1] = symbols[sz(symbols) - 1];
		poss_k[sz(symbols) -1] = (mul[sz(symbols) - 1] == SYM_k);
		for(i = sz(symbols) - 2; i >= 0; i--) {
			mul[i] = multiply(symbols[i], mul[i+1]);

			poss_k[i] = (poss_k[i+1] || (mul[i] == SYM_k));
			//printf("%d: %d %d\n", i, mul[i] , poss_k[i] ? 1 : 0);
		}
		poss_k.push_back(false);
		poss_k.push_back(false);

		bool p;

		if (mul[0] == multiply(SYM_i, multiply(SYM_j, SYM_k))) {
			int m;
			p = false;

			for(i = 0; i < sz(symbols); i++) {
				if (i == 0) m = symbols[0];
				else m = multiply(m, symbols[i]);

				if (m == SYM_i && poss_k[i+2]) {
					p = true;
					break;
				}
			}
		} else {
			p = false;
		}

		printf("Case #%d: %s\n",cs, p ? "YES" : "NO");
	}

	return 0;
}
