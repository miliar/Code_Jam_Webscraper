#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <cstring>
#include <string>
#include <cmath>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <vector>
#include <algorithm>
#include <numeric>
#include <utility>
#include <functional>
#include <limits>
using namespace std;

typedef long long ll;

const double pi = acos(-1.0);

#define oned(a, x1, x2) { cout << #a << ":"; for(ll _i = (x1); _i < (x2); _i++){ cout << " " << a[_i]; } cout << endl; }
#define twod(a, x1, x2, y1, y2) { cout << #a << ":" << endl; for(ll _i = (x1); _i < (x2); _i++){ for(ll _j = (y1); _j < (y2); _j++){ cout << (_j > y1 ? " " : "") << a[_i][_j]; } cout << endl; } }

#define mp make_pair
#define pb push_back
#define fst first
#define snd second

#define MAXM 1005

ll TESTS, CASE;
ll n, p;

void solve() {
	cout << "Case #" << CASE << ": ";
	
	if(p == (1LL<<n)) {
		cout << (1LL<<n)-1 << ' ' << (1LL<<n)-1 << endl;
	} else {
		ll cnt = 0, curr = 0, add = 2, k = (1LL<<(n-1));
		while(cnt+k < p) {
			cnt += k;
			k /= 2;
			curr += add;
			add *= 2;
		}
		cout << curr << ' ';
		
		cnt = 0; curr = 0; add = (1LL<<(n-1)); k = 1;
		while(cnt+k < p) {
			cnt += k;
			k *= 2;
			curr += add;
			add /= 2;
		}
		cout << curr << endl;
	}
}

int main() {
//	n = 3;
//	ll s[1<<n];
//	for(ll i = 0; i < (1<<n); i++) {
//		s[i] = i;
//	}
//	
//	p = 8;
//	
//	ll cnt[1<<n], mx = 0;
//	memset(cnt,0,sizeof(cnt));
//	do {
//		ll r[1<<n];
//		memcpy(r,s,sizeof(s));
//		for(ll l = n; l > 0; l--) {
//			ll q[1<<n];
//			ll a = (1<<l);
//			ll b = a/2;
//			for(ll i = 0; i < (1<<n); i += a) {
//				ll x = i, y = i+b;
//				for(ll j = i; j < (i+a); j += 2) {
//					q[x++] = min(r[j], r[j+1]);
//					q[y++] = max(r[j], r[j+1]);
//				}
//			}
//			memcpy(r,q,sizeof(q));
//		}
//		for(ll i = 0; i < p; i++) {
//			cnt[r[i]]++;
//			mx = max(mx, r[i]);
//		}
//	} while(next_permutation(s,s+(1<<n)));
//	
//	ll ft = 0;
//	for(ll i = 0; i < (1<<n); i++) {
//		if(cnt[i] == 40320) {
//			ft = max(ft, i);
//		}
//	}
//	
//	cout << ft << ' ' << mx << endl;
	
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	cin >> TESTS;
	for(CASE = 1; CASE <= TESTS; CASE++) {
		cin >> n >> p;
		solve();
	}
}
