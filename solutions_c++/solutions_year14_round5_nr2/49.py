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
#define MODD(a,b) (((a)%(b)+(b))%(b))
#define REP(i,a,n) for (int i = (a); i < (n); i++)

int T;

int P, Q, N;
int H[200];
int G[200];
int dp[200][20000];

int main() {
	scanf("%d ", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d%d%d", &P, &Q, &N);
		REP(i,0,N) {
			scanf("%d%d", H+i, G+i);
		}
		REP(i,0,N+1)
		REP(u,0,20000)
			dp[i][u] = ((i == 0 && u == 1) ? 0 : -1E9);
		REP(i,0,N) {
			REP(u,0,20000) {
				if (dp[i][u] < 0)
					continue;
// 				if (dp[i][u] >= 0)
// 					printf("%d,%d: %d\n", i, u, dp[i][u]);
				REP(nr,0,1<<10) {
					int us = u;
					int K = 0, r = H[i];
					while(r > 0) {
						if (nr&(1<<K))
							r -= P;
						else
							r -= Q;
						K++;
					}
					bool ok = true;
					bool had = false;
					REP(k,0,K) {
						if (nr&(1<<k)) {
							if (had && (nr&(1<<(k-1))))
								ok = false;
							us--;
							if (us < 0)
								ok = false;
						} else {
							us++;
							had = true;
						}
					}
					if (ok) {
						int h = dp[i][u];
						if (nr&(1<<(K-1)))
							h += G[i];
						dp[i+1][us] = max(dp[i+1][us], h);
					}
				}
			}
		}
		int res = 0;
		REP(u,0,20000) {
			res = max(res, dp[N][u]);
		}
		printf("%d\n", res);
	}
	return 0;
}
