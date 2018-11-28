#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	for(int ii = 0; ii < T; ++ ii) {
		int N; int K;
		scanf("%d%d", &N, &K);
		vector<double> P(N);
		for(int i = 0; i < N; ++ i)
			scanf("%lf", &P[i]);
		vector<double> dp;
		double ans = 0;
		rep(i, 1 << N) {
			int p = 0;
			rep(j, N) p += i >> j & 1;
			if(p == K) {
				dp.assign(K + 1, 0);
				dp[0] = 1;
				int num = 0;
				rep(j, N) if(i >> j & 1) {
					double prob = P[j];
					++ num;
					for(int k = num; k >= 0; -- k) {
						dp[k] *= 1 - prob;
						if(k > 0) dp[k] += dp[k - 1] * prob;
					}
				}
				amax(ans, dp[K / 2]);
			}
		}
		printf("Case #%d: %.10f\n", ii + 1, ans);
	}
	return 0;
}
