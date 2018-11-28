#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#define MAXN (1 << 10)
using namespace std;

typedef unsigned long long ll;

ll R, T;
vector<int> vec;

inline ll save(ll a, ll b) {
	ll t = a;
	vec.clear();
	
	while (t) {
		vec.push_back(t & 1ULL);
		t >>= 1ULL;
	}
	
	ll res = 0ULL;
	for (int i=(int)vec.size()-1; i >= 0; --i) {
		res *= 2ULL;
		
		if (res > T)
			return -1;
		
		if (vec[i] == 1) {
			res += b;
			if (res > T)
				return -1;
		}
	}
	
	return res;
}

inline bool good(ll x) {
	ll other = 2ULL * R + 1ULL + (x-1)*2ULL;
	
	ll res = save(x, other);
	if (res < 0) return false;
	return (res <= T);
}

inline void solve(int test) {
	ll l=0, r=T, mid;
	
	while (r-l > 1LL) {
		mid = (l+r) / 2;
		
		if (good(mid)) l = mid;
		else r = mid;
	}
	
	printf("Case #%d: ", test);
	cout << l << '\n';
}

inline void read() {
	cin >> R >> T;
}

int main() {
	int brt = 0, test = 0;
	scanf("%d", &brt);
	
	while (brt --) {
		read();
		solve(++test);
	}
	return 0;
}