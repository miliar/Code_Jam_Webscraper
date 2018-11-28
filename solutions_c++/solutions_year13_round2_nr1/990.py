
#include <cstdio>
#include <algorithm>
using namespace std;

typedef long long i8;

int tst, mote[505], a,n;
int bre[505];

int solve() {
	int rez=n;
	if (a==1) return rez;
	
	for (int j=1; j<105; j++)
		bre[j]=0;
	bre[0]=a;
	
	sort(mote,mote+n);
	for (int i=0; i<n; i++) {
		int e=mote[i];
		for (int m=rez; m>=0; m--) if (bre[m]>0) {
			int x=bre[m], z=0;
			while (x<=e) {
				z++;
				x+=x-1;
			}
			bre[m]=0;
			if (m+z<=rez) {
				bre[m+z]=max(bre[m+z],x+e);
				rez=min(rez,m+z+n-i-1);
			}
		}
	}
	
	return rez;
}

main() {
	scanf("%d", &tst);
	for (int cas=1; cas<=tst; cas++) {
		scanf("%d%d",&a,&n);
		for (int i=0; i<n; i++)
			scanf("%d",mote+i);

		printf("Case #%d: %d\n", cas, solve());

	}
}
