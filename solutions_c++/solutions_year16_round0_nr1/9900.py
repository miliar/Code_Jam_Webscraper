#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
int T,m;
ll n;
int fl[10];
int now;

void check(ll v) {
	ll tmp = v;
	while(v) {
		if(!fl[v%10]) {
			now--;
			fl[v%10] = 1;
		}
		v/=10;
	}
	if(now == 0) printf("%lld\n",tmp);
	return;
}

int main() {
	scanf("%d",&T);
	for(int tt=1; tt<=T; tt++) {
		scanf("%lld",&n);
		printf("Case #%d: ",tt);
		if(n == 0) puts("INSOMNIA");
		else {
			now = 10;
			for(int i=0; i<now; i++) fl[i] = 0;
			for(m=1;now > 0;m++) {
				check(n*m);
			}
		}
	}
	return 0;
}
