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

int t, u[15];

int ok(ll x) {
	int ret = 0;
	do {
		if(!u[x%10]) ret++, u[x%10] = 1;
		x /= 10;
	} while(x > 0);
	return ret;
}
inline void solve(int tst) {
	ll x; scanf("%lld", &x);
	memset(u, 0, sizeof u);
	ll beg = x;
	int it = 0, cnt = 0;
	while(it <= 300000 && x <= (ll)5e16 && cnt < 10) {
		cnt += ok(x);
		it++;
		x += beg;
	}
	printf("Case #%d: ", tst);
	if(cnt == 10) printf("%lld\n", x-beg);
	else puts("INSOMNIA");
}

int main() {
	#ifdef accepted
		freopen(".in", "r", stdin);
		freopen("A.out", "w", stdout);
	#endif
	cin >> t;
	rep(i, 0, t-1) solve(i+1);
	return 0;
}
