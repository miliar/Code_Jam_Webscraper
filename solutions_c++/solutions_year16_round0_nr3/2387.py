#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <unistd.h>
#include <stack>
#include <sstream>
#include <iomanip>
#include <bitset>
#define ff first
#define ss second

using namespace std;

typedef long long ll;

bitset<16> x;

int is_prime(ll num){
	if(!(num&1)) return 2;
	for(ll i = 3; i*i <= num; i+= 2){
		if(!(num%i)) return i;
	}
	return 0;
}

ll pot(ll a, int b){
	ll r = 1;
	while(b){
		if(b&1){
			b--;
			r*=a;
		}
		a*=a;
		b/=2;
	}
	return r;
}
vector<ll> ans;

bool check(){
	int i,j;
	ll sum;
	for(i = 2; i <= 10; i++){
		sum = 0;
		for(j = 15; j >= 0; j--){
			if(x[j]) sum += pot(i,j);
		}
		ll ret = is_prime(sum);
		if(!ret) return false;
		ans.push_back(ret);
	}
	return true;
}

int main() {
	int t,n,tc=1,j;

	cin >> t;
	while(t--){
		cin >> n >> j;
		ll i = (1<<n-1) + 1;
		ll lim = 1<<(n);
		cout << "Case #" << tc++ << ":\n";
		for(; i < lim && j; i+=2){
			x = i;
			ans.clear();
			if(check()){
				cout << x;
				for(ll a : ans){
					cout << " " << a;
				}
				cout << "\n";
				j--;
			}
		}
	}

	return 0;
}
