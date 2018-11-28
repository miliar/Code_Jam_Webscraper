#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
ll t, n, w;
ll arr[33];
vector<ll> v;

ll power(ll a, ll x){
	if (x == 0) return 1;
	if (x == 1) return a;
	ll half;
	if (x % 2 == 0){
		half = power(a, x/2);
		half *= half;
	} else {
		half = power(a, (x - 1)/2);
		half *= half;
		half *= a;
	}
	return half;
}

bool checker(ll x){
	if (x == 1) return false;
	if (x == 2) return false;
	if (x % 2 == 0){
		v.push_back(2);
		return true;
	}
	for (ll i = 3; i*i <= x; i+=2){
		if (i == x) return false;
		if (x % i == 0){
			v.push_back(i);
			return true;
		}
	}
	return false;
}

bool checking(){
	ll num = 0;

	for (ll i = 2; i <= 10; i++){
		num = 0;
		for (ll j = 0; j < n; j++){
			if (arr[j] == 0) continue;
			num += power(i, n - 1 - j);
		}
		if (!checker(num)) return false;
	}
	return true;
}

bool check(){ //return true if not completely filled
	for (ll i = 0; i < n; i++){
		if (arr[i] != 1) return false;
	}
	return true;
}

void addone(){
	for (ll i = n - 1; i >= 0; i--){
		if (arr[i] == 0){
			arr[i] = 1;
			break;
		} else {
			arr[i] = 0;
		}
	}
}

void printarr(){
	for (ll i = 0; i < n; i++){
		cout << arr[i];
	}
	cout << endl;
}


int main(){
	freopen("C-small-out2.txt", "w", stdout);
	scanf("%lld%lld%lld", &t, &n, &w);
	printf("Case #1:\n");
	while (!check() && w > 0){
		addone();
		if (arr[0] == 0){
			arr[0] = 1;
		}
		if (arr[n - 1] == 0){
			addone();
		}
		//printarr();
		v.clear();
		if (!checking()) continue;
		//printarr();
		w--;
		for (ll i = 0; i < n; i++){
			printf("%lld", arr[i]);
		}
		for (vector<ll>::iterator it = v.begin(); it != v.end(); it++){
			printf(" %lld", *it);
		}
		v.clear();
		printf("\n");
		
	}
	
}
