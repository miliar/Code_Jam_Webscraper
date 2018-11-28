#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(s) ((int)(s.size()))
#define all(s) s.begin(),s.end()
#define rep(i,a,n) for(int i=a;i<=n;++i)
#define per(i,n,a) for(int i=n;i>=a;--i)

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

const int MAXN = 3e5 + 256;
const char nxtl = '\n';
const double eps = (double)1e-9;
template<typename T> inline bool updmin(T &a, const T &b) {return a > b ? a = b, 1 : 0;}
template<typename T> inline bool updmax(T &a, const T &b) {return a < b ? a = b, 1 : 0;}

int t;
inline bool bit(const int &msk, const int &pos) {
	return msk & (1 << pos);
}
inline ll isprime(const ll &x) {
	for(ll i = 2ll; i * i <= x; ++i) {
		if(x % i == 0ll) return i;
	}
	return 0;
}
inline ll transform(ll x, const ll &sist) {
	ll ret = 0, cur = 1;
	while(x > 0) {
		ret += cur * (x % 10ll);
		cur *= sist;
		x /= 10ll;
	}
	return ret;
}

void solve(int tst) {
	int n, k; scanf("%d%d", &n, &k);
	printf("Case #%d:\n", tst);
	rep(msk, 0, (1<<n)-1) {
		if(!k) break;
		if(!bit(msk, 0) || !bit(msk, n-1)) continue;
		ll num = 0;
		rep(pos, 0, n-1) {
			num = num * 10 + bit(msk, pos);
		}
		bool ok = 1;
		rep(ss, 2, 10) {
			if(!isprime(transform(num, ss))) {
				ok = 0; break;
			}
		}
		if(ok) {
			k--;
			printf("%lld ", num);
			rep(ss, 2, 10) {
				printf("%lld ", isprime(transform(num, ss)));
			}
			puts("");
		}
	}
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen("A.out", "w", stdout);
	#endif
	cin >> t;
	rep(i, 1, t) solve(i);
	return 0;
}
