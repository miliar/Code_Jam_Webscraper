#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define DEBUG(x) cout << ">>> " << #x << " = " << (x) << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0;i<(a);++i)

#define INF (1<<29)
typedef long long ll;

const int MAXN = 40;

int T;
int N;
ll B;
ll X[MAXN];

double val(double sum, int cnt, ll rem) {
	//fprintf(stderr, "val %lf %d %lld = %lf\n", sum, cnt, rem, 36.0*sum/cnt-B+rem);
	return 36.0*sum/cnt-B+rem;
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%lld%d", &B, &N);
		REP(i,N) scanf("%lld", X+i);
		sort(X,X+N, greater<ll>());
		double best = 0.0;
		ll ml = 0;
		if (N == 37) {
			ml = X[N-1];
		}
		while (true) {
			int cnt = 37-N;
			ll rem = B - ml*cnt;
			if (rem < 0) break;
			REP(i,N) if (X[i] < ml) rem -= ml - X[i];
			if (rem < 0) break;
			double sum = cnt*ml;
			REP(i,N) if (X[i] <= ml) {
				++cnt;
				sum += ml-X[i];
			}
			double opt1 = val(sum, cnt, rem);
			REP(i,N) if (X[i] <= ml) {
				if (rem > 0) {
					--rem;
					--cnt;
					sum -= ml-X[i];
				}
			}
			double opt2 = val(sum, cnt, rem);
			best = max(best, opt1);
			best = max(best, opt2);
			//fprintf(stderr, "%lld -- %lf\n", ml, opt);
			fflush(stderr);
			++ml;
		}
		printf("Case #%d: %.10lf\n", t+1, best);
		fflush(stdout);
	}
	return 0;
}
