/*************************************************************************
Author: zjut_polym
Created Time:   2013/4/27 8:44:13
File Name: codejam.cpp
************************************************************************/
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <climits>
#include <queue>
using namespace std;


//----------------------[ZJUT-polym for div2]-------------------------------------
#define ll long long
#define MOD 1000000007
#define PII pair<int, int>
#define ff first
#define ss second
#define sz(v) (int)v.size()
#define _mst(buf, val) memset(buf, val, sizeof(buf))
#define rep(i, l, r) for(i = (l); i <= (r); i++)
#define srep(i, l, r) for(i = (l); i >= (r); i--)
#define repi(it, c) for(typeof(c.begin())it = c.begin(); it != c.end(); it++)
#define inf 0x3f3f3f3f
#define N 100005
#define eps 1e-8
#define pi (2.0 * acos(0.0))
//--------------------------------------------------------------------------------
ll R;
bool cal(ll x, ll n){
	n -= x * (R-1);
	ll tmp = x * (x+1) / 2;
	//cout << tmp << " " << n << endl;
	if(tmp <= n)
		return true;
	return false;
}
ll B(ll l, ll r, ll n){
	ll mid;
	//cout << l << " " << r << endl;
	while(l < r){
		//cout << l << " " << r << endl;
		mid = (l + r + 1) / 2;
		if(cal(mid, n)){
			l = mid;
		}
		else{
			r = mid-1;
		}
	}
	//cout << l << endl;
	return l / 2;
}
int main() {
	int C, cas = 1;
	ll n;
	scanf("%d", &C);
	while(C--){
		scanf("%I64d%I64d", &R, &n);
		ll tmp = (ll)1 << 31;
		if(R != 1) tmp = n / (R - 1);
		printf("Case #%d: %I64d\n", cas++, B(1, min((ll)1 << 31, tmp), n));
	}	
    return 0;
}

