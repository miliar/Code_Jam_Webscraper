#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

int i,j,k,l,n,t;
double c,f,x,tim[110000],gps,ans;

int main() {
	scanf("%d", &t);
	for(l=1 ; l<=t ; l++) {
		scanf("%lf%lf%lf", &c, &f, &x);
		
		n = (int) floor(x);
		
		ans = x/2.0;
		gps = 2.0;
		
		for(i=1 ; i<=n ; i++) {
			tim[i] = tim[i-1] + (c/gps);
			gps += f;
			ans = min(ans, tim[i] + (x/gps));
		}
		
		printf("Case #%d: %.7lf\n", l, ans);
	}
	
	return 0;
}
