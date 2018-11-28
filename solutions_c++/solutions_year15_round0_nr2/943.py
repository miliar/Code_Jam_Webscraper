
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;
int n, pla[1005];

bool can(int tm) {
	for (int e=tm; e>0; e--) {
		int u=0;
		for (int i=0; i<n && pla[i]>e; i++) {
			u+=(pla[i]+e-1)/e-1;
			if (u+e>tm) break;
		}
		if (u+e<=tm)
			return true;
	}
	return false;
}

int solve() {
	scanf("%d",&n);
	for (int i=0; i<n; i++) {
		scanf("%d",pla+i);
	}
	sort(pla,pla+n);
	reverse(pla,pla+n);
	
	int a=0, b=pla[0], c;
	while (a+1<b) {
		c=(a+b)/2;
		if (can(c)) b=c; else a=c;
	}
	return b;
}

main() {
	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %d\n", cas$, solve());
	}
}
