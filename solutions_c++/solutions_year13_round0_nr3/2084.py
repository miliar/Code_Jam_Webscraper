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

ve<ll> good;
char s[20];
bool palin(ll x) {
	sprintf(s, "%I64d", x);
	int l = strlen(s);
	for(int i = 0, j = l - 1; i < j; ++i, --j)
		if (s[i] != s[j]) return false;
	return true;
}
void init() {
	const ll N = 100000000000000LL;
	for(ll i = 1; i * i <= N; ++i) {
		if (palin(i) && palin(i * i)) good.pb(i * i);
	}
}
void solve() {
	ll a, b;
	cin >> a >> b;
	cout << upper_bound(all(good), b) - upper_bound(all(good), a-1);
}
int ucount(ve<int> &s, int a, int b) {
	return upper_bound(all(s), b) - upper_bound(all(s),a-1);
}
int main() {
#ifdef air
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	//ios_base::sync_with_stdio(false);
	
	init();
	int test;
	cin >> test;
	REP(t, 0, test) {
		printf("Case #%d: ", t+1);
		solve();
		printf("\n");
	}
	

#ifdef air
	//printf("\n\n%lf\n", clock() * 1e-3);
#endif

	return 0;
}