#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cstring>
#include <cassert>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long int64;
#ifdef HOME
	#define E(c) cerr<<#c
	#define Eo(x) cerr<<#x<<" = "<<(x)<<endl
	#define Ef(...) fprintf(stderr, __VA_ARGS__)
#else
	#define E(c) ((void)0)
	#define Eo(x) ((void)0)
	#define Ef(...) ((void)0)
#endif

const int SIZE = 1<<10;
const int NUM = 128;
typedef pair<int, int> pii;

int n, k;
int sum[SIZE];
int delta[SIZE];
pii interv[SIZE];

int res[NUM][NUM];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tests;
	scanf("%d", &tests);
	for (int tt = 1; tt<=tests; tt++) {
		scanf("%d%d", &n, &k);
		for (int i = 0; i < n-k+1; i++)
			scanf("%d", &sum[i]);

		for (int i = 0; i < n; i++) {
			if (i < k)
				delta[i] = 0;
			else
				delta[i] = sum[i-k+1] - sum[i-k];
		}
		Ef("delta: ");
		for (int i = 0; i < n; i++) Ef("%d ", delta[i]);
		Ef("\n");

		for (int i = 0; i < k; i++) {
			interv[i] = pii(0, 0);
			int now = 0;
			for (int j = i; j < n; j += k) {
				now += delta[j];
				interv[i].first = min(interv[i].first, now);
				interv[i].second = max(interv[i].second, now);
			}
		}
		Ef("intervals: \n");
		for (int i = 0; i < k; i++) Ef("  [%d %d]", interv[i].first, interv[i].second);
		Ef("\n");

		interv[0].first += sum[0];
		interv[0].second += sum[0];
		for (int i = 0; i < k; i++) {
			int t = interv[i].first / k * k;
			while (t > interv[i].first)
				t -= k;
			interv[i].first -= t;
			interv[i].second -= t;
		}

		int ans = 1000000000;
		for (int base = 0; base < k; base++) {
			int minlvl = interv[base].first;

			memset(res, 63, sizeof(res));
			res[0][0] = minlvl;
			for (int i = 0; i < k; i++) {
				for (int s = 0; s < k; s++) {
					int tres = res[i][s];
					if (tres > 1000000000) continue;
					for (int x = 0; x < k; x++) {
						pii intv = interv[i];
						intv.first += x;
						intv.second += x;
						while (intv.first < minlvl) {
							intv.first += k;
							intv.second += k;
						}
						while (intv.first - k >= minlvl) {
							intv.first -= k;
							intv.second -= k;
						}
						assert(intv.first >= minlvl);
						int nres = max(tres, intv.second);
						int ns = (s + x) % k;
						res[i+1][ns] = min(res[i+1][ns], nres);
					}
				}
			}

			ans = min(ans, res[k][0] - minlvl);
		}

		printf("Case #%d: %d\n", tt, ans);
		fflush(stdout);
	}
	return 0;
}
