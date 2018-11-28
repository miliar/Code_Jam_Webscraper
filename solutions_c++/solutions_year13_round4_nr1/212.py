#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

typedef long long LL; 

const int MOD = 1000002013;
const int MAXN = 1010;

vector<LL> a, b;

LL o[MAXN], e[MAXN], p[MAXN];
LL N;

LL calc(int k) {
	LL L = N + N - k + 1;
	return (L * k / 2) % MOD;
}

int main() {
	int T;
	freopen("x.txt", "r", stdin); freopen("w.txt", "w", stdout);
	scanf("%d", &T);
	for (int re = 1; re <= T; re++) {
		int n, m;
		LL org = 0;
		scanf("%d%d", &n, &m);
		N = n;
		a.clear();
		b.clear();
		for (int i = 0; i < m; i++) {
			scanf("%lld%lld%lld", o + i, e + i, p + i);
			b.PB(o[i]);
			b.PB(e[i]);
			org += calc(e[i] - o[i]) * p[i] % MOD;
			org %= MOD;
		}
		sort(b.begin(), b.end());
		b.erase(unique(b.begin(), b.end()), b.end());
		// for (int i = 0; i < b.size(); i++) printf("%d ", b[i]); puts("");
		for (int i = 0; i < b.size() - 1; i++) {
			LL t = 0;
			for (int j = 0; j < m; j++) {
				if (o[j] <= b[i] && b[i+1] <= e[j]) {
					t += p[j];
				}
			}
			a.PB(t);
			// printf("%d ", a[i]);
		}
		// puts("");
		// printf("%lld\n", org);
		LL ans = 0;
		
		for (int i = 0; i < b.size() - 1; i++) {
			while (a[i] > 0) {
				LL t = a[i];
				// printf("a[%d] = %lld\n", i, a[i]);
				for (int j = i; j < b.size() - 1; j++) {
					if (a[j] == 0) break;
					t = min(t, a[j]);
				}
				int j;
				for (j = i; j < b.size() - 1; j++) {
					if (a[j] == 0) {
						break;
					}
					a[j] -= t;
				}
				// printf("t = %lld %d %d\n", t, b[i], b[j]);
				ans += (t % MOD) * calc(b[j] - b[i]) % MOD;
				ans %= MOD;
				// printf("ans = %lld\n", ans);
			}
		}
		ans = ((org - ans) % MOD + MOD) % MOD;
		printf("Case #%d: %lld\n", re, ans);
	
	}
}
