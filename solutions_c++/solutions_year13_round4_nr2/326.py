#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = (ll)1e15;

int TC, TCC;
ll N, M, P;

ll A (int n, ll p) {
	if(n == 0) return 0;
	else if(p == (1ll << n)) return p - 1;
	else if(p <= (1ll << (n - 1))) return 0;
	return 2 * A(n - 1, p - (1ll << (n - 1))) + 2;
}

ll res1() {
	if(M == P) return P - 1;
	return A(N, P);
}

ll B (int n, ll p) {
	if(n == 0) return 0;
	else if(p == (1ll << n)) return p - 1;
	else if(p > (1ll << (n - 1))) return (1ll << n) - 2;
	return B(n - 1, p) << 1;
}

ll res2() {
	if(M == P) return P - 1;
	return B(N, P);
}

int main() {
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);

    int i, j, k;

	scanf("%d", &TC);
	while(++TCC <= TC) {
		printf("Case #%d: ", TCC);

		scanf("%lld%lld", &N, &P);
		M = 1ll<<N;

		printf("%lld %lld", res1(), res2());

		puts("");
	}

	return 0;
}