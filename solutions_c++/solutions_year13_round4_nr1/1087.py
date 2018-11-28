
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

typedef long long i8;

int tst;
i8  mo=1000002013;
const int MN=99333;
int N, M, a[MN], b[MN], pa[MN];

i8 solve() {
	scanf("%d%d", &N, &M);
	for (int i=0; i<M; i++) {
		scanf("%d%d%d",a+i,b+i,pa+i);
	}

	i8 re=0;
	while (true) {
		bool fin=true;
		for (int i=0; i<M; i++) {
			for (int j=0; j<M; j++) if (a[i]<a[j] && b[i]<b[j] && b[i]>=a[j]) {
				fin=false;
				if (M+1>=MN) return -1;
				int p=min(pa[i],pa[j]);
				re += (i8)(a[j]-a[i])*(i8)(b[j]-b[i])%mo*p%mo;
				
				int x=b[i];
				b[i]=b[j];
				b[j]=x;
				if (pa[i]>pa[j]) {
					a[M]=a[i]; b[M]=x; pa[M++]=pa[i]-p;
					pa[i]=p;
				} else if (pa[i]<pa[j]) {
					a[M]=a[j]; b[M]=b[i]; pa[M++]=pa[j]-p;
					pa[j]=p;
				}
			}
		}
		if (fin) break;
	}
	
	return re;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		printf("Case #%d: %lld\n", cas, solve());
	}
}
