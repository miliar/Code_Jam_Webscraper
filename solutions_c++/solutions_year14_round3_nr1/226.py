
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long i8;

int tst, n, m;
i8 a,b; char c;

i8 nod(i8 a, i8 b) {
	if (!b) return a;
	return nod(b,a%b);
}

void solve() {
	i8 n=nod(a,b);
	a/=n; b/=n;
	if (a==b) {
		printf("1\n");
		return;
	}
	
	i8 c=1; bool ok=false; int p=-1;
	for (int i=0; i<40; i++) {
		c*=2;
		if (b==c) {
			ok=true;
			p=i;
			break;
		}
	}
	if (!ok) {
		printf("impossible\n");
		return;
	}

	while (a/2>0) {
		a/=2;
		p--;
	}
	printf("%d\n",p+1);
	return;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%lld", &a);
		scanf("%c", &c);
		scanf("%lld", &b);

		printf("Case #%d: ", cas);
		solve();
	}
}
