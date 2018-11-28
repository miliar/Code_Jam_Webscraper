#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

set<int> dig;

void f(ll k) {
	while(k) {
		dig.insert(k%10);
		k/=10;
	}
}

int t;

int main()
{
	scanf("%d", &t);
	for(int q=1; q<=t; q++) {
		ll x;
		scanf("%lld", &x);
		if(x==0) {
			printf("Case #%d: INSOMNIA\n", q);
			continue;
		}
		dig.clear();
		f(x);
		ll cur=x;
		while(dig.size()<10) {
			cur+=x;
			f(cur);
		}
		printf("Case #%d: %lld\n", q, cur);
	}

	return 0;
}
