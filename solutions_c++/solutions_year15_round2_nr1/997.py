
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;

i8 sl(i8 n) {
	i8 re=0, og=n, t, p;
	int dg[22], sz=0;
	
	if (n<=10) 
		return n;
	if (n%10==0) {
		re++;
		n--;
	}
		
	t=n;
	while (t) {
		dg[sz++]=t%10;
		t/=10;
	}
	reverse(dg,dg+sz);
	
	// frst
	t=0; p=1;
	for (int i=0; i<sz/2; i++) {
		t += p*dg[i];
		p*=10;
	}
	re += t-1;
#ifdef MR7
	printf("    n=%lld sz=%d a1=%lld ", n, sz, t-1);
#endif
	
	// flp
	if (t-1) // if not 100000......
		re ++;
	reverse(dg,dg+sz);
	
	// sec
	t=0; p=1;
	for (int i=0; i<sz/2+(sz%2); i++) {
		t +=p*dg[i];
		p*=10;
	}
	re += t+1;
#ifdef MR7
	printf(" a2=%lld re:%lld\n", t+1, re);
#endif
	
	t=0;
	for (int i=0; i<sz-1; i++) {
		t=t*10+9;
	}
	
	return min(og, re+sl(t));
}

i8 solve() {
	i8 n;
	scanf("%lld",&n);
	return sl(n);
}

main() {
	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %lld\n", cas$, solve());
	}
}
