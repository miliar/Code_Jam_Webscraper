#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;

typedef long long ll;
int t;
ll add(ll val, ll t, ll n){
	ll  ret = 0;
	while (t--)
		ret = (ret + val) % n;
	return ret;
}
ll multi(ll a, ll b, ll n){
	ll sum = 0;
	if (b > a)
		swap(b, a);
	int c = 0;
	while (b){
		ll cur = add(a, b % 10, n);
		int i = c;
		while (i--)
			cur = add(cur, 10, n);
		sum = (sum + cur) % n;
		b /= 10;
		++c;
	}
	return sum;
}
ll calc(ll b, ll e, ll n){
	if (!e)
		return 1;
	ll ret = calc(b, e / 2, n);
	ret = multi(ret, ret, n);
	if (e & 1)
		return multi(ret, b, n);
	return ret;
}
bool pri(ll val){
	if (val < 2 || (val % 2== 0 && val != 2))
		return 0;
	for (int i = 0; i < 6; ++i){
		if (calc(rand() % (val - 1) + 1, val - 1, val) != 1)
			return 0;
	}
	return 1;
}
vector<ll>vv;
bool ok(ll val){
	vv.clear();
	for (int b = 2; b < 11; ++b){
		ll x = val;
		ll fact = 1;
		ll dec = 0;
		while (x){
			dec += fact * (x % 2);
			fact *= b;
			x /= 2;
		}
		if (pri(dec))
			return 0;
		vv.push_back(dec);
	}
	return 1;
}
void print(ll val){
	vector<bool>v;

	while (val){
		v.push_back(val & 1);
		val /= 2;
	}
	for (int i = v.size() - 1; i > -1; --i)
		cout << v[i];
}
vector<int>p;
void printF(ll val){
	printf(" ");
	for (int i = 0; i < p.size(); ++i){
		if (val % p[i] == 0){
			printf("%d", p[i]);
			return;
		}
	}
}

const int N = 100000001;
bool s[N];
int main(){
	freopen("Cin.txt", "r", stdin);
	freopen("Cout.txt", "w", stdout);
	for (int i = 2; i * i < N; ++i){
		if (!s[i]){
			for (int j = i*i; j < N; j += i)
				s[j] = 1;
		}
	}
	for (int i = 2; i < N;++i)
	if (!s[i])
		p.push_back(i);
	cin >> t;
	for (int k = 1; k <= t; ++k){
		printf("Case #%d:\n", k);
		int l, j;
		cin >> l >> j;
		ll S = (1ll << (l - 1)) + 1;
		ll E = (1ll << l) - 1;
		for (ll i = S; i <= E && j; ++++i){
			if (ok(i)){
				--j;
				print(i);
				for (int ii = 0; ii < vv.size(); ++ii)
					printF(vv[ii]);
				puts("");
			}
		}
	}
}