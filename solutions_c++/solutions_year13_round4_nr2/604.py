#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <climits>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <ctime>

#define PI 3.14159265358979
#define EPS 1e-9

using namespace std;

#define REP(i, n) for (int i=0; i<n; i++)
#define FOR(i, m, n) for (int i=m; i<=n; i++)
#define ABS(a) (((a)>0)?(a):(-(a)))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int N, P;
ll n;

ll nejhorsi(ll x) {
	ll ans = 0;
	ll skok = 1;
	int k = 0;
	while (x-skok>=0 && k<N) {
		//printf("%lld\n", x);
		x -= skok;
		ans = ans*2 + 1;
		k++;
		skok *= 2;
	}
	while(k<N) {
		ans *= 2;
		k++;
	}
	return ans;
}

ll nejlepsi(ll x) {
	ll ans = 0;
	ll skok = 1;
	int k = 0;
	while (x+skok<n && k<N) {
		//printf("t%lld\n", x);
		x += skok;
		k++;
		skok *= 2;
	}
	while (k<N) {
		ans = ans*2+1;
		k++;
	}
	return ans;
}

ll low() {
	ll ans = -1;
	ll l = 0; ll r = n-1;
	while (l<=r) {
		ll h = (l+r)/2;
		ll poz = nejhorsi(h);
		if (poz<=P) {
			ans = max(ans, h);
			l = h+1;
		}
		else {
			r = h-1;
		}
	}
	return ans;
}

ll top() {
	ll ans = -1;
	ll l = 0; ll r = n-1;
	while (l<=r) {
		ll h = (l+r)/2;
		ll poz = nejlepsi(h);
		if (poz<=P) {
			ans = max(ans, h);
			l = h+1;
		}
		else {
			r = h-1;
		}
	}
	return ans;
}

void solve() {
	scanf("%d%d", &N, &P); P--;
	n = 1;
	REP (i, N)
		n *= 2;
	//printf("%lld %lld\n", nejhorsi(2), nejlepsi(2));
	printf("%lld %lld\n", low(), top());
}

int main()
{
	int t;
	scanf("%d", &t);
	REP (i, t) {
		printf("Case #%d: ", i+1);
		solve();
	}
	return 0;
}
