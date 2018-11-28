#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <set>
using namespace std;
#define ll long long
ll t, n;
set<ll> s;

void getnum(ll x){
	while (x != 0){
		s.insert(x % 10);
		x -= (x%10);
		x/=10;
	}
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large-out.txt", "w", stdout);
	scanf("%lld", &t);
	for (ll i = 0; i < t; i++){
		scanf("%lld", &n);
		if (n == 0){
			printf("Case #%lld: INSOMNIA\n", i + 1);
			continue;
		}
		s.clear();
		for (ll j = 1; j < 1000; j++){
			getnum(j*n);
			if (s.size() == 10){
				printf("Case #%lld: %lld\n", i + 1, n*j);
				break;
			}
		}
	}
}
