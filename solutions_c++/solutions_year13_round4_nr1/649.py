#define _CRT_SECURE_NO_WARNINGS
#include <numeric>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <bitset>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <stdio.h>
#include <string.h>
#include <string>
#include <sstream> 
#include <stack>

#pragma comment(linker, "/STACK:256000000")
using namespace std;
typedef long long ll;
template<typename T> int size(T &a) {return (int)a.size();}
template<typename T> T sqr(T a)  { return a * a; }

#define fi first
#define se second
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,a,b) for(int i=(a);i<(b); ++i)
#define REPD(i,a,b)for(int i=(b)-1;i>=a;--i)
#define _(a,b) memset((a), (b), sizeof(a))
#define all(a) a.begin(), a.end()
#define mp make_pair
#define pb push_back
#define ve vector

const ll mod = 1000002013LL;
ll MOD(ll x) {
	x = (x % mod + mod) % mod;
	return x;
}
void add(ll &a, ll b) {
	a = MOD(a) + MOD(b);
	a %= mod;
}
ll cost(ll len, int n) {
	ll res = MOD(len * n) - MOD(len * (len - 1) / 2);
	res = MOD(res);
	return res;
}
ll solve(ve<int> co, ve<ll> cnt, int l, int r, int n) {
	ll res = 0;
	for (int i = l, j = i; i <= r; i = j) {
		if (cnt[i] == 0) {
			j = i + 1;
			continue;
		}
		for(j = i; j <= r && cnt[j]>0; ++j) ;
		ll mn = ll(1e18);
		for(int u = i; u < j; ++u)
			mn = min(mn, cnt[u]);
		res = res + MOD( cost(co[j] - co[i],n) * MOD(mn));
		res = MOD(res);
		for(int u = i; u < j; ++u)
			cnt[u] -= mn;
		res = MOD(res + solve(co, cnt, i, j-1, n));
	}
	return res;
}
void solve() {
	int n, m;
	cin >> n >> m;
	ve<int> a(m), b(m), p(m);
	REP(i, 0, m) cin >> a[i] >> b[i] >> p[i];
	ve<int> co;
	REP(i, 0, m) co.pb(a[i]);
	REP(i, 0, m) co.pb(b[i]);
	sort(all(co));
	co.erase(unique(all(co)), co.end());
	ve<ll> cnt(size(co) - 1);
	ll old = 0;
	REP(i, 0, m) {
		int len = b[i] - a[i];
		ll cur = MOD(cost(len, n) * p[i]);
		old = (old + cur) % mod;
	}
	REP(i, 0, size(co) - 1) {
		int l = co[i];
		int r = co[i + 1];
		ll cur = 0;
		REP(j, 0, m) {
			int x = a[j];
			int y = b[j];
			if (x <= l && r <= y) {
				cur += p[j];
			}
		}
		cnt[i] = cur;
	}
	ll nw = solve(co, cnt, 0, size(cnt) - 1, n);
	old = ((old - nw) % mod + mod) % mod;
	cout<<old<<endl;
}
int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int test;
	cin>>test;
	REP(it, 0, test) {
		printf("Case #%d: ", it+1);
		solve();
	}


	return 0;
}           