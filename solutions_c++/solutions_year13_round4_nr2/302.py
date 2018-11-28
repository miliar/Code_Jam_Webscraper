#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int n;
long long p;

long long pow2[64];

void input() {
	scanf("%d%lld", &n, &p);
}

long long search_best(int tn, long long tp) {
	if(tp == 1) return 0;
	if(tp == pow2[tn]) return pow2[tn]-1;

	if(tp <= pow2[tn-1]) return 0;
	
	return search_best(tn-1, tp-pow2[tn-1])*2 + 2;
}

long long search_possible(int tn, long long tp) {
	if(tp == 1) return 0;
	if(tp == pow2[tn]) return pow2[tn]-1;

	if(tp <= pow2[tn-1]) return 2*search_possible(tn-1, tp);
	return pow2[tn]-2;
}

void solve() {
	pow2[0] = 1;
	for(int i = 1;i < 64;i ++) pow2[i] = pow2[i-1]*2;

	printf("%lld %lld\n", search_best(n, p), search_possible(n, p));
}

int main() {
	freopen("B-large.in", "r", stdin);
	//freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t = 1;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}