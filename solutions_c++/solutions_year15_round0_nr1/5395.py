#include <cstdio>

#define FOR(I,S,T) for(int I=S;I<T;++I)
#define REP(I,N) FOR(I,0,N)

char S[1001];
int main() {
	int TC;
	scanf("%d", &TC);
	REP(tc, TC) {
		int n;
		scanf("%d%s", &n, S);
		int acc = 0;
		int need = 0;
		REP(i, n+1) {
			if (acc < i) {
				need += i - acc;
				acc = i;
			}
			acc += S[i] - '0';
		}
		printf("Case #%d: %d\n", tc+1, need);
	}
	return 0;
}
