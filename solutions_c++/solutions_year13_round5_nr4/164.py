#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int T, TT;
int N;
char S[256];
int V[1<<20];
long double M[1<<20];

long double go(int mask) {
	if(V[mask] == T) return M[mask];
	V[mask] = T;
	int ii = -1;
	long double r = 0, t = -1;
	for(int i = N-1; i >= 0; --i) {
		if(!(mask & (1<<i))) {
			t = go(mask|(1<<i));
			r += t + N;
			ii = i;
		} else if(ii != -1) {
			r += t + N - (ii-i);
		}
	}
	for(int i = N-1; i >= 0; --i) {
		if(!(mask & (1<<i))) break;
		r += t + N - (N+ii-i);
	}
	M[mask] = r = r/N;
	return r;
}

int main() {
	scanf("%d\n", &TT);
	for(T = 1; T <= TT; ++T) {
		scanf("%s", S);
		N = strlen(S);
		V[(1<<N)-1] = T;
		M[(1<<N)-1] = 0;
		int mask = 0;
		for(int i = 0; i < N; ++i)
			if(S[i] == 'X') mask |= 1<<i;
		long double prf = go(mask);
		printf("Case #%d: %.9Lf\n", T, prf);
	}
}

