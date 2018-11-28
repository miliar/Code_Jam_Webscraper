
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst;
bool vo[333];
char nm[1000111];

i8 solve() {
	int n, ma=-1;
	i8 re=0;
	scanf("%s%d",nm,&n);
	int k=0;
	for (int i=0; nm[i]; i++) {
		if (vo[nm[i]]) {
			k=0;
		} else {
			k++;
			if (k>=n) ma=i-n+1;
		}
		if (ma>=0) re+=ma+1;
	}
	return re;
}

main() {
	vo['a']=true;
	vo['e']=true;
	vo['i']=true;
	vo['o']=true;
	vo['u']=true;

	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		printf("Case #%d: %lld\n", cas, solve());
	}
}
