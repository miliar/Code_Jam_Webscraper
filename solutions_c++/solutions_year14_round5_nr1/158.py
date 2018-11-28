#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstring>
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
#define DEBUG(x) cerr << '>' << #x << ':' << x << endl;
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a) for(int i=0; i<(a);++i)
inline bool EQ(double a, double b) {return fabs(a-b) < 1e-9;}

const int INF = 1<<29;
typedef long long ll;

const int MAXN = 1000100;

int T, N;
ll P, Q, R, S;

ll values[MAXN];
ll prefix[MAXN];

ll sum(int it1, int it2) {
	return prefix[it2] - prefix[it1];
}

int main() {
	scanf("%d", &T);
	REP(t,T) {
		scanf("%d%lld%lld%lld%lld", &N, &P, &Q, &R, &S);

		prefix[0] = 0;

		REP(i,N) {
			values[i] = ((i * P + Q) % R + S);
			prefix[i+1] = prefix[i] + values[i];
		}

		int it1 = 0, it2 = 0;
		ll total = sum(0, N);
		ll best = total;
		while (true) {
			ll s1 = sum(0, it1);
			ll s2 = sum(it1, it2);
			ll s3 = sum(it2, N);

			ll m = max(max(s1, s2), s3);
			if (m < best) {
				best = m;
			}

			if (s1 > s2 && s1 > s3) {
				break;
			}

			if (s2 > s3 && s2 > s1) {
				++it1;
				continue;
			}

			++it2;
		}

		printf("Case #%d: %.10lf\n", t+1, 1.0 - (double)best / total);
	}
	return 0;
}
