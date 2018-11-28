#include <iostream>
#include <cstdio>
#include <cmath>

int main() {
	int cases;
	long long r,t;
	long long p;
	long long acc;
	scanf("%d",&cases);
	for (int i=1; i <= cases; i++ ) {
		scanf("%lld %lld",&r,&t);
		acc = 0;
		p=0;
		while (true) {
			p = (r+1)*(r+1) - r*r;
			if ( p <= t) {
				t = t-p;
				r = r+2; 
				acc++;
			} else {
				break;
			}
		}
		printf("Case #%d: %lld\n",i,acc);
	}
}
