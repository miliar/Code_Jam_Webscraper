#include <functional>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cassert>
#include <bitset>
#include <cstdio>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;

const int INF = 1000 * 1000 * 1000;

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define ALL(v) v.begin(), v.end()
#define SZ(v) (int) v.size()
#define MP make_pair
#define PB push_back

#define TASK ""

ll m[1 << 7];

int main() {

	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;

	scanf("%d", &T);

	int cnt = 0;

	while (T--) {
		ll A, N;
		scanf("%I64d%I64d", &A, &N);
		REP(i, N) {
			scanf("%I64d", &m[i]);
		}
		sort(m, m + N);
	/*	int result = N;
		for (int mask = 1; mask < (1 << N); ++mask) {
			int cur = 0;
			vector<int> tmp;
			REP(bit, N)
				if (mask & (1 << bit)) {
					tmp.PB(m[bit]);
				} else {
					++cur;
				}
			if (A == 1) {
				continue;
			}
			int aa = A;
			REP(i, SZ(tmp)) {
				while (aa <= tmp[i]) {
					++cur;
					aa = 2 * aa - 1;
				}
				aa += tmp[i];
			}
			result = min(result, cur);
		}*/
		ll R = N;
		for (int i = 0; i < N; ++i) {
			ll cur = N - i - 1;
			if (A == 1) {
				continue;
			}
			ll aa = A;
			REP(j, i + 1) {
				while (aa <= m[j]) {
					++cur;
					aa = 2 * aa - 1;
				}
				aa += m[j];
			}
			R = min(R, cur);
		}
	/*	if (R != result) {
			puts("!");
			return 0;
		}*/
		printf("Case #%d: %I64d\n", ++cnt, R);
	}
	

	return 0;
}