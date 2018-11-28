
#include <cstdio>
#include <algorithm>
#include <set>
using namespace std;

typedef long long i8;

int tst, a, b, k;

i8 slow() {
	int re=0;
	for (int i=0; i<a; i++)
		for (int j=0; j<b; j++)
			if ((i&j)<k) re++;
	return re;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%d%d%d",&a,&b,&k);
		printf("Case #%d: %lld\n", cas, slow());
	}
}
