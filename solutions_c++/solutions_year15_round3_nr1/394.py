
#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long i8;

int ntc$, cas$;

int solve() {
	int r,c,w;
	scanf("%d%d%d",&r,&c,&w);
	if (w==1)
		return r*c;
	
	int nos=c/w;
	int shi=c/w+w-1;
	if (c%w) shi++;
	return (r-1)*nos + shi;
}

main() {
	scanf("%d", &ntc$);
	for (int cas$=1; cas$<=ntc$; cas$++) {
		printf("Case #%d: %d\n", cas$, solve());
	}
}
