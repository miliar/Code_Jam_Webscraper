#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int tc;
int n,a,b,c;

void doit(int p,int r,int s) {
	if (p+r+s == 0) return;
    if (p+r+s == 2) {
		if (p) printf("P");
		if (r) printf("R");
		if (s) printf("S");
		return;
    }
    int mx = max(p,max(r,s));
	int mi = min(p,min(r,s));
	int sum = p+r+s;
	if (sum%3 == 1) {
		if (p == mx) { doit(mx/2,mx/2,mx/2-1); doit(mx/2,mx/2-1,mx/2); return; }
		if (r == mx) { doit(mx/2,mx/2,mx/2-1); doit(mx/2-1,mx/2,mx/2); return; }
		if (s == mx) { doit(mx/2,mx/2-1,mx/2); doit(mx/2-1,mx/2,mx/2); return; }
	}
	else {
		if (p == mi) { doit(mi/2,mi/2+1,mi/2); doit(mi/2,mi/2,mi/2+1); return; }
		if (r == mi) { doit(mi/2+1,mi/2,mi/2); doit(mi/2,mi/2,mi/2+1); return; }
		if (s == mi) { doit(mi/2+1,mi/2,mi/2); doit(mi/2,mi/2+1,mi/2); return; }
	}
}

int main() {
	scanf("%d",&tc);
	for (int t=1; t<=tc; t++) {
		scanf("%d%d%d%d",&n,&b,&a,&c);
		int mx = max(a,max(b,c));
		int mi = min(a,min(b,c));
		if (mx>mi+1) {
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		printf("Case #%d: ",t);
		doit(a,b,c);
		printf("\n");
	}
    return 0;
}
