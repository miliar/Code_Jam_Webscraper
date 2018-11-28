#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <iostream>
#include <math.h>
#include <time.h>
#include <unistd.h>
#include <algorithm>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <string>

#ifndef ONLINE_JUDGE
	#define DEBUG(x) cout << '>' << #x << ':' << x << endl;
#else
	#define DEBUG(x) do {} while(0);
#endif

#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define FOR(i, A, N) for(int (i) = (A); (i) < (N); (i)++)
#define REP(i, N) for(int (i) = 0; (i) < (N); (i)++)

using namespace std;
typedef long long ll;
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }

int n,m,k;
long double P[222];
int T;
vector<int> V;

void solve() {
	scanf("%d%d", &n, &k);
	REP(i, n) scanf("%Lf", P+i);
	long double ans = 0;
	REP(i, (1<<n)) {
		V.clear();
		REP(j, n) if(i&(1<<j)) { V.pb(j);}
		if(V.size() == k) {
			long double cans = 0;
			REP(j, 1<<k) {
				int c = 0;
				long double prob = 1.0;
				REP(z, k) if(j&(1<<z)) {
					prob *= P[V[z]];
					c++;
				} else {
					prob *= 1-P[V[z]];
				}
				if(c == k/2) {
					cans += prob;
				}
			}
			ans = max(ans, cans);
		}
	}
	printf("%.10Lf", ans);
}

int main() {
	scanf("%d", &T);
	REP(testc, T) {
		printf("Case #%d: ", testc+1);
		solve();
		printf("\n");
	}
	return 0;
}
