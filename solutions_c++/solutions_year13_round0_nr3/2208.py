
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst;
int dig[22], lp[99999], cp=1;
i8 ma=100000000000000LL, A,B;

int ple(i8 t) {
	int a=0, b=cp-1, c;
	while (a+1<b) {
		c=(a+b)/2;
		i8 z=lp[c];
		if (z*z<t) a=c; else b=c;
	}
	return a;
}

bool pal(i8 x) {
	int p=0;
	while (x>0) {
		dig[p++]=x%10;
		x/=10;
	}

	for (int i=0; i<p/2; i++)
		if (dig[i]!=dig[p-i-1]) return false;
	return true;
}

main() {
	for (int i=1; true; i++) {
		if (pal(i)) {
			i8 x=i;
			x*=x;
			if (x>ma) break;
			if (pal(x)) {
				//printf("   %d\n", i);
				lp[cp++]=i;
			}
		}
	}

	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%lld%lld", &A,&B);
		int re=ple(B+1)-ple(A);
		printf("Case #%d: %d\n", cas, re);
	}
}
