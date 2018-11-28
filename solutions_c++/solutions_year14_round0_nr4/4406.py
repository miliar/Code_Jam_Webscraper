#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
double a[1111], b[1111];
int T, n;
bool cmp(double x, double y){
	return x > y;
}
int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	scanf("%d", &T);
	for ( int I(1); I <= T; I++){
		scanf("%d", &n);
		for ( int i(1); i <= n; i++) scanf("%lf", &a[i]);
		for ( int i(1); i <= n; i++) scanf("%lf", &b[i]);
		sort(a+1, a+n+1, cmp);
		sort(b+1, b+n+1, cmp);
		int ans2 = n, k = n;
		for ( int i(n); i>=1; i--){
			while ( b[k] < a[i] && k > 1 ) k--;
			if ( b[k] > a[i] ) {
				ans2--,k--;
				if ( k == 0 ) break;
			}else
			if ( k==1 ) break;
		}
		int ans1=0; k = n;
		for ( int i(n); i>=1; i--){
			while ( a[k] < b[i] && k > 1) k--;
			if ( a[k] > b[i] ) {
				ans1++,k--;
				if ( k == 0 ) break;
			}else
			if ( k==1) break;
		}
		printf("Case #%d: %d %d\n", I, ans1, ans2);
	}
	return 0;
}
