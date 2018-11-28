#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define FOR(I,A,B)	for(int I = (A); I < (B); ++I)
#define REP(I,N)	FOR(I,0,N)
#define ALL(A)		(A).begin(), (A).end()
#define MOD 1000002013
using namespace std;
long long p[555555];
long long o[555555];
long long e[555555];
int ord[555555];
long long n;

long long dist(long long s, long long end) {
	return ((end-s)*n-(end-s)*(end-s-1)/2)%MOD;
}

int main()
{
	int currTest,T;
	scanf("%d", &T);
	REP(currTest, T) {
		int m;
		scanf("%lld %d", &n, &m);
		REP(i, m) scanf("%lld %lld %lld", &o[i], &e[i], &p[i]);
		//REP(i, m) printf("%lld %lld\n", o[i], e[i]);
		REP(i, m) ord[i] = i;
		long long ans = 0;
		long long diff = 0;
		bool cont;
		do {
			cont = false;
			ans += diff;
			ans %= MOD;
			diff = 0;
			REP(i, m) {
				REP(j, m) {
					int k = ord[i], l = ord[j];
					if(i == j || o[k] == o[l]) continue;
					long long s1, s2, e1, e2;
					if(o[k] < o[l]) {
						s1 = o[k]; s2 = o[l];
						e1 = e[i]; e2 = e[j];
					} else {
						s1 = o[l]; s2 = o[k];
						e1 = e[j]; e2 = e[i];
					}
					if(e1 < s2) continue;

					long long x = min(p[i], p[j]);
					long long y = (dist(s1, e1)-dist(s2, e1)+dist(s2, e2)-dist(s1, e2));
//					printf("%lld %lld\n", dist(s1, e1)+dist(s2, e2), dist(s2, e1) + dist(s1, e2));
					//printf("%d %d: %lld %lld %lld %lld\n", i, j, s1, e1, s2, e2);
					if(y > 0) {
						cont = true;
						if(p[i] == p[j]) {
							diff += y*p[i];
							diff %= MOD;
							int tmp = ord[i];
							ord[i] = ord[j];
							ord[j] = tmp;
						} else if(p[i] < p[j]) {
							diff += x*y;
							diff %= MOD;
							o[m] = o[l];
							e[m] = e[j];
							ord[m] = m;
							p[m++] = p[j]-p[i];
							p[j] = p[i];
							int tmp = ord[i];
							ord[i] = ord[j];
							ord[j] = tmp;
						} else {
							diff += x*y;
							diff %= MOD;
							o[m] = o[k];
							e[m] = e[i];
							ord[m] = m;
							p[m++] = p[i]-p[j];
							p[i] = p[j];
							int tmp = ord[i];
							ord[i] = ord[j];
							ord[j] = tmp;
						}
					}
				}				
			}
		} while(cont);
//		REP(i, m) printf("%d %d %d\n", o[ord[i]], e[i], p[i]);

		printf("Case #%d: %lld\n", currTest+1, ans);
	}
	return 0;
}
