#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

const int MOD = 1000002013;
int n, m;
int l[10000];
int x[10005], y[10005], z[10005];
int c[10005];

	int calc(int v)
	{
		return (((int64)(2LL * n - (int64)v + 1) * (int64)v) / 2LL) % MOD;
	}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int Tests, tts = 0;
	for (scanf("%d", &Tests); Tests--; ) {
		scanf("%d%d", &n, &m);
		int ans = 0;
		l[0] = 0;
		for (int i = 1; i <= m; ++i) {
			scanf("%d%d%d", &x[i], &y[i], &z[i]);
			int64 tmp = calc(y[i] - x[i]);
			tmp = tmp * (int64)z[i] % MOD;
			ans += tmp;
			if (ans >= 1000002013) ans -= 1000002013;
			l[++l[0]] = x[i];
			l[++l[0]] = y[i];
		}
		//printf("%d\n", ans);
		sort(l + 1, l + l[0] + 1);
		l[0] = unique(l + 1, l + l[0] + 1) - (l + 1);
		//printf("%d\n", l[0]);
		//for (int i = 1; i <= l[0]; ++i) printf("%d ", l[i]); puts("");
		ME(c);
		for (int i = 1; i <= m; ++i) {
			x[i] = lower_bound(l + 1, l + l[0] + 1, x[i]) - (l + 1) + 1;
			y[i] = lower_bound(l + 1, l + l[0] + 1, y[i]) - (l + 1) + 1;
			//printf("%d %d\n", x[i], y[i]);
			for (int j = x[i]; j < y[i]; ++j) {
				c[j] += z[i];
				if (c[j] >= MOD) c[j] -= MOD;
			}
		}

		int ans2 = 0;
		for (;;) {
			int la = 1;
			int64 mn = 1LL << 60;
			bool ff = 1;
			for (int j = 1; j <= l[0]; ++j)
			if (c[j] == 0) {
				if (j > la) {
					ff = 0;
					//printf("%d %d\n", l[la], l[j]);
					for (int k = la; k < j; ++k) c[k] -= mn;
					int64 tmp = calc(l[j] - l[la]);
					tmp = tmp * mn % MOD;
					ans2 += tmp;
					if (ans2 >= MOD) ans2 -= MOD;
				}
				la = j + 1;
				mn = 1LL << 60;
			} else mn = min(mn, (int64)c[j]);
			if (ff) break;
		}
		//printf("%d\n", ans2);
		ans = ((ans + MOD - ans2) % MOD + MOD) % MOD;
		printf("Case #%d: %d\n", ++tts, ans);
	}
	return 0;
}
