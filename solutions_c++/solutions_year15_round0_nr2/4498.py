#include <stdio.h>
#include <vector>
#include <queue>
#include <map>
using namespace std;
#define FOR(I,S,T) for(int I=S;I<T;++I)
#define RNG(I,S,T) FOR(I,S,T+1)
#define REP(I,N) FOR(I,0,N)
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))


int main() {
	int TC;
	scanf("%d", &TC);
	RNG(tc, 1, TC) {
		int d, p, res = 0;
		scanf("%d", &d);
		vector<int> state(10);
		REP(i, d) {
			scanf("%d", &p);
			state[p] += 1;
			res = MAX(res, p);
		}
		map<vector<int>, bool> v;
		queue<vector<int> > q;
		q.push(state);
		v[state] = true;
		RNG(t, 0, 9) {
			int len = q.size();
			REP(qi, len) {
				vector<int> s = q.front();
				q.pop();
				int maxp = 0;
				RNG(i, 0, 9) if (s[i] > 0) maxp = i;
				res = MIN(res, t + maxp);
				vector<int> ns(10);
				RNG(i, 0, 8) ns[i] = s[i+1];
				if (!v[ns]) {
					v[ns] = true;
					q.push(ns);
				}
				RNG(i, 1, maxp/2) {
					vector<int> ns = s;
					ns[maxp] -= 1;
					ns[i] += 1;
					ns[maxp-i] += 1;
					if (!v[ns]) {
						v[ns] = true;
						q.push(ns);
					}
				}
			}
		}
		printf("Case #%d: %d\n", tc, res);
	}

	return 0;
}
