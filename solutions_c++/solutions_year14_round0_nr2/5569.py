#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;
double c, f, x, d;
double ans, w;
double cal() {
	while(1){
		if (w >= x) {
			return ans;
		}
		if(w < c){
			if ((c - w) / d > (x - w) / d){
				ans += (x - w) / d;
				return ans;
			} else {
				ans += (c - w) / d;
				w = c;
			}
		}
		if ((x - w) / d > c / f) {
			w -= c;
			d += f;
		} else {
			ans += (x - w) / d;
			w = x;
		}
	}
	return ans;
}
int main() {
		freopen("B-large.in", "r", stdin);
		freopen("B-large.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int cas = 1; cas <= t; cas++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		d = 2;
		w = 0;
		ans = 0;
		printf("Case #%d: %0.7lf\n", cas, cal());
	}
	return 0;
}
