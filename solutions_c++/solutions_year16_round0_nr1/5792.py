#include <bits/stdc++.h>
using namespace std;
#define ll long long

void update(ll n, int &bit) {
	while(n) {
		bit|=(1<<(n%10));
		n/=10;
	}
}

int main()
{
	ll ans;
	int tt,t,n,bit;
	cin >>tt;
	for(t=1;t<=tt;t++) {
		cin >> n;
		printf("Case #%d: ",t);
		if(!n) {
			puts("INSOMNIA");
			continue;
		}
		bit=0;
		ans=n;
		update(ans,bit);
		while(bit!=1023) {
			ans+=n;
			update(ans,bit);
		}
		printf("%lld\n",ans);
	}
	return 0;
}