#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <assert.h>
#include <math.h>
#include <string.h>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,n) for (int i = 0; i < (n); i++)

int T, N;
ll B;
ll X[37];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%lld%d", &B, &N);
		REP(i, 37)
			X[i] = 0;
		REP(i, N)
			scanf("%lld", &X[i]);
		sort(X, X+37);
		double best = 0;
		for (int k = 0; k <= 36; k++) {
			if (k < 35 && X[k+2] > X[k+1]) {
				ll bs = 0;
				for (int i = 0; i <= k; i++)
					bs += X[k+1]-X[i];
				if (bs <= B) {
// 					fprintf(stderr, "bs1 = %lld (k=%d); ", bs, k);
					best = max(best, (double)(36-(k+2))/(k+2)*bs);
				}
			}
			for (int s = k+1; s < 36; s++) {
				ll A = X[s+1]-2;
				ll bs = 0, bs1 = 0;
				for (int i = 0; i <= k; i++)
					bs1 += A-X[i];
				bs = bs1;
				for (int i = k+1; i <= s; i++)
					bs += A+1-X[i];
				bool ok = true;
				if (bs > B) {
					ll ov = bs-B;
					ll m = (ov+s)/(s+1);
					if (m > A+1-X[s] || m > A-X[k])
						ok = false;
					bs1 -= m*(k+1);
					bs -= m*(s+1);
				}
				if (ok) {
// 					fprintf(stderr, "bsfds = %lld; ", bs);
					best = max(best, (double)36/(k+1)*bs1-bs);
				}
			}
			if (k < 36) {
				ll bs = 0;
				bool ok = true;
				for (int i = 0; i <= k; i++) {
					bs += X[k+1]-1-X[i];
					if (X[k+1]-1-X[i] < 0)
						ok = false;
				}
				if (bs > B) {
					ll ov = bs-B;
					ll m = (ov+k)/(k+1);
					if (m > X[k+1]-1-X[k])
						ok = false;
					else
						bs -= m*(k+1);
				}
				if (ok) {
// 					fprintf(stderr, "bs = %lld; ", bs);
					best = max(best, (double)(36-(k+1))/(k+1)*bs);
				}
			}
		}
		printf("%.9lf\n", best);
	}
	return 0;
}
