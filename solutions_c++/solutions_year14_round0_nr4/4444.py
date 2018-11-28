#include <cstdio>
#include <algorithm>
using namespace std;
double a[1200], b[1200];
int n;
int gao(double a[], double b[]){
	for(int r=n; r; r--){
		bool ok=1;
		for(int i=0; i<r; i++)
			if(a[i]>=b[n-r+i])ok=0;
		if(ok)return r;
	}
	return 0;
}
int main(){
	int T;
	scanf("%d", &T);
	for(int tt=1; tt<=T; tt++){
		scanf("%d", &n);
		for(int i=0; i<n; i++)
			scanf("%lf", a+i);
		for(int i=0; i<n; i++)
			scanf("%lf", b+i);
		sort(a, a+n);
		sort(b, b+n);
		printf("Case #%d: %d %d\n", tt, gao(b,a), n-gao(a,b));
	}
}
