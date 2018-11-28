#include<stdio.h>
#include<algorithm>
using namespace std;

int T, TT;
int N, P;
long long A1, A2;

int main() {
	scanf("%d\n", &TT);
	for(int T = 1; T <= TT; ++T) {
	fprintf(stderr, "T = %d\n", T);
		scanf("%d %d", &N, &P);
		--P;
		A2 = (1LL<<N) - 1;
		long long rnk, s, t;
		for(rnk = (1LL<<N)-1, s = 1LL<<(N-1), t = 1; rnk > P && s > 0; ) {
			rnk -= s;
			s >>= 1;
			A2 -= t;
			t <<= 1;
		}
		A1 = 0;
		for(rnk = 0, s = 1LL<<(N-1), t = 1; rnk <= P && s > 0; ) {
			rnk += s;
			s >>= 1;
			A1 += t;
			t <<= 1;
		}
		if(rnk > P) --A1;
		printf("Case #%d: %lld %lld\n", T, A1, A2);
	}
}

