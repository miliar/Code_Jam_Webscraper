#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#include <ctime>
#include <queue>
using namespace std;
typedef long long llong;

template<class T>
int bit(T x, int pos){
	return (x >> pos) & 1;
}
llong f(int n, llong p){
	--p;
	int u = 0;
	for(int i = n - 1; i >= 0 && bit(p, i); --i) ++u;
	return min((1LL << n) - 1, (1LL << (u + 1)) - 2);
}

llong worst(int n, llong x){
	llong ret = 0;
	++x;
	for(int i = 0;i < n; ++i){
		ret <<= 1;
		if(x > 1) ret |= 1;
		x >>= 1;
	}
	return ret;
}
llong best(int n, llong x){
	llong ret = 0;
	x = (1LL << n) - x;
	for(int i = 0;i < n; ++i){
		ret <<= 1;
		if(x <= 1) ret |= 1;
		x >>= 1;
	}
	return ret;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for(int cas = 1;cas <= TT; ++cas){
		int n;
		llong p;
		scanf("%d %lld", &n, &p);
		--p;
		llong l = 0, r = (1LL << n);
		while(l < r){
			llong m = (l + r) / 2;
			if(worst(n, m) <= p) l = m + 1;
			else r = m;
		}
		llong ret1 = l - 1;
		l = 0, r = (1LL << n);
		while(l < r){
			llong m = (l + r) / 2;
			if(best(n, m) <= p) l = m + 1;
			else r = m;
		}
		llong ret2 = l - 1;

		printf("Case #%d: %lld %lld\n", cas, ret1, ret2);
	}
	return 0;
}
