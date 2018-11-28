#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <fstream>
#include <list>
#include <set>
#include <climits>
#include <map>
#include <stack>
#include <queue>
#include <complex>
#include <cmath>
#include <sstream>
#include <deque>
#include <utility>
#include <bitset>
#include <ext/hash_set>
#include <ext/hash_map>

using namespace std;
using namespace __gnu_cxx;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define M 1001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define iter(it,s) for(it=s.begin();it!=s.end();it++)
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

ll mx = (ll) 1e7 + 100;
vector<ll> v;
int main() {
#ifndef ONLINE_JUDGE
	freopen("test.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	ll x, y, s1, s2;
	for (ll i = 1; i < mx; i++) {
		x = i * i;
		y = 0;
		s1 = i, s2 = 0;
		while (x)
			y *= 10, y += (x % 10), x /= 10;
		while (s1)
			s2 *= 10, s2 += (s1 % 10), s1 /= 10;
		if (i * i == y && i == s2)
			v.pb(i * i);
	}
	int t;
	ll a, b;
	scanf("%d", &t);
	FOR (cs, 1 , t + 1) {
		scanf("%lld%lld", &a, &b);
		int id1 = lower_bound(all(v),a)  - v.begin(), id2 =
				upper_bound(all(v),b)  - v.begin();
		if (id2 == sz(v) || v[id2] > b)
			b--;
		printf("Case #%d: %d\n", cs, id2 - id1);
	}
	return 0;
}
